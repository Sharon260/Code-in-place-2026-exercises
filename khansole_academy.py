#Implement Khansole Academy—a program that helps other people learn addition! Write a program that randomly generates a simple addition problem for the user, reads in the answer from the user, and then checks to see if they got it right or wrong.


#More specifically, your program should be able to generate simple addition problems that involve adding two 2-digit integers (i.e., the numbers 10 through 99). The user should be asked for an answer to the generated problem. Your program should determine if the answer was correct or not, and give the user an appropriate message to let them know.

import random

def main():
    print("Khansole Academy")
    rand_num_1= random.randint (10, 99)
    rand_num_2= random.randint(10,99)
    print (f"What is {rand_num_1} + {rand_num_2}?")
    Answer_str= input ("Your answer: ")
    answer= int(Answer_str)
    total = rand_num_1 + rand_num_2
    if answer == total:
        print("Correct!")
    else:
        print ("Incorrect.")
        print (f"The expected answer is {total}")
    
    
if __name__ == '__main__':
    main()