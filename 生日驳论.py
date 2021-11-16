
import random as r
p = 1 
def birth(n):
    ls = []
    for i in range(n):
        a = r.randint(1,366)
        ls.append(a) 
    if len(ls) != len(set(ls)): 
        global p
        for i in range(n):
            p = p*(366-i)
    else:
        print("There is no same birth")
    return 1-p/366**n 
birth(90)
