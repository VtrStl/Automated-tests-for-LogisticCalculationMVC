from selenium import webdriver
from selenium.webdriver.common.by import By
from AutomaticTestScript import AutomaticTestTemplate
import time

class AnalyZasob:
    
    def __init__(self, input_elements, selector, test_values):
        self.input_elements = input_elements
        self.selector = selector
        self.test_values = test_values
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://localhost:7063/Forms/AnalyzaZasob")

    def analyza_zasob_test(self):
        for i in range(len(self.test_values)):
            AutomaticTestTemplate().fill_inputs(self.driver, self.input_elements, self.test_values[i])
            AutomaticTestTemplate().select_options(self.driver, self.selector, "BQ")
            AutomaticTestTemplate().submit_click(self.driver, By.CLASS_NAME, "btn-primary")
            time.sleep(6)
            AutomaticTestTemplate().select_options(self.driver, self.selector, "sQ")
            AutomaticTestTemplate().submit_click(self.driver, By.CLASS_NAME, "btn-primary")
            time.sleep(6)
        self.driver.quit()

if __name__ == "__main__":
    input_elements = ["Spotreba", "ObjednavaciDavka", "PojistnaZasoba", "PokrytiPoptavky", "DodaciLhuta", "DnyNaTyden", "IntervalKontroly"]
    first_test_values = ["3000", "500", "100", "0", "2", "50", "4"]
    second_test_values = ["1200", "800", "0", "3", "4", "50", "6"]
    test_values = [first_test_values, second_test_values]
    selector = "Systemy"

    AnalyZasob(input_elements, selector, test_values).analyza_zasob_test()