#!/usr/bin/python3
""" Prime Game """


def findMultiples(num, targets):
    """ multiples of a given num """
    for i in targets:
        if i % num == 0:
            targets.remove(i)
    return targets


def isPrime(i):
    """ is number a prime? """
    if i == 1:
        return False
    for j in range(2, i):
        if i % j == 0:
            return False
    return True


def findPrimes(n):
    """ find primses """
    counter = 0
    target = list(n)
    for i in range(1, len(target) + 1):
        if isPrime(i):
            counter += 1
            target.remove(i)
            target = findMultiples(i, target)
        else:
            pass
    return counter


def isWinner(x, nums):
    """ is a winner or not ?"""
    players = {'Maria': 0, 'Ben': 0}
    cluster = set()
    for x in range(x):
        nums.sort()
        num = nums[x]
        for i in range(1, num + 1):
            cluster.add(i)
            if i == num + 1:
                break
        temp = findPrimes(cluster)

        if temp % 2 == 0:
            players['Ben'] += 1
        elif temp % 2 != 0:
            players['Maria'] += 1

    if players['Maria'] > players['Ben']:
        return 'Maria'
    elif players['Maria'] < players['Ben']:
        return 'Ben'
    else:
        return None
