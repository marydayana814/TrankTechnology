class Technologies:
    def __init__(self, page):
        self.page = page
        self.technologies = page.locator("(//a[text()='Technologies'])[1]")
        self.ecomerce_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.mgnto_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.code_ignit = page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
        self.big_commerce = page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
        self.cs_cart_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
        self.nop_commerce = page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.open_cart = page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.word_press = page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.shopify = page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.node_js = page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
        self.woo_commerce = page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
        self.ecomerce_dev_elements = [self.mgnto_dev, self.code_ignit, self.big_commerce, 
                                            self.cs_cart_dev, self.nop_commerce, self.open_cart, self.word_press, self.shopify,self. node_js, self.woo_commerce]

   
        self.mobile_dev = page.locator("//strong[text()='Mobile App Development']")
        self.react_mob_app = page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.xamarin_mob_app = page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.flutter_mob_app = page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.swift_mob_app = page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.enterprise_app = page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.kotlin_app = page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.ionic_app = page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.appointment_app = page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')
        self.mob_app_elements = [self.mobile_dev, self.react_mob_app, self.xamarin_mob_app, self.flutter_mob_app,
                                 self.swift_mob_app, self.enterprise_app, self.kotlin_app, self.ionic_app]

        #artificial intelligence
        self.artificial_intl = page.locator("//strong[text()='Artificial Intelligence']")
      


    def ecommerce_function(self):
        for e in self.ecomerce_dev_elements:
            self.technologies.hover()
            self.ecomerce_dev.hover()
            e.click()
            print(self.page.title())
            self.page.wait_for_load_state('load')
            self.page.go_back()

    def mobile_app_def_function(self):
        for m in self.mob_app_elements:
            self.technologies.hover()
            self.mobile_dev.hover()
            m.click()
            print(self.page.title())
            self.page.wait_for_load_state('load')
            self.page.go_back()

    