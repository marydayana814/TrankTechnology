class ContactUs:
    def __init__(self, page):
        self.page = page
        self.contact_us = page.locator('(//[@href="https://www.tranktechnologies.com/contact-us"])[1]')
        self.cts_web_dev = page.locator('//a[@href="https://www.tranktechnologies.com/web-development-company"]')
        self.cts_cms = page.locator('//a[@href="https://www.tranktechnologies.com/web-development-company"]')
        self.cts_ecom = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[7]')
        self.cts_custom = page.locator('//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company"]')
        self.cts_app_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/app-development-company"])[1]')
        self.cts_ios_app = page.locator('(//a[@href="https://www.tranktechnologies.com/ios-mobile-app-development-company"])[1]')
        self.cts_and_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/android-mobile-app-development-company"])[1]')
        self.cts_hybrid = page.locator('(//a[@href="https://www.tranktechnologies.com/hybrid-mobile-app-development-company"])[1]')
        self.cts_cross = page.locator('(//a[@href="https://www.tranktechnologies.com/cross-platform-mobile-app-development-company"])[1]')
        self.cts_prog_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/progressive-web-app-development-company"])[1]')
        self.cts_grp_dsn = page.locator('(//a[@href="https://www.tranktechnologies.com/graphic-design-company"])[1]')
        self.cts_logo_dsn = page.locator('(//a[@href="https://www.tranktechnologies.com/logo-design-company"])[1]')
        self.cts_bnr_dsn = page.locator('(//a[@href="https://www.tranktechnologies.com/banner-design-company"])[1]')
        self.cts_pkg_dsn = page.locator('(//a[@href="https://www.tranktechnologies.com/packaging-design-company"])[1]')
        self.cts_bsn_den = page.locator('(//a[@href="https://www.tranktechnologies.com/business-cards-design-company"])[1]')
        self.cts_elements = [self.cts_web_dev, self.cts_cms, self.cts_ecom, self.cts_custom, self.cts_app_dev, 
                             self.cts_ios_app, self.cts_and_dev, self.cts_hybrid, self.cts_cross, self.cts_prog_dev, self.cts_grp_dsn,
        self.cts_logo_dsn, self.cts_bnr_dsn, self.cts_pkg_dsn]


    def contact_us_function(self):
        self.contact_us.click()
        for c in self.cts_elements:
            c.click()
            self.page.wait_for_load_state('load')
            print(self.page.title())
            self.page.go_back()
