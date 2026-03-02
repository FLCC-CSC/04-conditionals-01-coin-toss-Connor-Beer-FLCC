# FILE NAME - coin_toss.py
# NAME: Connor Beer
# DATE: March 1, 2026
# BRIEF DESCRIPTION: Flips a coin based on a random number 

import random

########## ENTER YER CODE BELOW THIS LINE ##########

def main():
    coin_toss()

def coin_toss():
    print('===== Coin Flipper =====')

    random_number = random.randint(1, 100)

    if random_number >=51:
        print('Tails')
    else:
        print('Heads')

main()

########### END YER CODE ABOVE THIS LINE ###########

########################################
#          REFLECTION QUESTIONS
########################################

'''
1. What was the hardest part of completing this lab? 
accidentally using random.randrange instead of random.randint
'''

########################################
#            ATTESTATION
########################################

'''
It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 

[ ] I understand very little about this lab.
[ ] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[X] I pretty much get it.
[ ] I'm solid. Totally got it.
'''