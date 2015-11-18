###########################################################################
#This game is made for practice the use of python.		  		  		  #
#Rock, paper, scissors prompts player to 'choose his hand'.		  		  #
#The computer chooses random hand and compares it to players hand.		  #
#If the player wins the round, one point is added to players score.		  #
#If the computer wins the round, one point is adds to the computers score.#
#If the round ends with a draw, neither gets a point.					  #
#game continues until chosen amount of rounds has been won.				  #
###########################################################################

#prompts the player for number of rounds
def gameStart():
	while True:
		try:
			numberOfRounds = int(raw_input('Choose the number of rounds: \n'))
		except ValueError:
			print ("Please enter a number")
			continue
		except numberOfRounds < 1:
			print "The number of rounds must be bigger than zero"
		else:	
			#Succesful input
			break
		
gamestart()		