import random
#Infinite loop to keep the game running
while True: 
    choose = ["rock", "paper", "scissors"]
    system = random.choice(choose)
    user = input('User Choice: ').lower()
    
    # Check if user input is valid or not
    if user not in choose: 
        print('Error: Invalid input!!')
        # Prompt user again if input is valid
        continue 
    
    print('Computer:', system)
    
    if user == system:
        print('Tie!!')
        
    elif (user == 'rock' and system == 'scissors') or (user =='paper' and system =='rock') or (user =='scissors' and system == 'paper'):
        print('User Wins')
        
    else:
        print('Computer Wins') 
        
# Asks user is they want to play again
    play_again = input('Play Again ? (y/n): ')
    if play_again != 'y':
        print('Thanks for playing')
        break