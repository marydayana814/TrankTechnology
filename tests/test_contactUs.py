import pytest
from pages.contactUs import ContactUs

@pytest.mark.contactUs
def test_contact_us_function(page):
    contactUs_obj = ContactUs(page)
    contactUs_obj.contact_us_function()