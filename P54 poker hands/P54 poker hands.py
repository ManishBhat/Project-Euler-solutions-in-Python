# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 07:54:36 2020

@author: manis_apezuzf
"""
def whowon(p1_hand,p2_hand):
    """
    This function uses the rules of poker to evaluate the winner b/w 2 hands.
    
    Args:
        p1_hand: Player 1's hand. It comprises of 5 cards.
        p2_hand: Player 2's hand. It comprises of 5 cards.
    
    Returns:
        1 if P1 wins
        2 if P2 wins
        0 if there is no clear winner(i.e. error as problem specifically states 
        that all matchups have a clear winner)
        
    """
    if royalflush(p1_hand)>royalflush(p2_hand): #Royal flush is the best possible hand so it comes first.
        return 1 # #If P1 has the royal flush, he wins
    elif royalflush(p1_hand)<royalflush(p2_hand):
        return 2 #If P2 has royal flush he wins
    #Note that at this stage, both either have or don't have royal flush.
    #So we will use straightflush as a tiebreaker
    if straightflush(p1_hand)>straightflush(p2_hand):
        return 1
    elif straightflush(p1_hand)<straightflush(p2_hand):
        return 2
    #Both players don't have straight flush or both have same card values on their flushes.
    #We will use fourofakind as a tiebreaker.
    if fourofakind(p1_hand)>fourofakind(p2_hand):
        return 1
    elif fourofakind(p1_hand)<fourofakind(p2_hand):
        return 2
    #And so on... We will progressively use important rules until one gives the winner.
    if fullhouse(p1_hand)>fullhouse(p2_hand):
        return 1
    elif fullhouse(p1_hand)<fullhouse(p2_hand):
        return 2
    if flush(p1_hand)>flush(p2_hand):
        return 1
    elif flush(p1_hand)<flush(p2_hand):
        return 2
    if straight(p1_hand)>straight(p2_hand):
        return 1
    elif straight(p1_hand)<straight(p2_hand):
        return 2
    if threeofakind(p1_hand)>threeofakind(p2_hand):
        return 1
    elif threeofakind(p1_hand)<threeofakind(p2_hand):
        return 2
    if twopairs(p1_hand)>twopairs(p2_hand):
        return 1
    elif twopairs(p1_hand)<twopairs(p2_hand):
        return 2
    if onepair(p1_hand)>onepair(p2_hand):
        return 1    
    elif onepair(p1_hand)<onepair(p2_hand):
        return 2
    if highcard(p1_hand)>highcard(p2_hand):
        return 1    
    elif highcard(p1_hand)<highcard(p2_hand):
        return 2
    #At this stage, no rule could decide with hand was better.
    #This is an error as problem specifically states that all matchups have a clear winner
    #Thus, we will print an error message and return 0.
    else:
        print("ERROR")
        return 0
def highcard(playerhand):
    """
    This function implements the highcard rule.
    i.e. Given a hand (set of 5 cards), the function will return card with the
    largest number
    
    Args:
        playerhand: Player's hand. It comprises of 5 cards.
    
    Returns:
        Number on highest value card. (e.g. returns 13 for 3H 7H 6S KC JS QH TD JC 2D 8S)
        as there is a King(K) that equals value=13.
        
    """    
    return max(playerhand, key=lambda x: x[0])[0]
def onepair(playerhand):
    playerhand.sort(key = lambda x: x[0])
    if playerhand[0][0]==playerhand[1][0]:
        return playerhand[0][0]
    if playerhand[1][0]==playerhand[2][0]:
        return playerhand[1][0]
    if playerhand[2][0]==playerhand[3][0]:
        return playerhand[2][0]
    if playerhand[3][0]==playerhand[4][0]:
        return playerhand[3][0]
    return 0
def twopairs(playerhand):
    playerhand.sort(key = lambda x: x[0])
    if playerhand[0][0]==playerhand[1][0]:
        if playerhand[2][0]==playerhand[3][0]:
            return playerhand[3][0]
        elif playerhand[3][0]==playerhand[4][0]:
            return playerhand[3][0]
    elif playerhand[1][0]==playerhand[2][0]:
        if playerhand[3][0]==playerhand[4][0]:
            return playerhand[3][0]
    return 0
def threeofakind(playerhand):
    playerhand.sort(key = lambda x: x[0])
    if playerhand[0][0]==playerhand[1][0]==playerhand[2][0] or playerhand[1][0]==playerhand[2][0]==playerhand[3][0] \
    or playerhand[2][0]==playerhand[3][0]==playerhand[4][0]:
        return playerhand[2][0]
    return 0

def straight(playerhand):
    playerhand.sort(key = lambda x: x[0])
    if playerhand[0][0]+4==playerhand[1][0]+3==playerhand[2][0]+2 \
    ==playerhand[3][0]+1==playerhand[4][0]:
        return playerhand[4][0]
    return 0
def flush(playerhand):
    if playerhand[0][1]==playerhand[1][1]==playerhand[2][1]==playerhand[3][1]==playerhand[4][1]:
        return True
    return False
def fullhouse(playerhand):
    playerhand.sort(key = lambda x: x[0])
    if playerhand[0][0]==playerhand[1][0] and playerhand[2][0]==playerhand[3][0]==playerhand[4][0]:
        return playerhand[2][0]
    if playerhand[0][0]==playerhand[1][0]==playerhand[2][0] and playerhand[3][0]==playerhand[4][0]:
        return playerhand[0][0]
    return 0 
def fourofakind(playerhand):
    playerhand.sort(key = lambda x: x[0])
    if playerhand[0][0]==playerhand[1][0]==playerhand[2][0]==playerhand[3][0]:
        return playerhand[0][0]
    if playerhand[1][0]==playerhand[2][0]==playerhand[3][0]==playerhand[4][0]:
        return playerhand[1][0]
    return 0
def royalflush(playerhand):
    playerhand.sort(key = lambda x: x[0])
    if playerhand[0][1]==playerhand[1][1]==playerhand[2][1]==playerhand[3][1]==playerhand[4][1]:
        if playerhand[0][0]==10 and playerhand[1][0]==11 and playerhand[2][0]==12 and playerhand[3][0]==13 and playerhand[4][0]==14:
            return True
    return False

def straightflush(playerhand):
    playerhand.sort(key = lambda x: x[0])
    if playerhand[0][1]==playerhand[1][1]==playerhand[2][1]==playerhand[3][1]==playerhand[4][1]:
        if playerhand[0][0]+4==playerhand[1][0]+3==playerhand[2][0]+2 \
            ==playerhand[3][0]+1==playerhand[4][0]:
            return playerhand[4][0]
    return False
def main():
    #Reads text file into a list of lists each list containing 
    #a game(set of 10 cards, comprising of 2 player's hands)
    arr = [x for x in [ y.rstrip().split(' ') for y in
    open('p054_poker.txt').readlines() ] if x and not x == '\n']
    #listofpokergames is defined inorder to write down cards like 'JS' as (11,S).
    #This was convenient as there are rules that involve checking for 
    #consecutive numbers.
    listofpokergames=arr
    for i in range(len(arr)):
        for j in range(10):
            if arr[i][j][0]=="T":
                listofpokergames[i][j]=(10,arr[i][j][1])
            elif arr[i][j][0]=="J":
                listofpokergames[i][j]=(11,arr[i][j][1])
            elif arr[i][j][0]=="Q":
                listofpokergames[i][j]=(12,arr[i][j][1])
            elif arr[i][j][0]=="K":
                listofpokergames[i][j]=(13,arr[i][j][1])
            elif arr[i][j][0]=="A":
                listofpokergames[i][j]=(14,arr[i][j][1])
            else:
                listofpokergames[i][j]=(int(arr[i][j][0]),arr[i][j][1])   
    #The next 5 lines, compute the answer. The remaining 180+ lines are to
    #ensure that these 5 lines work. Whether that makes this code beautiful or an 
    #ugly monstrosity is for you to decide :)
    counter=0
    for pokergame in listofpokergames:
        if whowon(pokergame[0:5],pokergame[5:10])==1:
            counter+=1
    print("The number of hands won by player 1 are: ",counter)
if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print("Program run time(in s): ", (time.time() - start_time))             

 