
class CSV(object):
    """
    This file implements a CSV class. This class has the following attributes 
    as set in the init function:

    filename: the name of the CSV to be parsed (as provided by the user)
  
    result_csv: the list designed to keep track of the rows of the CSV (which 
    are themselves lists of colums); the result CSV is implemented as a list of 
    lists as it allows for O(1) access to individual rows and columns when the 
    desired row and column are known (as exists in common spreadsheet programs 
    such as Microsoft Excel)

    type_list: a list of the types of each row and column

    parse_csv: a function that takes in the filename provided by the user and parses
    the CSV into the list of lists format; this is called in the init function to 
    ensure that the CSV is created in the correct format for O(1) lookup time
    """

    def __init__(self,filename):
        self.filename = filename
        self.result_csv = []
        self.type_list = []

        self.parse_csv(filename)


    def parse_csv(self,filename):
        """
        This method parses the CSV into the two-dimensional array format described above.

        It takes in the filename provided by the user and checks that the filename 
        is valid (i.e. located in the same folder) and throws an error if it is not.

        The method then loops through each line in the file, splits the line, and adds it to the result_csv, 
        thus creating an array of arrays.
        """
        try:
            csv_file = open(filename)
        except IOError:
            print "File not found!"
            return
        else:
            closed_quotes = True
            for line in csv_file:
                line = line.strip()
                line_list = line.split(",")
                
                if closed_quotes == True:
                    quote_stack = []
                    combined_line, closed_quotes = self.combine_double_quotes(line_list, closed_quotes, quote_stack)
                    if closed_quotes == True:
                        self.result_csv.append(combined_line)
                    else:
                        to_add = line_list
                else:
                    quote_stack = []
                    to_add.extend(line_list)
                    combined_line, closed_quotes = self.combine_double_quotes(to_add, closed_quotes, quote_stack)
                    if closed_quotes == True:
                        self.result_csv.append(combined_line)
                    else:
                        to_add = line_list
            csv_file.close()
            print self.result_csv


    def combine_double_quotes(self,line_list, closed_quotes, quote_stack):
        """
        This method creates the lists to be added to the two-dimensional array (as stored in 
        the new_list variable); 
        it also considers cases not handled by the basic split function: quotes that begin
        on one line and end on another (as occurs in example2.csv) or quotes that contain commas 
        (as occurs in example.csv).

        This method takes in the line_list, a list of strings representing each line in the original file 
        to be parsed; thus, it preserves the string type of each item in the list.

        To keep track of whether or not all of the quotes are closed, this method takes in closed_quotes, 
        a boolean, and quote_stack, a stack that keeps track of open parentheses. When a new open parenthesis 
        appears, it gets pushed to the quote_stack and popped from the quote_stack when the closing 
        parenthesis is found (note: for the sake of brevity, the quote_stack is represented as a list being used 
        as a stack; a further implementation could implement a stack class, however representing a stack as a list and 
        using it in this way provides the same O(1) time to push and pop from the stack as most implementations would).
        
        It then combines all of the indicies in between quotes using a join function (note: for simplicity, original 
            commas separating the values are not preserved.)

        If the quote stack is not empty, the closed_quotes boolean is set to false.

        The method then returns the new_list (row in the csv) to be added to the result_csv in the parse_csv
        method.
        """
        new_list = []
        for i in xrange(len(line_list)):
            if line_list[i] == "":
                new_list.append(line_list[i])
                continue
            if line_list[i][0] == "\"" and line_list[i][-1] != "\"":
                quote_stack.append(i)
                continue
            if line_list[i][-1] == "\"" and quote_stack != []:
                last_quote = quote_stack.pop()
                new_list.append(" ".join(line_list[last_quote:i+1]))
                closed_quotes = True
            else:
                new_list.append(line_list[i])
        if quote_stack != []:
            closed_quotes = False
        return new_list, closed_quotes

    def get_cell_value(self,row,col):
        """
        This function gets the value at a specified row and column of the csv.

        Since the csv is stored as a list of lists, the lookup time for this value 
        is O(1) as lists have constant lookup time at a specified index.
        """
        return self.result_csv[row][col]


    def get_types(self):
        """
        This method gets the types of columns in the CSV.

        It returns a list of the types in the order that the columns appear.

        This method assumes that there are only String and Numeric types in the file.

        It also assumes that the types of the columns are consistent throughout the file 
        (i.e. if the types of the first row are ["String", "String", "Numeric"], the types in
        each row will follow the pattern ["String", "String", "Numeric"])

        Specifically, String and Numeric types are defined as follows:

        String: any value of type str, including empty colums denoted by the placeholder "" 

        Numeric: any value that contains only digits or digits plus a negative sign (-) in
        the first index or a decimal point 
        """
        if self.type_list == []:
            if self.result_csv == []:
                self.type_list.append("String")
            else:
                for item in self.result_csv[0]:
                    decimal_index = item.find('.')
                    if item.isdigit():
                        self.type_list.append("Numeric")
                    elif item[1:].isdigit() and (item[0] == '-' or item[0] == '.'):
                        self.type_list.append("Numeric")
                    elif decimal_index != -1 :
                        if item[0] == '-' and (item[1:decimal_index].isdigit() and item[decimal_index+1:].isdigit()):
                            self.type_list.append("Numeric")
                        elif item[0:decimal_index].isdigit() and item[decimal_index+1:].isdigit():
                            self.type_list.append("Numeric")
                        else:
                            self.type_list.append("String")
                    else:
                        self.type_list.append("String")
        return self.type_list
    

