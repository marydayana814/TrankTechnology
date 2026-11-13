import pytest
from pages.country import Country

@pytest.mark.country
def test_country_function(page):
    country_obj = Country(page)
    country_obj.country_function()