class Blog:
    def __init__(self, page):
        print(page)
        self.page = page
        # #blog
        self.blog = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')
        self.blog_app_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/app-development/"])[2]')
        self.art_int = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/artificial-intelligence/"]')
        self.cont_mrk = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/content-marketing/"]')
        self.blog_crm_dev = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/crm-development/"]')
        self.blog_dig_mrk = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/digital-marketing/"]')
        self.blog_ecom_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ecommerce-development/"])[5]')
        self.blog_e_mark = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/email-marketing/"]')
        self.blog_grp_des = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/graphic-design/"])[3]')
        self.blog_sf_cmp = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-it-company/"]')
        self.sft_Dev = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-development/"]')
        self.ux_desng = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ui-ux-design/"])[5]')
        self.web_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/web-development/"])[5]')
        self.blog_elements = [self.blog_app_dev, self.art_int, self.cont_mrk, self.blog_crm_dev, self.blog_dig_mrk, self.blog_ecom_dev, 
                              self.blog_e_mark, self.blog_grp_des, self.blog_sf_cmp, self.sft_Dev, self.ux_desng, self.web_dev]

    def blog_function(self):
        self.blog.click()
        for b in self.blog_elements:
            b.click()
            self.page.wait_for_load_state('load')
            self.page.go_back()


       
