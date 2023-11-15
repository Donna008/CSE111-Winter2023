# def main():
#     colors = ['yellow','red','green','yellow','blue']
#     length = len(colors)
#     print(f"Number of elements: {length}")
#     print(colors[2])
#     colors[3] = 'purple'
#     print(colors)

# if __name__ =="__main__":
#     main()

# def main():
    # fabrics = []
    # fabrics.append("velvet")
    # fabrics.append("denim")
    # fabrics.append("gingham")
    # fabrics.insert(0,"chiffon")
    # print(fabrics)

    # if "gingham" in fabrics:
    #     print("gingham is in the list.")
    # else:
    #     print("gingham is NOT in the list.")

    # i = fabrics.index("velvet")
    # fabrics[i] = "taffeta"
    # fabrics.pop()
    # fabrics.remove("denim")
    # n = len(fabrics)
    # print(f"the fabrics list contains {n} elements.")
    # print(fabrics)
#list
    # number = []
    # number.append(1)
    # number.append(2)
    # number.insert(3,20)
    # number.insert(0,1000)
    # print(number)
    # if 2 in number:
    #     print("2 is in the list")
    # else:
    #     print("2 is NOT in the list")

    # B = number.index(2)
    # number[B] = 99999
    # number.pop()
    # number.remove(1000)
    # C = len(number)
    # print(f"the number list contains {C} elements.")
    # print(number)

# for loop
#     colors = ["red","orange","yellow","green","blue"]
#     for color in colors:
#         print(color)
#     for i in range(len(colors)):
#         color = colors[i]
#         print(color)

# #range function
#     for i in range(10):
#         print(i)
#     print()
#     for i in range(5,10):
#         print(i)
#     print()
#     for i in range(1,10,2):
#         print(i)
#     print
#     for i in range(69,100,+3):
#         print(i)
#     print()

# break statement
    # sum = 0
    # for i in range(10):
    #     number = float(input("please enter a number: "))
    #     if number == 0:
    #         break 
    #     sum += number
    # print(f"sum: {sum}")

#while loop
#     list1 = ["red","orange","yellow","green","blue"]
#     list2 = ["red","orange","green","green","blue"]
#     index = compare_lists(list1,list2)
#     if index == -1:
#         print("the contents of list1 and list2 are equal")
#     else:
#         print(f"list1 and list2 differ at index {index}")
# def compare_lists(list1,list2):
#     length1 = len(list1)
#     length2 = len(list2)
#     limit = min(length1,length2)
#     i = 0
#     while i < limit:
#         element1 = list1[i]
#         element2 = list2[i]
#         if element1 != element2:
#             break
#         i += 1
#     if length1 == length2 == i:
#         i = -1
#     return i

# compund list
    # YEAR_PLANTED_INDEX = 0
    # HEIGHT_INDEX = 1
    # GIRTH_AMOUNT_INDEX = 2
    # FRUIT_AMOUNT_INDEX = 3
    # apple_tree_data = [
    #     [2012,2.7,3.6,70.5],
    #     [2012,2.9,3.6,71.5],
    #     [2012,2.3,3.6,77.5],
    #     [2012,2.5,3.9,74.5]
    # ]
    # total_fruit_amount = 0
    # for inner_list in apple_tree_data:
    #     fruit_amount = inner_list[FRUIT_AMOUNT_INDEX]#,inner_list[HEIGHT_INDEX]
    #     print(fruit_amount)
    #     total_fruit_amount += fruit_amount
    # print(f"total fruit amount: {total_fruit_amount}")
#values and reference



# dictionaries
    # students = {
    #      "42-039-4736": "Clint Huish",
    #     "61-315-0160": "Amelia Davis",
    #     "10-450-1203": "Ana Soares",
    #     "75-421-2310": "Abdul Ali",
    #     "07-103-5621": "Amelia Davis"
    # }
    # students["81-298-9238"] = "Sama Patel"
    # students.pop("61-315-0160")
    # length = len(students)
    # print(f"length: {length}")
    # print(students)
    # print()
    # id = input("enter a student ID: ")
    # if id in students:
    #     name = students[id]
    #     print(name)
    # else:
    #     print("no such student")

#compund values
#    students = {
#     "str":[]
#    }

