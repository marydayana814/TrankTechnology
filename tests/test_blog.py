import pytest
from pages.blog import Blog

@pytest.mark.blog
def test_blog_function(page):
    blog_obj = Blog(page)
    blog_obj.blog_function()
