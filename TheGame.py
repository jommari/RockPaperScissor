###########################################################################
#RockPaperScissors game engine that uses functions from RockPaperScissor.py
###########################################################################
import RockPaperScissor

#Ask how many rounds the player wants to player
roundsLeft = RockPaperScissor.gameStart()
playerScore = 0
computerScore = 0
#Loop through until chosen rounds have been won
while True: 
	player = RockPaperScissor.playerHand()
	computer = RockPaperScissor.computerHand()
	
	#'a' for rock, 'b' for paper and 'c' for scissors
	if (player == 'a' and computer == 'b') or (player == 'b' and computer == 'c') or (player == 'c' and computer == 'a'):
		print "The computer won this round!"
		computerScore += 1
		print "Player's score: ", playerScore
		print "Computer's score: ", computerScore
		if computerScore == roundsLeft:
			print "The computer won %s rounds!" % (roundsLeft)
			break
	elif (player == 'a' and computer == 'c') or (player == 'c' and computer == 'b') or (player == 'b' and computer == 'a'):
		print "The player won this round!"
		playerScore += 1
		print "Player's score: ", playerScore
		print "Computer's score: ", computerScore
		if playerScore == roundsLeft:
			print "The player won %s rounds!" % (roundsLeft)
			break
	elif player == computer:
		print "Draw\n"
	
	