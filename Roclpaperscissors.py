'''
Created on Sep 15, 2018

@author: ITAUser
'''
#Loops the whole game

keepPlaying = True
while(keepPlaying):
    print("Welcome to Rock Paper Scissors!")
    print("Best two out of three. Press 'q' or 'Q' to quit")
    
    # 1 = Rock
    # 2 = Scissors
    # 3 = paper
    
    
        #Select a random integer between 1 qnd 3
    import random
        
        
    cpuScore = 0
    humanScore = 0
    while(humanScore < 2 and cpuScore < 2):
        cpuChoice = random.randint(1,3)
        choice = input("please choose(Rock, Paper, Scissors): ")
        
        
        #checks if user wants to quit
        if(choice == 'q' or choice == 'Q'):
            keepPlaying = False
            break    
        #checks for a draw
        elif((choice.lower()=="rock" and cpuChoice ==1) or 
           (choice.lower() == "scissors" and cpuChoice ==2) or 
           (choice.lower() == "paper" and cpuChoice ==3)):
            print("draw!!") 
            print("Human: " + str(humanScore) + "CPU:" + str(cpuScore))
        #check if human wins
        elif((choice.lower()=="rock" and cpuChoice ==2) or 
           (choice.lower() == "scissors" and cpuChoice ==3) or 
           (choice.lower() == "paper" and cpuChoice ==1)):
            humanScore = humanScore +1
            print ("Human: " + str(humanScore) + "CPU:" + str(cpuScore))        
        #checks if cpu wins 
        elif((choice.lower()=="rock" and cpuChoice == 3) or 
           (choice.lower() == "scissors" and cpuChoice ==1) or 
           (choice.lower() == "paper" and cpuChoice ==2)):
            cpuScore = cpuScore +1
            print ("Human:" + str(humanScore) + "CPU: " + str(cpuScore))
        else:
            print("not an option try again.")
                
    print("Thanks for Playing")
    #These two conditions check who won the game
    if(humanScore == 2):
        print("You WON!!!")
    elif(cpuScore == 2):
        print("You lose!!!")
    #This prints the final score
    print("Human:" + str(humanScore) , "CPU: " + str(cpuScore))