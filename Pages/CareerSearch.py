import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CareerSearch:



    def __init__(self, driver):
        self.driver = driver
        self.careerLinkClass = "/html/body/div[2]/div[1]/div[2]/div[2]/div/ul/li[4]/a"
        self.workOfferSpan = "/html/body/div[2]/div[5]/div[1]/div/div/div/div[1]/ul/li/a/span"
        self.localizationXpath = "/html/body/section/div/div/div/div[2]/div[3]/div[2]/div/a"
        # nie wchodzi Lublin| moze trzeba pobrac wszystkie labele i ifem wybrac ten ktorego data-name ='lublin, bo nie chodzi w selektorze data-name'

        #self.localizationLublinSpan = "//label[@data-name ='Lublin']/div[contains(@class, 'sii-m-checkbox-line')]/input[@type = 'checkbox']"

        self.localizationLublinSpan = "//label[@data-name ='Lublin']/div[contains(@class, 'sii-m-checkbox-line')]/span[contains(@class, 'sii-m-checkbox-line__input')]"

        # self.localizationLublinSpan = "//span[text()='Lublin']"
        #self.localizationLublinSpan = "//span[contains(text(),'Lublin')]"

        self.categories = "/html/body/section/div/div/div/div[2]/div[3]/div[3]/div/a"
        self.categoriesTesting = "//span[text()='Testing & QA']"
        self.searchIcon = "//a[contains(@class, 'js-search-button')]"

        #lista ofert z Lublina
        self.job_localization_xpath = "//div[contains(@class, 'sii-o-grid__wrapper__item')]//h3[contains(@class, 'sii-o-card-job__title')]"

        #lista dostępnych lokalizacji w ramach danej karty
        self.cities_list = "sii-o-card-job__location__cities"



    def work_search(self):


        self.driver.find_element_by_xpath(self.careerLinkClass).click()
        self.driver.find_element_by_xpath(self.workOfferSpan).click()

        self.driver.find_element_by_xpath(self.localizationXpath).click()
        elementLublin = self.driver.find_element_by_xpath(self.localizationLublinSpan)
        self.driver.execute_script("arguments[0].click();", elementLublin)


        self.driver.find_element_by_xpath(self.categories).click()
        elementCategories = self.driver.find_element_by_xpath(self.categoriesTesting)
        self.driver.execute_script("arguments[0].click();", elementCategories)
        self.driver.find_element_by_xpath(self.searchIcon).click()
        time.sleep(3)

        #self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)

        self.driver.execute_script("window.scrollTo(0, 2100);")
        time.sleep(3)


        wait = WebDriverWait(self.driver, 10)
        jobs = wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, self.job_localization_xpath)))

        #pobranie miast przypisanych do ofert
        cities_of_offert = self.driver.find_elements_by_class_name(self.cities_list)



        # obsłużenie okienka z ilością wyników
        search_results = self.driver.find_element_by_xpath("//span[contains(@class, 'js-ajax-load-number')]")
        print(search_results.text)
        self.results_digit = "".join(char for char in search_results.text if char.isdigit())

        #wypisanie nazw ofert
        counter = 1
        for job in jobs:

            print(str(counter) + ". " + job.text)
            counter += 1

        print("Ofert z Lublina jest " + str(len(jobs)))



        #self.driver.save_screenshot("sii.png")


        assert len(jobs) == int(self.results_digit)

        for city in cities_of_offert:
            if "Lublin" in city.text:
                return True
        print("All offerts contain city of Lublin in it")


        #pobiera nie tą ilość ofert co trzeba

        # przy powolnym scrollu łapie wszystkie 25 elementow, czyli tak jakby łapie te elementy które widzi

        # kolejny pomysl to: zrobic wlasnego explicita ktory najpierw wczyta ile jest ofert z "znalezionych wynikow" i poczeka az ofert bedzie dokladnie tyle

        # timeout exception, nie znajduje wszystkich wyników więc wywala
        # jobs = WebDriverWait(self.driver, 10).until(lambda wd: len(wd.find_elements(By.XPATH, self.job_localization_xpath)) == int(self.results_digit))