from selenium.webdriver import ActionChains


class CareerSearch:

    def __init__(self, driver):
        self.driver = driver
        self.careerLinkClass = "/html/body/div[1]/div[1]/div[2]/div[2]/div/ul/li[4]/a"
        self.workOfferSpan = "/html/body/div[1]/div[5]/div[1]/div/div/div/div[1]/ul/li/a/span"
        self.localizationXpath = "/html/body/section/div/div/div/div[2]/div[3]/div[2]/div/a"
        # nie wchodzi Lublin| moze trzeba pobrac wszystkie labele i ifem wybrac ten ktorego data-name ='lublin, bo nie chodzi w selektorze data-name'
        # pomysl 2 aria-label?

        #self.localizationLublinSpan = "//label[contains(@class, 'js-locationOption')]/div[contains(@class, 'sii-m-checkbox-line')]/input[@type = 'checkbox']"

        #self.localizationLublinSpan = "//label[@data-name ='Lublin']/div[contains(@class, 'sii-m-checkbox-line')]/input[@type = 'checkbox']"

        self.localizationLublinSpan = "//label[@data-name ='Lublin']/div[contains(@class, 'sii-m-checkbox-line')]/span[contains(@class, 'sii-m-checkbox-line__input')]"

        #self.localizationLublinSpan = "//label[@data-name ='Lublin']"
        #self.localizationLublinSpan = "//div[@class ='-col2']//span[text()='Lublin']"
        # self.localizationLublinSpan = "//span[text()='Lublin']"
        #self.localizationLublinSpan = "//span[contains(text(),'Lublin')]"

        '''self.categories = "/html/body/section/div/div/div/div[2]/div[3]/div[3]/div/a"
        self.categoriesTesting = "//span[text()='Testing & QA']"
        self.searchIcon = "/html/body/section/div/div/div/div[2]/div[3]/a"'''

    def work_search(self):
        self.driver.find_element_by_xpath(self.careerLinkClass).click()
        self.driver.find_element_by_xpath(self.workOfferSpan).click()
        self.driver.find_element_by_xpath(self.localizationXpath).click()
        #Lublin = self.driver.find_element_by_xpath(self.localizationLublinSpan)
        print(len(self.localizationLublinSpan))
        element = self.driver.find_element_by_xpath(self.localizationLublinSpan)
        self.driver.execute_script("arguments[0].click();", element)
        #^cos klika ale otweira sie strona lublin-oddzial


        #ActionChains(self.driver).move_to_element(Lublin).click(Lublin).perform()
        '''self.driver.find_element_by_xpath(self.categories).click()
        QA = self.driver.find_element_by_xpath(self.categoriesTesting).click()
        ActionChains(self.driver).move_to_element(QA).click(QA).perform()
        self.driver.find_element_by_xpath(self.searchIcon).click()'''

