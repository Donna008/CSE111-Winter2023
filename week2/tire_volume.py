import math
from datetime import datetime


width = int(input("Enter the tire of width: "  ))
aspect = int(input("Enter aspect of the wheel: "  ))
diameter = int(input("Enter diameter: "  ))
volume = math.pi * width **2 * aspect * (width * aspect + 2540 * diameter) / 10_000_000_000
print(f"The approximate volume is {volume:.2f} liters")
print(f"Width is: {width}, Aspect Ratio is: {aspect}, The Diameter is: {diameter} ")
print("Thank you for contacting us. Have a good day!")
current_date_and_time = datetime.now()
with open("week2/volumes.txt", "at") as use_file:
    print(f"Width is: {width}, Aspect Ratio is: {aspect}, The Diameter is: {diameter} ", file=use_file)
    print(f"Today's date is: {current_date_and_time:%Y-%m-%d}",f"{volume:.2f}",file=use_file )
    print("Thank you for contacting us. Have a good day!", file=use_file)
    print(f"{current_date_and_time:%Y-%m-%d}")
   
prices_1 = 129
prices_2 = 140
prices_3 = 160
prices_4 = 200

if volume == 10:
    print("This size price is:" + str(prices_1))
    if volume == 25:
        print("This size price is:" + str(prices_4))
        if volume == 39:
            print("This size price is:" + str(prices_3))
elif volume == 70:
     print("This size price is:" +str(prices_2))
elif volume == 100:
    print("Sorry, we have not this size prices!")
else:
    print("Thank you!")

answer = str(input("Do you want to buy tires?(Y/N): "))
if answer.title() == "Yes":
    phone_number =int(input("Please enter your phone number:"))
    print("Thank you for contacting us. Have a good day!")
    with open("week2/volumes.txt", "at") as use_file:
        print(f"Custumers phone number is:{phone_number}", file=use_file)    
else:
    print("Thank you")








