"""Welcome to tic-tac-toe game. The rules are simple first one
 to get a complete horizontal or diagonal line of either 'x' or 'o' wins!!"""

#  |_1_|_2_|_3_|
#  |_4_|_5_|_6_|
#  |_7_|_8_|_9_|
 #Player one enters

 #Player two enters
 #Player one uses x, player two uses o
g = """|_1_|_2_|_3_|
|_4_|_5_|_6_|
|_7_|_8_|_9_|"""

s1 = """|_x_|_x_|_x_|
|_4_|_5_|_6_|
|_7_|_8_|_9_|"""
print(g)
  
a = input("Player one's turn:") #player one first try
b = g.replace(a,"x")
print (b)
c = input("Player two's turn:") #player two first try
d = b.replace(c, "o")
print(d)
a1 = input("Player one's turn:") #player one second try
b1 = d.replace(a1,"x")
print (b1)
c1 = input("Player two's turn:") #player two second try
d1 = b1.replace(c1,"o")
print (d1)
a2 = input("Player one's turn:") #player one third try
b2 = d1.replace(a2,"x")
print (b2)

if int(a) == 1 and int(a1) == 2 and int(a2) == 3:
    print("Player one wins!!")
elif int(a) == 4 and int(a1) == 5 and int(a2) == 6:
    print("Player one wins!!")
elif int(a) == 7 and int(a1) == 8 and int(a2) == 9:
    print("Player one wins!!")
else:
    print("Game continues")



c2 = input("Player two's turn:") #player two third try
d2 = b2.replace(c2,"o")
print (d2)
if int(a) == 1 and int(a1) == 2 and int(a2) == 3:

    print("Player two wins!!")


def playerone():
    a = input("Player one's turn:") #player one first try
    b = g.replace(a,"x")
    print (b)

def playertwo():
    a = input("Player two's turn:") #player one first try
    b = g.replace(a,"x")
    print (b)



