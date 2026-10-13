# Each year for a human is like 7.18 years for a dog
DOG_YEARS_MULTIPLIER = 7.18  

def main():
    Age =input ("Enter an age in calendar years:")
    Age = int (Age)
    converted_years= Age * DOG_YEARS_MULTIPLIER
    print (f"That's {converted_years} in dog years!")


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()