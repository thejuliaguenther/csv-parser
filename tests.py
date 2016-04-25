import unittest 
from csv import CSV

class CSVUnitTests(unittest.TestCase):
    def test_create_instance(self):
        """
        Tests the basic functionality: that the CSV init function creates an 
        instance of the CSV class
        """
        new_csv = CSV("example.csv")
        self.assertIsInstance(new_csv,CSV)

    def test_empty_instance(self):
        """
        Tests that the CSV init function creates an 
        instance of the CSV class when given an empty file, empty.csv

        For the purposes of this class, we assume that an empty CSV is still a 
        CSV; since the parse_csv function allows us to access individual rows and 
        columns, we can add methods to add values to specific rows and columns later 
        if desired
        """
        new_csv = CSV("empty.csv")
        self.assertIsInstance(new_csv,CSV)

    # def test_invalid_filename(self):
    #     new_csv = CSV("foo.csv")
    #     self.assertNotIsInstance(new_csv, CSV)  

if __name__ == "__main__":
    unittest.main()