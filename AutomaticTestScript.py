from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AutomaticTestTemplate:

    found_elements = []

    def fill_inputs(self, driver, input_elements, values):
        for i in range(len(input_elements)):
            if (input_elements[i] in self.found_elements):
                driver.find_element(By.NAME, input_elements[i]).clear()
                self.found_elements.remove(input_elements[i])

            driver.find_element(By.NAME, input_elements[i]).send_keys(values[i])
            self.found_elements.append(input_elements[i])

    def fill_tables(self, driver, test_values, rows, cols, xpath_generator):
        for row in range(1, rows + 1):
            for col in range(2, cols + 2):
                xpath_expression = xpath_generator(row, col)
                cell_element = driver.find_element("xpath", xpath_expression)
                cell_element.send_keys(str(test_values[row - 1][col - 2]))
    
    def submit_click(self, driver, by, value):
        driver.find_element(by, value).click()

    def select_options(self, driver, selector, value):
        Select(driver.find_element(By.ID, selector)).select_by_value(value)
        driver.implicitly_wait(2)