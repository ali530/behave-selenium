from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        # Element locators unified using XPath
        self.icon_search = (By.XPATH, "//a[@title='fal fa-search']")
        self.input_search = (By.XPATH, "//input[@id='searchField']")
        self.button_submit = (By.XPATH, "//input[@id='submitSearch']")
        self.items_results = (By.XPATH, "//div[@class='ms-srch-item-summary']")
        self.text_no_results = (By.XPATH, "//div[@class='ms-textLarge ms-srch-result-noResultsTitle']")

    def search(self, term):
        # Click search icon
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.icon_search)
        ).click()

        # Type the dynamic search term after clearing the text field
        input_box = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(self.input_search)
        )
        input_box.clear()
        input_box.send_keys(term)
      
        # Click submit button
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.button_submit)
        ).click()
        logging.info("Searching . .")

    def assert_results(self, term):
        # Verify that each result contains at least one word from the search term (ignoring letters-case)
        elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.items_results)
        )
        logging.info("Verifying results . .")

        for el in elements:
            result_text = el.text.lower().strip()
            if not any(word in result_text for word in term.lower().split()):
                assert False, f"No matching word found in result: '{result_text}'"
        
        logging.info("All search results matched the search term")

    def assert_no_results_message(self):
        # Verify the dispalyed message when there are no results
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.text_no_results)
        )
        actual_text = element.text.strip()
        expected_message = "Nothing here matches your search"
        assert expected_message in actual_text, f"Expected '{expected_message}' in '{actual_text}'"
        logging.info("No results found and message is disapyed succesuly")
