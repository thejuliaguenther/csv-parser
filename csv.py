
# def combine_double_quotes(line_list):
#         quote_stack = []

#         for i in xrange(len(line_list)):
#             if line_list[i][0] == "\"":
#                 quote_stack.append(i)
#             if line_list[i][-1] == "\"":
#                 last_quote = quote_stack.pop()
#                 line_list[last_quote] = " ,".join(line_list[last_quote:i+1])
#         return line_list

class csv(object):
    def __init__(self,filename):
        self.filename = filename
        self.result_csv = []
        self.type_list = []

        csv_file = open(filename)

        for line in csv_file:
            # strip the right side 
            line = line.rstrip()
            #split the lines by comma 
            line_list = line.split(",")
            # combined_line = combine_double_quotes(line_list)
            self.result_csv.append(line_list)
        print self.result_csv

    # def combine_double_quotes(line_list):
    #     quote_stack = []

    #     for i in line_list:
    #         if line_list[i][0] == "\"":
    #             quote_stack.append(i)
    #         if line_list[i][-1] == "\"":
    #             last_quote = quote_stack.pop()
    #             line_list[last_quote] = " ".join(line_list[last_quote:i+1])
    #     return line_list

    def get_cell_value(self,row,col):
        """
        This function gets the value at a specified row and column of the csv

        Since the csv is stored as a list of lists, the lookup time for this value 
        is O(1) as lists have constant lookup time at a specified index
        """
        return self.result_csv[row][col]


        # private method to parse the CSV and create a 

    def get_types(self):
        """
        This method gets the types of columns in the CSV 

        It returns a list of the types in the order of the columns 

        This method assumes that there are only String and Numeric types in the file

        Specifically, String and Numeric types are defined as follows:

        String: any value of type str, including empty colums denoted by the placeholder " " 

        Numeric: integers, floats, long integers, and complex numbers 
        """

        for item in self.result_csv[0]:
            if item.isdigit():
                self.type_list.append("Numeric")
            else:
                self.type_list.append("String")

        return self.type_list