#finding one item
#value = students[id]
    # students = {
    #      student_ID: [given_name, surname, email_address, credits]
    #     "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
    #     "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
    #     "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
    #     "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
    #     "07-103-5621": ["Amelia", "Davis" "dav19008@byui.edu", 0]
    # }
    # GIVEN_NAME_INDEX = 0
    # SURNAME_INDEX = 1
    # EMAIL_INDEX = 2
    # CREDITS_INDEX = 3
    # id = input("enter a student ID: ")
    # if id in students:
    #     value = students[id]
    #     given_name = value[GIVEN_NAME_INDEX]
    #     surname = value[SURNAME_INDEX]
    #     print(f"{given_name} {surname}")
    # else:
    #     print("no such student")

# PROCESSING ALL ITEMS
    # students = {
    # #      #student_ID" : [given_name, surname, email_address, credits]
    #     "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
    #     "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
    #     "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
    #     "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
    #     "07-103-5621": ["Amelia", "Davis" "dav19008@byui.edu", 0],
    #     "81-298-9238": ["sama","patel","pat21004@byui.edu",8]
    # }
    # students = {
    #     "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
    #     "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
    #     "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
    #     "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
    #     "07-103-5621": ["Amelia", "Davis", "dav19008@byui.edu", 0],
    #     "81-298-9238": ["Sama", "Patel", "pat21004@byui.edu", 8]
    # }
    # GIVEN_NAME_INDEX = 0
    # SURNAME_INDEX = 1
    # EMAIL_INDEX = 2
    # CREDITS_INDEX = 3

    # total = ""

    # # For each item in the list add the number
    # # of credits that the student has earned.
    # for key,value in students.items():
    #     # key = item[0]
    #     # value = item[1]

    #     # Retrieve the number of credits from the value list.
    #     credits = value[EMAIL_INDEX]
    #     total = credits
    #     # Add the number of credits to the total.
    #     #total += credits
    #     print(total)
    #     i = " " #HOW TO PRINT ENTER LIST IN THE DICTIONARY? 
    #     for i in len(students):
    #         i[EMAIL_INDEX]
    #         print(i)
  
    # GIVEN_NAME_INDEX = 0
    # SURNAME_INDEX = 1
    # EMAIL_INDEX = 2
    # CREDITS_INDEX = 3
#     GIVEN_NAME_INDEX = 0
#     SURNAME_INDEX = 1
#     EMAIL_INDEX = 2
#     CREDITS_INDEX = 3
#     total = 0
#     # for item  in students.items():
#     #     key =  item[0]
#     #     value = item[1]
#     for item in students.items():
#         key = item[0]
#         value = item[1]
#         credits = value[CREDITS_INDEX]
#         #credits = value[CREDITS_INDEX]
#         total += credits
#     print(f"total credits earned by all students: {total}")
#     # Example 6

# #def main():
#     #Create a dictionary with student IDs as the keys
#     #and student data stored in a list as the values.
#     students = {
#         "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
#         "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
#         "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
#         "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
#         "07-103-5621": ["Amelia", "Davis", "dav19008@byui.edu", 0],
#         "81-298-9238": ["Sama", "Patel", "pat21004@byui.edu", 8]
#     }

#     # These are the indexes of the elements in the value lists.
#     GIVEN_NAME_INDEX = 0
#     SURNAME_INDEX = 1
#     EMAIL_INDEX = 2
#     CREDITS_INDEX = 3

#     total = 0

#     # For each item in the list add the number
#     # of credits that the student has earned.
#     for key, value in students.items():

#         # Retrieve the number of credits from the value list.
#         credits = value[CREDITS_INDEX]

#         # Add the number of credits to the total.
#         total += credits

#     print(f"Total credits earned by all students: {total}")


# converting betwwen lists and dictionary
#     numbers = ["42","43","23","45","64"]
#     names = ["a","a","c","d","e"]
#     student_dict = dict(zip(names,numbers))
#     print("dictionary:", student_dict)
#     print()

# #convert the student dictionary into two lists named keys and values
#     keys = list(student_dict.keys())
#     values = list(student_dict.values())
#     print("keys:" , keys)
#     print()
#     print("values:", values)
    
str='123456789'
print(str)
print(str[0:-1])
print(0)
print(str[2:5])
print(str[1:5:2])
print(str * 2)


# if __name__ == "__main__":
    # main()
