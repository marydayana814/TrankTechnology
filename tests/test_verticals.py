import pytest
from pages.verticals import Vertical


@pytest.mark.smoke
def test_vertical_function(page):
    trading_obj = Vertical(page)
    trading_obj.trading_function()

@pytest.mark.reg
def test_retail_functions(page):
    retail_obj = Vertical(page)
    retail_obj.retail_functions()

@pytest.mark.reg
def test_healthcare_function(page):
    health_obj = Vertical(page)
    health_obj.healthcare_function()

@pytest.mark.reg
def test_healthcare_function(page):
    fintech_obj = Vertical(page)
    fintech_obj.fintech_function()

@pytest.mark.reg
def test_custom_function(page):
    customapp_obj = Vertical(page)
    customapp_obj.customapp_function()


