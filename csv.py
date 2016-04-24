
class csv(object):

    def __init__(self,filename):
        self.filename = filename
        self.result_csv = []
        self.type_list = []
        self.parse_csv(filename)


    def parse_csv(self,filename):

        csv_file = open(filename)

        closed_quotes = True
        for line in csv_file:
            # strip the right side 
            line = line.rstrip()
            #split the lines by comma 
            line_list = line.split(",")
            print line_list
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
        print closed_quotes

        print self.result_csv

    def combine_double_quotes(self,line_list, closed_quotes, quote_stack):
        new_list = []
        for i in xrange(len(line_list)):
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
        This function gets the value at a specified row and column of the csv

        Since the csv is stored as a list of lists, the lookup time for this value 
        is O(1) as lists have constant lookup time at a specified index
        """
        return self.result_csv[row][col]


    def get_types(self):
        """
        This method gets the types of columns in the CSV 

        It returns a list of the types in the order of the columns 

        This method assumes that there are only String and Numeric types in the file

        Specifically, String and Numeric types are defined as follows:

        String: any value of type str, including empty colums denoted by the placeholder " " 

        Numeric: any value that contains only digits 
        """

        for item in self.result_csv[0]:
            if item.isdigit():
                self.type_list.append("Numeric")
            else:
                self.type_list.append("String")

        return self.type_list

