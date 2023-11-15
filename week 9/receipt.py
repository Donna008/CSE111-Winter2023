import csv
from datetime import datetime
# KEY_COLUMN_INDEX = 0

def main():
    try:
        filename = "week 9/products.csv"
        key_column_index = 0
        products_dict =read_dictionary(filename,key_column_index)
        print(products_dict)
        current_date_and_time = datetime.now() # print current datetime.
        print('Inkom Emporium\n') # Print the store name here
        with open("week 9/request.csv","rt") as file:
            reader = csv.reader(file)
            next(reader)
            sum = 0
            subtotal = 0
            tax =0.06
            discount = 0.01
            # current_weeked = datetime.now()
            # print(current_weeked.year)
            # print(current_weeked.strftime("%A"))
            total = 0
            for product in reader:
                # print(product)
                key = product[0]
                # print(key)
                name = products_dict[key][1]
                price =float(products_dict[key][2])
                quantity =int(product[1])
                sum = sum + quantity# get the dictionary all items. 
                subtotal = subtotal + price * quantity # get the all items prices
                sales_tax = subtotal * tax  # get the sales tax
                total = subtotal + sales_tax  # get the total amount due
                print(f'{name} {quantity} @ {price}')# delete the key(product).
            print(f'\nNumber of Items: {sum}')
            print(f'Subtotal: {subtotal:.2f}')
            print(f'Sales tax: {sales_tax:.2f}')
            print(f'Total: {total:.2f}')
            print('\nThank you for shopping at the Inkom Emporium.')
            print(f"Today's date is: {current_date_and_time:%c}")

            datetimetime = datetime.now()
            getweek = datetimetime.strftime("%A")
            gethour = float(datetimetime.strftime("%H"))
            # exceeding requirements: 1
            if getweek == 'Tuesday'or getweek == 'Wednesday':
                count_week = total * discount
                print('\nToday is Tuesday or Wednesday.')
                print(f'The final total price of discount: {count_week:.2f}')
            # exceeding 2:
            elif gethour < 11:
                count_hour = total * discount
                print('\nThe time is before 11AM.')
                print(f'The final total price is: {count_hour:.2f}')
            # exceeding 3:
            elif key == 'D083':
                count_pro = 0.75 * discount
                print(f"\nToday's 1 cup yogurt have a coupon of 10%: {count_pro:.2f}")
            # exceeding 4:    
            else:
                # print('\nThere have an online survey 1-3 type a number please!')
                survey = [
                    '\nThere have an online survey 1-3 type a number please!'
                    '\n1.This is a bad shopping experience.'
                    '\n2.This is a good shopping experience.'
                    '\n3.This is a better shopping experience.'
                ]
                # ONE_INDEX = 1
                # TWO_INDEX = 2
                # THREE_INDEX = 3              
                for i in survey: # how to change the word number to decial number?
                    print(i)
                    # on = i[ONE_INDEX]
                    # two = i[TWO_INDEX]
                    # three = i[THREE_INDEX]                  
                number = int(input('please type a number: '))
                if number == 1:
                    print('So sorry for that, We will look at the feedback and improve it.')
                elif number == 2:
                    print('Thank you for your feedback.')
                elif number == 3:
                    print('I am glad you type this number.')
                else:
                    print('Thank you. Have a nice day!')

    except KeyError as key_error:
        print(key_error,'this is key error.')
    except FileNotFoundError as file_error:
        print(file_error,'you type a wrong file name.')
    except PermissionError as perission_error:
        print(perission_error,'this is a perission error.')
    except ZeroDivisionError as zero_error:
        print(zero_error,'')
    except ValueError as value_error:
        print(value_error,'')
    # except IndexError as index_error:
    #     print(index_error,'')

        # exceeding requirements: 1
   
    # for i in len(pro_list):
        #     print(i)
    #     for i in price:
    #         sum += i  # sum the subtotal due.
    #         print(sum)
        
    #     tax = sum / 0.06
    #     print(tax)# print sum of tax
    #     total_amount = sum + tax
    #     print(total_amount)# compute and print the total amount.
    # print('Thank you for shopping at the Inkom Emporium.')
    
def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    pro_dict = { }
    with open(filename,"rt")  as file:
        reader = csv.reader(file)
        next(reader)
        
        for row_list in reader:
            key = row_list[key_column_index]
            # there is a dictionary
            pro_dict[key] = row_list          
    return pro_dict

# If this file is executed like this:
# > python program.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
