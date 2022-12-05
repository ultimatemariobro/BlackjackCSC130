# author: Coleman Pilkington
# Supported by: Mario and Zineb
# CSC 130 final group Project
# 29 NOV 2022

# NOTICE: calling dealCards function invokes function to re-iterate. this causes issues with persistence of hand!

from listStack import ListStack
import random


def main():
    cardDeck = ListStack(
        [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8,
         9, 10, 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A'])

    endGame = 0
    while endGame < 1:
        print("game started")
        shufflesRemain = random.randint(5, 120)
        while shufflesRemain > 0:
            shuffle(cardDeck)
            shufflesRemain -= 1
        dealCards(cardDeck)                         # Function to deal cards to both user and dealer
        print(f'Dealer {dealCards(cardDeck)[1]}')            
        userDraw(cardDeck, dealCards(cardDeck)[0])
        endGame += int(gameEnder())


def gameEnder():
    """asks user to play again. validates entry. returns 1 to end game; returns 0 to NOT end game"""
    validAnswer = 0
    returnValue = 0
    while validAnswer < 1:
        answer = input("Play again? Y or N  ")
        answer = answer.upper()
        if answer != "Y" and answer != "N":
            print("invalid answer")
        elif answer.upper == 'Y':
            validAnswer = 1
            returnValue = 0
        elif answer.upper() == 'N':
            validAnswer = 1
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


def dealCards(cardDeck):
    """add doc about returns userHand, dealerHand"""
    userHand = ListStack()
    dealerHand = ListStack()        
    # add shuffle function here maybe for both players hands
    userHand.push(cardDeck.pop())           # card gets pushed to the top of the stack and removes it from the list 
    dealerHand.push(cardDeck.pop())
    userHand.push(cardDeck.pop())
    dealerHand.push(cardDeck.pop())

    if len(userHand) == 2:  # if the player has 2 cards
        if userHand[0] == 11 and userHand[1] == 11:  # both cards are ace
            userHand[0] = 1  # 1st card counts as 1
            userHand -= 10  # update user hand total by subtracting 10
    #
    if len(dealerHand) == 2:
        if dealerHand[0] == 11 and dealerHand[1] == 11:
            dealerHand[1] = 1  # 2nd card ace overrated to 1
            dealerHand -= 10

    return userHand, dealerHand

def userDraw(cardDeck, userHand):
    while countHand(userHand) < 21:  # while hand value under 21
        print(f'current hand: {userHand}')
        print(f'Current hand value: {countHand(userHand)}')
        decision = input('Do you want to draw another card?: (YES/NO) ')
        if decision.upper() == 'YES':  # if user wants another card
            userHand.push(cardDeck.pop())  # add card from cardDeck to userHand
        else:
            break
    if countHand(userHand) > 21:  # REPLACE LATER
        print(f"BUSTED!     current hand: {userHand}       hand value: {countHand(userHand)}")
    elif countHand(userHand) == 21:
        print('BLACKJACK!')
    else:
        print(countHand(userHand))


def dealerDraw(cardDeck, dealerHand):
    while countHand(dealerHand) < 21:  # while hand value under 21
        print(f'current hand: {dealerHand}')
        print(f'Current hand value: {countHand(dealerHand)}')
        decision = input('Do you want to draw another card?: (YES/NO) ')
        if decision.upper() == 'YES':  # if user wants another card
            dealerHand.push(cardDeck.pop())  # add card from cardDeck to userHand
        else:
            break
    if countHand(dealerHand) > 21:  # REPLACE LATER
        print(f"BUSTED!     current hand: {dealerHand}       hand value: {countHand(dealerHand)}")
    elif countHand(dealerHand) == 21:
        print('BLACKJACK!')
    else:
        print(countHand(dealerHand))

def revealDealerCards(userHand, dealerHand):
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]


if __name__ == __name__:
    main()
