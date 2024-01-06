from selenium import webdriver
from selenium.webdriver.common.by import By
from AutomaticTestScript import AutomaticTestTemplate
import time

class PrubeznaDoba:

    def __init__(self, input_elements, selector, test_values, input_values):
        self.input_elements = input_elements
        self.selector = selector
        self.test_values = test_values
        self.input_values = input_values
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://localhost:7063/Forms/PrubeznaDoba")

    def prubezna_doba_test(self):
        for i in range(3):
            AutomaticTestTemplate().submit_click(self.driver, By.ID, "pridatPracovisteBtn")
        self.driver.implicitly_wait(3)
        AutomaticTestTemplate().fill_tables(
            self.driver,
            self.test_values,
            3,
            3,
            lambda row, col: self.table_input(row, col)
        )
        AutomaticTestTemplate().fill_inputs(self.driver, self.input_elements, self.input_values)
        AutomaticTestTemplate().submit_click(self.driver, By.ID, "vypocitatPrubeznouDobuBtn")
        time.sleep(6)
        AutomaticTestTemplate().select_options(self.driver, self.selector, "1")
        AutomaticTestTemplate().submit_click(self.driver, By.ID, "vypocitatPrubeznouDobuBtn")
        time.sleep(6)

    def table_input(self, row, col):
        return f"//*[@id='prubeznaDobaVstup']/tbody/tr[{row}]/td[{col}]"

if __name__ == "__main__":
    test_values = [
    [10, 15, 5],
    [5, 10, 5],
    [15, 5, 0]
    ]
    input_elements = ["DavkaQ", "DavkaQd"]
    input_values = ["4", "2"]
    selector = "SystemZpracovani"
    
    PrubeznaDoba(input_elements ,selector, test_values, input_values).prubezna_doba_test()