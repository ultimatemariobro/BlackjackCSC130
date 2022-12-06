# authors: Coleman, Mario and Zineb
# CSC 130 final group Project
# 29 NOV 2022

# NOTICE: calling dealCards function invokes function to re-iterate. this causes issues with persistence of hand!

from listStack import ListStack
import random


def main():
    startingDeck = [2, 3, 4, 5, 6, 7, 8, 9, 10,
                    2, 3, 4, 5, 6, 7, 8, 9, 10,
                    2, 3, 4, 5, 6, 7, 8, 9, 10,
                    2, 3, 4, 5, 6, 7, 8, 9, 10,
                    'J', 'Q', 'K', 'A',
                    'J', 'Q', 'K', 'A',
                    'J', 'Q', 'K', 'A',
                    'J', 'Q', 'K', 'A']
    cardDeck = ListStack(startingDeck)

    endGame = 0
    while endGame < 1:
        userHand = []
        dealerHand = []  # the hand of the player is an empty list to be filled and get extracted from
        print("\n\t\tWelcome to Blackjack!\n")

        shufflesRemain = random.randint(5, 120)
        while shufflesRemain > 0:
            shuffle(cardDeck)
            shufflesRemain -= 1

        dealCards(cardDeck, userHand, dealerHand)  # Function to deal cards to both user and dealer
        print(f'Dealer hand: [{dealerHand[0]}, ?]')
        userValue = userDraw(cardDeck, userHand)  # ask the user if they want to hit or stand
        if userValue > -1:
            dealerValue = dealerDraw(cardDeck, dealerHand)
            if dealerValue > -1:
                findWinner(userValue, dealerValue)
        endGame = gameEnder()


def dealCards(cardDeck, userHand, dealerHand):
    """add doc about returns userHand, dealerHand"""
    # add shuffle function here maybe for both players hands?????
    userHand.append(cardDeck.pop())  # card gets pushed to the top of the stack and removes it from the list
    dealerHand.append(cardDeck.pop())
    userHand.append(cardDeck.pop())
    dealerHand.append(cardDeck.pop())

    return userHand, dealerHand


def aceOr11(userHand, dealerHand):
    if len(userHand) == 2:  # if the player has 2 cards
        if userHand[0] == 11 and userHand[1] == 11:  # both cards are ace
            userHand[0] = 1  # 1st card counts as 1
            userHand -= 10  # update user hand total by subtracting 10
    #
    if len(dealerHand) == 2:
        if dealerHand[0] == 11 and dealerHand[1] == 11:
            dealerHand[1] = 1  # 2nd card ace overrated to 1
            dealerHand -= 10
            
    # if handvalue > 21
        # ace in hand
        # hand value -= 1
    return userHand, dealerHand


def gameEnder():
    """asks user to play again. validates entry. returns 1 to end game; returns 0 to NOT end game"""
    validAnswer = 0
    returnValue = 0
    while validAnswer < 1:
        answer = input("Play again?(Y or N): ")
        answer = answer.upper()
        if answer != "Y" and answer != "N":
            print("invalid answer")
        elif answer.upper == 'Y':
            validAnswer = 1     # Not used???
            returnValue = 1
        elif answer.upper() == 'N':
            print("Thank you for playing! Come again.")
            validAnswer = 1     # Not used???
            returnValue = 1
        return returnValue


def countHand(hand):
    """counts card value of hand. returns calculated value INT
    arguments: listStack hand of cards (1-9, a, j, q, k)"""
    score = 0
    face = ['J', 'Q', 'K']
    ace = 0  # ignore for now
    for card in hand:
        if card in range(11):
            score += card
        elif card in face:
            score += 10
        else:
            score += 11
        # add ace implementation here :-)
    return int(score)


def shuffle(cardDeck):
    """shuffles cards in cardDeck. Arguments: CardDeck. returns: NOTHING (function invokes shuffle on live card deck)"""
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []

    try:
        while not cardDeck.isEmpty():  # distributes cards from cardDeck randomly into 6 groups
            starter = random.randint(1, 6)
            if starter == 1:
                list1.append(cardDeck.pop())
            elif starter == 2:
                list2.append(cardDeck.pop())
            elif starter == 3:
                list3.append(cardDeck.pop())
            elif starter == 4:
                list4.append(cardDeck.pop())
            elif starter == 5:
                list5.append(cardDeck.pop())
            else:
                list6.append(cardDeck.pop())
    except:
        pass

    while len(list1) > 0 or len(list2) > 0 or len(list3) > 0 or len(list4) > 0 or len(list5) > 0 or len(
            list6) > 0:
        starter = random.randint(1, 6)
        if starter == 1:
            if len(list1) != 0:
                cardDeck.push(list1.pop())
        elif starter == 2:
            if len(list2) != 0:
                cardDeck.push(list2.pop())
        elif starter == 3:
            if len(list3) != 0:
                cardDeck.push(list3.pop())
        elif starter == 4:
            if len(list4) != 0:
                cardDeck.push(list4.pop())
        elif starter == 5:
            if len(list5) != 0:
                cardDeck.push(list5.pop())
        else:
            if len(list6) != 0:
                cardDeck.push(list6.pop())


def userDraw(cardDeck, userHand):
    """ user draws cards until bust or stand.
    RETURNS: -1 for bust, hand value for stand."""
    while countHand(userHand) < 21:  # while hand value under 21
        print(f'Player hand: {userHand}')
        print(f'Current hand value: {countHand(userHand)}')
        decision = input("Do you want to hit or stand? (H/S): ")
        if decision.upper() == "H":  # if user wants another card
            userHand.append(cardDeck.pop())  # add card from cardDeck to userHand
            print("Player hits ")
            print("_______________________________________________")
        elif decision.upper() == "S":
            print("Player stands")
            print("_______________________________________________")
            break
        else:
            print("Bug here!")

    if countHand(userHand) > 21:  # REPLACE LATER
        print("Busted!")
        print(f"Current hand: {userHand}")
        print(f"Final hand value: {countHand(userHand)}")


        return -1
    else:
        return countHand(userHand)


def dealerDraw(cardDeck, dealerHand):  # NOT COMPLETE
    """dealer draws cards until 17 or greater.
    returns: -1 if dealer bust, otherwise returns hand value."""
    print(f'Dealer hand: {dealerHand}')
    while countHand(dealerHand) <= 17:  # while hand value under 21
        print('Dealer draws a card...')
        dealerHand.append(cardDeck.pop())
        print(f'Dealer hand: {dealerHand}')
        print(f'Current hand value: {countHand(dealerHand)}')

    if countHand(dealerHand) > 21:
        print(f"Dealer busted! You win!")
        return -1
    elif countHand(dealerHand) == 21:
        print("BLACKJACK! Dealer wins! Better luck next time chump..")  # might change this line
        return countHand(dealerHand)
    else:
        return countHand(dealerHand)


def findWinner(userValue, dealerValue):
    print("Final score values:")
    if userValue > dealerValue:
        print(F'Player: {userValue}, Dealer: {dealerValue}')
        print("USER WINS!")
    elif userValue < dealerValue:
        print(F'Player: {userValue}, Dealer: {dealerValue}')
        print("DEALER WINS!")
    elif userValue == dealerValue:
        print(F'Player: {userValue}, dealer: {dealerValue}')
        print("PUSH! it's a tie! Sucks to suck.")

main()
