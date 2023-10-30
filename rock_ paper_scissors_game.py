import  random
l=["paper","rock","scissor"]
'''
rock vs paper-paper win
rock vs scissor-rock win
paper vs scissor--scissor
'''

while True:
    ccount=0 #it is used to store score of game
    ucount=0

    op=int(input('''
Game Start............    
1.Yes
2.No | Exit
    '''))
    if op==1:
         for a in range(1,6):

             userinput=int(input('''
1.rock
2.scissor
3.paper             
             '''))
             if userinput ==1:
               uchoice="rock"
             elif userinput ==2:
                uchoice = "scissor"
             elif userinput==3:
                uchoice = "paper"
             cchoice=random.choice(l)
             if cchoice==uchoice:
                 print("computer value ",cchoice)
                 print("user value",uchoice)
                 print("game draw")
                 ucount=ucount+1
                 ccount=ccount+1
             elif (uchoice=="rock" and cchoice=="scissor") or (uchoice=="paper" and cchoice=="rock") or(uchoice == "scissor" and cchoice == "paper") or (uchoice=="rock" and cchoice=="scissor"):
                 print("computer value ", cchoice)
                 print("user value", uchoice)
                 print(" you win")
                 ucount = ucount + 1
             else:
                 print("computer value ", cchoice)
                 print("user value", uchoice)
                 print("computer win")
                 ccount = ccount + 1
                 print()
#we are adding the score of user and computer
    if ccount==ucount:
        print("final game draw")
        print("your score",ucount)
        print("computer score",ccount)
    elif ccount>ucount:
        print("final computer win this game")
        print("your score", ucount)
        print("computer score", ccount)
    elif ccount<ucount:
        print("final you are winner")
        print("your score", ucount)
        print("computer score", ccount)
    else:
        break