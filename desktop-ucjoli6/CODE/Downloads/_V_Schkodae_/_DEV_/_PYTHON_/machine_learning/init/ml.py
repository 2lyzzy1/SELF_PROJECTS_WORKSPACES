"""import math
print(math.fmod)

class Pos() :
    x = 0
    y = 0
    l = ['AZERTYUIOPQSDFGHJKLMWXCVBN','azertyuiopqsdfghjklmwxcvbn', [0,1,2,3,4,5,6,7,8,9]]
    setASCII = set("²&~#{([-|`_\^@=<>,;:!§/.?%¨£$¤*+°])}")
    dictio = {"Name": "Anova", "Age": 17, "Hobbit" : "Gamerz"}
    def init(self, x, y):
        self.x = x
        self.y = y

    def define(self, x, y):
        if (x > 0):
            self.y = 18
        else:
            self.y = -1
        print(f"L'acceleration moyenne de votre objet sera donc de {y}")
#
pos = Pos()

#

count = 0
print(f"Position {count} : ({pos.x}, {pos.y}) \n")

#

count += 1
pos.init(4, math.log2(2))
print(f"Position {count} : ({pos.x}, {pos.y}) \n")

#

count += 1
pos.define(3, 9)
print(f"Position {count} : ({pos.x}, {pos.y}) \n")

#

print(f"Element de liste : {pos.l[2]} \n Element de l'ensemble : {pos.setASCII} \n Element du dictionnaire : {pos.dictio["Age"]} \n {pos.dictio["Hobbit"]} ")

#

print( pos.l.pop(2)[3] )

#
"""

"""
import matplotlib.pyplot as plt

x = [1, 1.5, 3, 5, 3.5, 4.5, 3.5, 4, None]

for tp, tzs in enumerate( x ):
    # plt.hist(x, bins=2, range=(0,10), density=True, orientation='horizontal', color='red')    # error
    plt.scatter([1+tp, 1.5+tp, 3+tp, 5+tp, 3.5+tp, 4.5+tp, 3.5+tp, 4+tp, ],
                [1+tp, 2+tp, 4+tp, 7+tp, 5+tp, 5+tp, 4.5+tp, 4+tp, ],
            )
    plt.pause(2)

"""

