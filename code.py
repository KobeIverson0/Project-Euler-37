#!/usr/bin/python
# coding:utf-8

from math import sqrt

def is_Prime(n):
    if n == 1 or n == 0:
        return False
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

num = 0
res = []
n = 23

while num < 11:
    a = str(n)
    b = a
    judge = True
    while judge:
        judge = False
        if a != '' and is_Prime(int(a)) and is_Prime(int(b)):
            a = a[: -1]
            b = b[1: ]
            judge = True
    if a == '':
        res.append(n)
        n += 1
        num += 1
    else:
        n += 1

print res
