'''
edit by xy


'''

# -*- coding: utf-8 -*-

def checkio(number):
    num = 0
    old = 0
    add = 0
    while number > 0:
        if number > (old + add):
            number -= (old + add)
            num += add
            old += add
            add += 1
        elif number > old:
            number -= old
            num += number
            break
        else:
            break
    return num


print checkio(2)

# ans1
"""Determine the number of (greedy) pigeons who will be fed."""

import itertools

​

def checkio(food):
    """Given a quantity of food, return the number of pigeons who will eat."""

    pigeons = 0

    for t in itertools.count(1):

        if pigeons + t > food:
            # The food will be consumed this time step.

            # All pigeons around last time were fed, and there is enough food

            # this time step to feed 'food' pigeons, so return the max of each.

            return max(pigeons, food)

        # Increase pigeons, decrease food.

        pigeons += t

        food -= pigeons

​

# 2
def checkio(number):
    total_pigeons = 1

    next_group = 1

    while total_pigeons < number:
        number -= total_pigeons  # nom-nom-nom

        next_group += 1

        total_pigeons += next_group

    return max(total_pigeons - next_group, number)


# 3
def checkio(n):  # explanation follows...

    p = lambda t: t * (t + 1) // 2

    q = lambda t: (t * t * t + 3 * t * t + 2 * t) // 6

    h = 9 * n * n - 1 / 27

    R = 3 * n + h ** (1 / 2)

    T = 3 * n - h ** (1 / 2)

    X1 = R ** (1 / 3) + T ** (1 / 3) - 1

    w = int(X1)

    return p(w) + max(0, n - q(w) - p(w))

​

"""

   p(t): number of of pigeons at round t

   p(1) = 1

   p(n) = p(n-1) + n

​

   p(n) = 1 + 2 + 3 + ... + n = n*(n+1)/2

​

   q(t): number of portions to feed all pigeons in the first t rounds

   

   q(t)

 = \sum_{i=1}^{n} p(i)

 = 1/2 * \sum_{i=1}^{n} n^2 + 1/2 * \sum_{i=1}^{n} n

 = 1/2 * n * (n+1) * (2*n+1) / 6 + 1/2 * n * (n+1) / 2

 = 1/12 * (2*n^3 + 3*n^2 + n) + 1/4 * (n^2 + n)

 = 1/12 * (2*n^3 + 3*n^2 + n + 3*n^2 + 3*n)

 = 1/12 * (2*n^3 + 6*n^2 + 4*n)

 = 1/6 * (n^3 + 3*n^2 + 2*n)

​

Suppose we start with N portions and w full rounds of pidgeons are fed:

​

    q(w) <= N

<=> w^3 + 3*w^2 + 2*w - 6*N <= 0

​

Single real root is calculated by:

​

    a = 1, b = 3, c = 2, d = -6*N

​

    f = (3*c/a - b*b/a/a)/3

    g = (2*b*b*b/a/a/a - 9*b*c/a/a + 27*d/a)/27

    h = g*g/4 + f*f*f/27

    R = -(g/2) + h**(1/2)

    S = R**(1/3)

    T = -(g/2) - h**(1/2)

    U = T**(1/3)

    X1 = S + U - b/3/a

​

theferore:  w = int(X1)

​

We can feed p(w) pidgeons and we are left with N - q(w) portions for round w+1.

But the first p(w) pidgeons in round w+1 have already been fed.

So, if N - q(w) > p(w), we can feed N - q(w) - p(w) more pidgeons.

"""
