class Country:
    def __init__(self, page):
        self.page = page
        self.country = page.locator('//select[@id="countrySelector"]')
        self.options = ['USA', 'UAE', 'India']

    def country_function(self):
        for o in self.options:
            self.country.click()
            self.page.locator('//select[@id="countrySelector"]').select_option(o)
            self.page.wait_for_timeout(5000)