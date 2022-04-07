from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager

from Pages.CareerSearch import CareerSearch
from Pages.JobOffersVerification import JobOffers


class TestWorkOfferSearch:
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        #self.driver.implicitly_wait(10)
        yield
        #self.driver.quit()
    def test_work_offers(self, setup):
        self.driver.get("https://sii.pl/")
        search_work_offers = CareerSearch(self.driver)
        search_work_offers.work_search()


        #work_offers_verification = JobOffers(self.driver)
        #work_offers_verification.offers_from_lublin()
