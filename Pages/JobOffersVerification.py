#tymczasowow nie uzywany
class JobOffers:
    def __init__(self, driver):
        self.driver = driver

        #self.job_localization_xpath = "//div[contains(@class, 'sii-o-card-job ')]//dd[contains(@text, 'Lublin')]"
        self.job_localization_xpath = "//div[contains(@class, 'sii-o-grid__wrapper__item')]//h3[contains(@class, 'sii-o-card-job__title')]"
        #dokończyć wyszukiwanie ofert z Lublina bo znajduje 0"


    def offers_from_lublin(self):
        jobs = self.driver.find_elements_by_xpath(self.job_localization_xpath)


        for job in jobs:
            print(job.text)
            # wciaz za malo ofert pobiera oferty pracy zanim wejdzie do pracy fitr wyszukiwarki, dlaczego nie działa implicitlywait ???

        #print(len(jobs))
        print("ofert z Lublina jest " + str(len(jobs)))
        #print(jobs)
        #Wyszukuje 16 ofert a powinno byc 19

