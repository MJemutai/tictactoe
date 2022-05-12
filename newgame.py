"""Welcome to tic-tac-toe game. The rules are simple first one
 to get a complete horizontal or diagonal line of either 'x' or 'o' wins!!"""

#  |_1_|_2_|_3_|
#  |_4_|_5_|_6_|
#  |_7_|_8_|_9_|
# Player one enters

# Player two enters
# Player one uses x, player two uses o





g1 = """|_1_|_2_|_3_|
|_4_|_5_|_6_|
|_7_|_8_|_9_|"""
g2 = """|_1_|_2_|_3_|
|_4_|_5_|_6_|
|_7_|_8_|_9_|"""

g = """|_1_|_2_|_3_|
|_4_|_5_|_6_|
|_7_|_8_|_9_|"""


from store import match_one
m1 = """|_x_|_x_|_x_|         
|_4_|_5_|_6_|
|_7_|_8_|_9_|"""
one_attempts = 0
def playerone():

    global a
    a = input("Player one's turn:")  # player one first try
    global b1
    b1 = g1.replace(a, "x")
    print(b1)
    global b
    b = g.replace(a, "x")
    print(b)


def playertwo():
    g = """|_1_|_2_|_3_|
    |_4_|_5_|_6_|
    |_7_|_8_|_9_|"""
    global c
    c = input("Player two's turn:")  # player one first try
    global d1
    d1 = g2.replace(c, "o") # that is only "o"
    print(d1)
    g = b
    global d
    d = g.replace(c, "o")
    print(d)


print("Lets go!!")
# playerone()
# playertwo()
one_attempts_limit = 3
while one_attempts < one_attempts_limit:
    one_attempts += 1
    if one_attempts == 1:
       playerone()
       playertwo()
    else:
        g = d
        g1 = b1
        g2 = d1
        playerone()
        if one_attempts == 3:
            print(a)
            print(b1)
            print(m1)
            if b1 == m1:
                print("Player one wins!")

        playertwo()
        if one_attempts == 3:
            print("Check winner")
            # if (c == 1 and c == 2 and c == 3):
            #     print("Player two wins!")



# if one_attempts > 1:

    # g = d
    # playerone()
    # playertwo()


    # if one_attempts == one_attempts_limit:
    #     print("Check for winner")

#     # one_attempts = 1
#     players(one_attempts)
#     # one_attempts += 1
#     # another(g)
# if one_attempts > 3:
#     print("Check for winner")
