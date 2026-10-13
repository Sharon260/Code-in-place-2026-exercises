"Write a program which takes as input the number of sides on a dice.  Then, simulate rolling a dice with that many sides. "
import random

def main():
    Num_sides = input("How many sides does your dice have? ")
    Num_sides= int(Num_sides)
    dice = random.randint(1, Num_sides)
    print ("Your roll is", dice)


if __name__ == '__main__':
    main()