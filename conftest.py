import base64
import os
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright
from pytest_html import extras

from config import BASE_URL

video_path_key = pytest.StashKey[Path]()


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        headless_setting = os.getenv("PLAYWRIGHT_HEADLESS")
        if headless_setting is None:
            headless = (
                os.getenv("CI", "").strip().lower() in {"1", "true", "yes", "on"}
                or any(
                    os.getenv(name)
                    for name in ("JENKINS_URL", "JENKINS_HOME", "BUILD_TAG")
                )
            )
        else:
            headless = headless_setting.strip().lower() in {
                "1",
                "true",
                "yes",
                "on",
            }

        browser = playwright.chromium.launch(headless=headless)
        yield browser
        browser.close()


@pytest.fixture
def page(browser, request):
    videos_dir = Path("videos")
    videos_dir.mkdir(exist_ok=True)
    context = browser.new_context(
        ignore_https_errors=True,
        record_video_dir=str(videos_dir),
    )
    page = context.new_page()

    try:
        page.goto(BASE_URL)
        page.wait_for_load_state("load")
        yield page
    finally:
        try:
            video = page.video
            if video is not None:
                request.node.stash[video_path_key] = Path(video.path())
        finally:
            context.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    report_extras = getattr(report, "extras", [])

    if report.when == "call" or (
        report.when == "setup" and (report.failed or report.skipped)
    ):
        test_path = Path(str(item.path))
        report_extras.append(
            extras.text(
                test_path.read_text(encoding="utf-8"),
                name=f"Test script: {test_path.name}",
            )
        )

        if report.failed:
            page = item.funcargs.get("page")

            if page:
                screenshots_dir = Path("screenshots")
                screenshots_dir.mkdir(exist_ok=True)

                file_name = screenshots_dir / f"{item.name}.png"

                page.screenshot(path=str(file_name))

                report_extras.append(extras.image(str(file_name)))

        report.extras = report_extras

    if report.when == "teardown":
        video_path = item.stash.get(video_path_key, None)
        if video_path is not None:
            if not video_path.is_file():
                raise FileNotFoundError(
                    f"Playwright video was not created: {video_path}"
                )

            if item.config.getoption("self_contained_html"):
                video_content = base64.b64encode(video_path.read_bytes()).decode(
                    "ascii"
                )
            else:
                report_path = item.config.getoption("htmlpath")
                report_dir = (
                    Path(report_path).resolve().parent if report_path else Path.cwd()
                )
                video_content = os.path.relpath(
                    video_path.resolve(), report_dir
                ).replace("\\", "/")

            report_extras.append(
                extras.video(
                    video_content,
                    name=f"Video: {item.name}",
                    mime_type=(
                        "video/webm"
                        if video_path.suffix.lower() == ".webm"
                        else "video/mp4"
                    ),
                    extension=video_path.suffix.lstrip("."),
                )
            )
            report.extras = report_extras