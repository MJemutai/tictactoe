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

one_attempts = 0

g = """|_1_|_2_|_3_|
|_4_|_5_|_6_|
|_7_|_8_|_9_|"""

def playerone():  
    global a 
    a = input("Player one's turn:") #player one first try
    global b
    b = g.replace(a,"x")
    print (b)

def playertwo():
    c = input("Player two's turn:") #player one first try
    g = b
    global d
    d = g.replace(c,"o")
    print (d)

  
        
    
    

print("Lets go!!")
one_attempts_limit = 3
while one_attempts < one_attempts_limit:
    # if one_attempts == 1:
    playerone()
    playertwo()
    # if one_attempts > 1:
    g = d
    playerone()
    playertwo()

    if one_attempts == one_attempts_limit:
        print("Check for winner")
   
    

    
#     # one_attempts = 1
#     players(one_attempts)
#     # one_attempts += 1
#     # another(g)
# if one_attempts > 3:
#     print("Check for winner")
