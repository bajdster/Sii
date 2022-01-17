
class JobOffers:
    def __init__(self, driver):
        self.driver = driver
        self.job_localization_xpath = "//div[contains(@class, 'sii-o-card-job ')]//dd[contains(@text, 'Lublin')]"


    def offers_from_lublin(self):
        jobs = self.driver.find_elements_by_xpath(self.job_localization_xpath)
        print("ofert z Lublina jest" + str(len(jobs)))

