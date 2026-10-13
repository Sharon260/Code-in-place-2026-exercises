#Print 10 random numbers in the range 1 to 100. When you're done, click on the "Check Correct" button.
import random

N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

def main():
    for i in range (N_NUMBERS):
        random_num= random.randint( MIN_VALUE, MAX_VALUE)
        print (random_num)

if __name__ == '__main__':
    main()