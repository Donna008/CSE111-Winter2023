def main():
    print("This program is an implementation of the Rosenberg Self-Esteem Scale. This program will show you ten statements that you could possibly apply to yourself. Please rate how much you agree with each of the statements by responding with one of these four letters:")

    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.")
    
 
    # print("I feel that I am a person of worth, at least on an equal plane with others."))
    # number1= (input("Enter D, d, a, or A:"))
  
    # print("I feel that I have a number of good qualities.")
    # number2=(input("Enter D, d, a, or A:"))
    
    # print("All in all, I am inclined to feel that I am a failure."))
    # number3=(input("Enter D, d, a, or A:"))
   
    # print("I am able to do things as well as most other people."))
    # number4=(input("Enter D, d, a, or A:"))
    
    # print("I feel I do not have much to be proud of.")
    # number5=(input("Enter D, d, a, or A:"))
   
    # print("I take a positive attitude toward myself.")
    # number6=(input("Enter D, d, a, or A:"))
    
    # print("On the whole, I am satisfied with myself.")
    # number7=(input("Enter D, d, a, or A:"))
    
    # print("I wish I could have more respect for myself.")
    # number8=(input("Enter D, d, a, or A:"))
    
    # print("I certainly feel useless at times.")
    # number9=(input("Enter D, d, a, or A:"))
    
    # print("At times I think I am no good at all.")
    # number10=(input("Enter D, d, a, or A:"))
    


    score = 0
    score += ask_positive_question("I feel that I am a person of worth, at least on an equal plane with others.")
    score += ask_positive_question("I feel that I have a number of good qualities.")
    score += ask_negative_question("All in all, I am inclined to feel that I am a failure.")
    score += ask_positive_question("I am able to do things as well as most other people.")
    score += ask_negative_question("I feel I do not have much to be proud of.")
    score += ask_positive_question("I take a positive attitude toward myself.")
    score += ask_positive_question("On the whole, I am satisfied with myself.")
    score += ask_negative_question("I wish I could have more respect for myself.")
    score += ask_negative_question("I certainly feel useless at times.")
    score += ask_negative_question("At times I think I am no good at all.")
    print()
    print(f"Your score is {score}.")
    print("A score below 15 may indicate problematic low self-esteem.")


def ask_positive_question(statement):
    print(statement)
    answer = input("Enter D, d, a, or A:")
    score = 0
    if answer == 'D':
        score = 0
    elif answer =='d':
        score = 1
    elif answer == 'a':
        score = 2
    elif answer == 'A':
        score = 3
    return score


def ask_negative_question(statement):
    print(statement)
    answer = input("Enter D,d,a,or A:")
    score = 0
    if answer == 'D':
        score = 3
    elif answer == 'd':
        score = 2
    elif answer == 'a':
        score = 1
    elif answer == 'A':
        score = 0
    return score

if __name__ == "__main__":
    main()









