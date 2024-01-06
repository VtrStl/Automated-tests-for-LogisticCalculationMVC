from selenium import webdriver
from selenium.webdriver.common.by import By
from AutomaticTestScript import AutomaticTestTemplate
import time

class Qopt:

    def __init__(self, input_elements, test_values):
        self.input_elements = input_elements
        self.test_values = test_values
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://localhost:7063/Forms/Qopt")

    def qopt_test(self):
        for i in range(len(self.test_values)):
            AutomaticTestTemplate().fill_inputs(self.driver, self.input_elements, self.test_values[i])
            AutomaticTestTemplate().submit_click(self.driver, By.CLASS_NAME, "btn-primary")
            time.sleep(6)
        self.driver.quit()
    
if __name__ == "__main__":
    elements = ["VelikostPoptavky", "Npz", "Ns", "Nj", "Obdobi"]
    first_test_values = ["10000", "5000", "400", "1", "0.25"]
    second_test_values = ["4000", "1200", "0.2", "300", "1"]
    test_values = [first_test_values, second_test_values]

    Qopt(elements, test_values).qopt_test()