import pytest
from pages.technologies import Technologies


@pytest.mark.ecomerce
def test_ecommerce_function(page):
    trading_obj = Technologies(page)
    trading_obj.ecommerce_function()

@pytest.mark.ecomerce
def test_mobile_app_def_function(page):
    trading_obj = Technologies(page)
    trading_obj.mobile_app_def_function()