import math

items = int(input("Enter the number of items: "))
i_box = int(input("Enter number of items per box: "))

boxes = math.ceil(items / i_box)

print()
print(f"For {items} items, packing {i_box} items in each box, you will need {boxes} boxes.")