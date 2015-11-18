###########################################################################
#This game is made for practice the use of python.		  		  		  
#Rock, paper, scissors prompts player to 'choose his hand'.		  		  
#The computer chooses random hand and compares it to players hand.		  
#If the player wins the round, one point is added to players score.		  
#If the computer wins the round, one point is adds to the computers score.
#If the round ends with a draw, neither gets a point.					  
#game continues until chosen amount of rounds has been won.				  
###########################################################################

#prompts the player for number of rounds
def gameStart():
	while True:
		try:
			numberOfRounds = int(raw_input('Choose the number of rounds: \n'))
		except ValueError:
			print ("Please enter a number")
			continue
		if numberOfRounds < 1:
			print "The number of rounds must be bigger than zero"
			continue
		else:	
			#Succesful input
			return numberOfRounds
			break

#number of wins required
roundsLeft = gameStart()			

#prints how many rounds are left			
print "\nRounds left: ", roundsLeft			
#prompts the player for the hand of choice			
def playerHand():
	while True:
		try:
			playerHand = raw_input('Choose your hand: \n-A is Rock \n-B is Paper \n-C is Scissor \n').lower()
		except:
			pass
		if playerHand == 'a':
			print "You chose Rock!"
			return playerHand
			break
		if playerHand == 'b':
			print "You chose Paper!"
			return playerHand
			break
		if playerHand == 'c':
			print "You chose Scissors!"
			return playerHand
			break
		else:
			print "Please choose A, B or C \n"
			continue
			
playerHand()			