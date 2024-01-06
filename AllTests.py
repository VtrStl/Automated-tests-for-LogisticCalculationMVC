import QoptTest
import AnalyzaZasobTest
import PrubeznaDobaTest

class AllTests:

    def qopt_test():
        elements = ["VelikostPoptavky", "Npz", "Ns", "Nj", "Obdobi"]
        first_test_values = ["10000", "5000", "400", "1", "0.25"]
        second_test_values = ["4000", "1200", "0.2", "300", "1"]
        test_values = [first_test_values, second_test_values]
        QoptTest.Qopt(elements, test_values).qopt_test()
    
    def analyza_zasob_test():
        input_elements = ["Spotreba", "ObjednavaciDavka", "PojistnaZasoba", "PokrytiPoptavky", "DodaciLhuta", "DnyNaTyden", "IntervalKontroly"]
        first_test_values = ["3000", "500", "100", "0", "2", "50", "4"]
        second_test_values = ["1200", "800", "0", "3", "4", "50", "6"]
        test_values = [first_test_values, second_test_values]
        selector = "Systemy"
        AnalyzaZasobTest.AnalyZasob(input_elements, selector, test_values).analyza_zasob_test()

    def prubezna_doba_test():
        input_elements = ["DavkaQ", "DavkaQd"]
        test_values = [
        [10, 15, 5],
        [5, 10, 5],
        [15, 5, 0]
        ]
        input_values = ["4", "2"]
        selector = "SystemZpracovani"
        PrubeznaDobaTest.PrubeznaDoba(input_elements ,selector, test_values, input_values).prubezna_doba_test()
    
    def run_all_tests():
        AllTests.qopt_test()
        AllTests.analyza_zasob_test()
        AllTests.prubezna_doba_test()

if __name__ == "__main__":
    AllTests.run_all_tests()