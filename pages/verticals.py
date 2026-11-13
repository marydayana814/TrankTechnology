class Vertical:
    def __init__(self, page):
        self.page = page
        #locators of verticals
        self.verticals = page.locator("(//a[text()='Verticals'])[1]")
        self.technologies = page.locator("(//a[text()='Technologies'])[1]")
        self.trading = page.locator("//strong[text()='Trading']")
        self.stock_trading = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
        self.paper_trading = page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
        self.cfd_trading = page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
        self.massachusetts_trading = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.algo_trading = page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
        self.custom_trading = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.webportal_trading = page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')
        self.trading_elements = [self.stock_trading, self.paper_trading, self.cfd_trading, self.massachusetts_trading, 
                                 self.algo_trading, self.custom_trading, self.webportal_trading]

        #retail and commerce
        self.retail_commerce = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
        self.ecomerce_website = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[2]')
        self.ecomerce_app = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')
        self.retail_commerce_elements = [self.ecomerce_website, self.ecomerce_app]

        #health care
        self.health_care = page.locator('//li[@data-id="healthcare"]')
        self.diet_nutritients = page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.health_tracking_app = page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')
        self.health_care_option = [self.diet_nutritients, self.health_tracking_app]

        #fintech 
        self.fintech = page.locator('(//li[@data-id="fintech"])[1]')
        self.pos_software = page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.crypto = page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')
        self.fintench_element = [self.pos_software, self.crypto]

        #custom app
        self.custom_app = page.locator("//strong[text()='Custom App']")
        self.desktop_app = page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.hrm_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.travel = page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.dating_app = page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.crm_dev_usa = page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
        self.crm_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.erp_app = page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.e_learning = page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.real_estate = page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')
        self.custom_app_element = [self.desktop_app, self.hrm_dev, self.travel, self.dating_app, 
                                   self.crm_dev_usa, self.crm_dev, self.erp_app, self.e_learning, self.real_estate]
 
         
    def trading_function(self):
        for t in self.trading_elements:
            self.verticals.hover()
            self.trading.hover()
            t.click()
            self.page.wait_for_load_state('load')
            print(self.page.title())
            self.page.go_back()
            self.page.wait_for_timeout(2000)

    def retail_functions(self):
        for r in self.retail_commerce_elements:
            self.verticals.hover()
            self.retail_commerce.hover()
            r.click()
            self.page.wait_for_load_state('load')
            print(self.page.title())
            self.page.go_back()
            self.page.wait_for_timeout(2000)

    def healthcare_function(self):
        for h in self.health_care_option:
            self.verticals.hover()
            self.health_care.hover()
            h.click()
            self.page.wait_for_load_state('load')
            self.page.go_back()
            self.page.wait_for_timeout(5000)

    def fintech_function(self):
        for f in self.fintench_element:
            self.verticals.hover()
            self.fintech.hover()
            f.click()
            self.page.wait_for_load_state('load')
            self.page.go_back()
            self.page.wait_for_timeout(2000)

    def customapp_function(self):
        for c in self.custom_app_element:
            self.verticals.hover()
            self.custom_app.hover()
            c.click()
            self.page.wait_for_load_state('load')
            self.page.go_back()
            self.page.wait_for_timeout(2000)

    def ecommerce_function(self):
        for e in self.ecomerce_dev_elements:
            self.technologies.hover()
            self.ecomerce_dev.hover()
            e.click()
            print(self.page.title())
            self.page.wait_for_load_state('load')
            self.page.go_back()
            self.page.wait_for_timeout(2000)

    
   
 
                


        