import random
import blackjaclogo as bjlogo

ch='y'
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def calculate_score(cards):
    score=sum(cards)
    if 11 in cards and score>21:
        cards.remove(11)
        cards.append(1)
        score=sum(cards)
    return score

print(bjlogo.logo)
while ch=='y':
    ch=input("Do you want to play blackjack??\nType y or n \n")
    if ch=='n':
        print("Thank you for playing")
        break

#Distributing cards
    ucards=random.sample(cards,2)
    dcards=random.sample(cards,2)

#Calculate score  
    usum=calculate_score(ucards)
    dsum=calculate_score(dcards)

#Dealer draws until crossing 17 mark
    while dsum<17:
        dnewcard=random.choice(cards)
        dcards.append(dnewcard)
        dsum=calculate_score(dcards)

    print(f"your cards are {ucards} and your total score is {usum}")
    print(f"Dealer first card is {dcards[0]}")
    ch2=input("Do you want another card?\nType y or n \n")

#Player turn to draw cards
    while ch2=='y':
        newcard=random.choice(cards)
        ucards.append(newcard)
        usum=calculate_score(ucards)
        print(f"Your cards are {ucards} and your total score is {usum}")
        if usum>21:
            ch2='n'
        else:
            ch2=input("Do you want another card?\nType y or n \n")

#calculating results
    while ch2=='n':
        print(f"Dealer's cards are {dcards} and dealer's total score is {dsum}")
        print(f"your cards are {ucards} and your total score is {usum}")

        if usum>21:
            print("Sorry you lost!!")
            break
        elif usum<=21:
            uwincheck=21-usum
            if dsum>21:
                print("Great!!\nYou win!!")
                break
            elif dsum<=21:
                dwincheck=21-dsum
            if uwincheck==dwincheck:
                print("Game Draw")
                break
            elif uwincheck<dwincheck:    
                print("You Win")
                break
            else:
                print("You lose")
                break