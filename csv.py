class csv(object):
    def __init__(self,filename):
        self.filename = filename

    def get_types(self):
        """
        This method gets the types of columns in the CSV 

        It returns a list of the types in the order of the columns 

        This method assumes that there are only String and Numeric types in the file
        """
        
