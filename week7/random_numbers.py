import random
def main():
    numbers = [16.2, 75.1, 52.3]
    print(f"numbers {numbers}")
    add_numbers = append_random_numbers
    print(add_numbers)
    #how to add three numbers to numbers
    list = [1,2,3]
    new_add_number = (append_random_numbers, list)
    print(new_add_number)



def append_random_numbers(numbers_list,quantity=1):
    #quantity = 1
    for _ in range(quantity):
        random_number = random.uniform(0,100)
        rounded = round(random_number,1)
        numbers_list.append(rounded)
def append_random_words(words_list, quantity=1):
    candidates = ["join","love","smile","love","cloud","head"]
    for _ in range(quantity):
        word = random.choice(candidates)
        words_list.append(word)
if __name__ == "__main__":
        main()



