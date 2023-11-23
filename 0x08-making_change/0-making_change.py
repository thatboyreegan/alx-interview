#!/usr/bin/python3
"""Change comes from within """

def makeChange(coins, total):
    """
    determines the fewest number of 
    coins needed to meet a given amount total 
    given a pile of coins of different values
    """
    if total <= 0:
        return 0
    
    rem = total
    coinCount = 0
    coinIndex = 0
    sortedCoins = sorted(coins, reverse=True)
    i = len(coins)
    
    while rem > 0:
        if coinIndex >= i:
            return -1
        if rem - sortedCoins[coinIndex] >= 0:
            rem -= sortedCoins[coinIndex]
            coinCount += 1
        else:
            coinIndex += 1
    return coinCount
