import unittest 
from csv import CSV

class CSVUnitTests(unittest.TestCase):
    def test_create_instance(self):
        """
        Tests the basic functionality: that the CSV init function 
        creates an instance of the CSV class.
        """

        new_csv = CSV("example.csv")
        self.assertIsInstance(new_csv,CSV)

    def test_empty_instance(self):
        """
        Tests that the CSV init function creates an 
        instance of the CSV class when given an empty file, empty.csv.

        For the purposes of this class, we assume that an empty CSV is still a valid
        CSV; since the parse_csv function allows us to access individual rows and 
        columns, we can add methods to add values to specific rows and columns later 
        if desired.
        """
        new_csv = CSV("empty.csv")
        self.assertIsInstance(new_csv,CSV)

    def test_parse_csv_normal_input(self):
        """
        Tests parse_csv on an input file containing only strings, commas, and 
        integer numerics
        """
        new_csv = CSV("example.csv")
        self.assertEqual(new_csv.result_csv, [['John D', '120 any st.', '"Anytown  WW"', '08123'], ['Andrew P', '114 Sansome st.', '"San Francisco  CA"', '94105'], ['Morgan R', '905 Green st.', '"Chicago  IL"', '68100']])

    def test_parse_csv_empty_input(self):
        """Tests parse_csv on an empty file"""

        new_csv = CSV("empty.csv")
        self.assertEqual(new_csv.result_csv, [])

    def test_parse_csv_empty_cells(self):
        """
        Tests parse_csv on an input file containing strings, numerics, and empty 
        cells denoted by spaces between commas 

        For example:
        Andrew P,,94105
        """
        new_csv = CSV("empty_cells.csv")
        self.assertEqual(new_csv.result_csv, [['John D', '', '08123'], ['Andrew P', '', '94105'], ['Morgan R', '', '68100']])

    def test_get_types_normal_input(self):
        """
        Tests get_type on an input file containing only strings, commas, and 
        integer numerics
        """
        new_csv = CSV("example.csv")
        types = new_csv.get_types()
        self.assertEqual(new_csv.type_list, ['String', 'String', 'String', 'Numeric'])

    def test_get_types_empty_input(self):
        """Tests get_types on an empty file"""

        new_csv = CSV("empty.csv")
        types = new_csv.get_types()
        self.assertEqual(new_csv.type_list, ['String'])

    def test_get_types_negative_input(self):
        """Tests get_types on an input file containing negative numbers"""

        new_csv = CSV("negative_numbers.csv")
        types = new_csv.get_types()
        self.assertEqual(new_csv.type_list, ['String', 'Numeric', 'Numeric'])

    def test_get_types_decimal_input(self):
        """Tests get_types on an input file containing negative numbers"""
        new_csv = CSV("float_numbers.csv")
        types = new_csv.get_types()
        self.assertEqual(new_csv.type_list, ['String', 'Numeric', 'Numeric'])

    def test_get_types_empty_cells(self):
        """Tests get_types on an input file containing empty cells"""

        new_csv = CSV("empty_cells.csv")
        types = new_csv.get_types()
        self.assertEqual(new_csv.type_list, ['String', 'String', 'Numeric'])

    def test_combine_double_quotes(self):
        """
        Tests combine_double_quotes on an input file that contains quotes spread 
        across lines
        """
        new_csv = CSV("example2.csv")
        self.assertEqual(new_csv.result_csv, [['"For whom the bells toll"', '0', '0'], ['"Bring me some shrubbery"', '2', '3'], ['"Once upon a time"', '5', '6'], ['"\'It\'s just a flesh wound."', '8', '9']])

    def test_get_cell_value_normal_input(self):
        """Tests the ability to look up a value at a specified row and column"""
        new_csv = CSV("example.csv")
        value_at_index = new_csv.get_cell_value(1,2)
        self.assertEqual(value_at_index, '"San Francisco  CA"')

    def test_get_cell_value_empty_cell(self):
        """
        Tests the ability to look up a value at a specified row and column
        when the cell is empty
        """
        new_csv = CSV("empty_cells.csv")
        value_at_index = new_csv.get_cell_value(1,1)
        self.assertEqual(value_at_index, '')

if __name__ == "__main__":
    unittest.main()