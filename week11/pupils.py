import csv

def main():
    try:
    
        
        print('Ordered from Oldest to Youngest')
        student_list = read_compound_list('pupils.csv')
        extract_birthdate = lambda student: student[BIRTHDATE_INDEX]
        sorted_list = sorted(student_list, key=extract_birthdate)
        # get a new list.
        extract_given_name = lambda student: student[GIVEN_NAME_INDEX]
        sorted_list1 = sorted(student_list,key=extract_given_name)
        
        ignor_year = lambda student:student[BIRTHDATE_INDEX]
        extract_birth = student_list[5:]
        sorted_list2 = sorted(student_list,key=extract_birth)
        print('Ordered from Oldest to Youngest')
        print(sorted_list)
        print('Ordered by Given name')
        print_list(sorted_list1)
        print('Ordered by birth month and day')
        print(sorted_list2)
        #can crete a many functions. and there have a other function in there.
        


    except (IndentationError,FileNotFoundError) as error:
        print(error,' ')
# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2


def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
   
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list

def print_list(compound_list):
    for number in compound_list:
       print(number)
    print()# why there do not use return?
if __name__=='__main__':    
    main()