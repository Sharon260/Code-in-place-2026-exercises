#Write a program that loops over a dictionary of words and quizzes the user for their corresponding Spanish translations, keeping count of how many the user gets correct! Separate each question and answer with a blank line to help with visual clarity.

def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    
    # Ask the translation of the word 
    #allow user to answer
    #save the aswer
    #make a loop to continue asking questions
    #print the number of correct answers
    
    
    
    correct=0
    for english, spanish in translations.items ():
        answer = input (f"What is the Spanish translation for {english}? ")
        if answer == spanish:
            print ("That is correct!")
            correct += 1
        else:
            print (f"That is incorrect, the Spanish translation for {english} is {spanish}.")
    
        print ()
    print (f"You got {correct}/{len(translations)} words correct, come study again soon!")

    


if __name__ == '__main__':
    main()