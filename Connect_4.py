#Connect 4 game written by Dakota

def print_board():        #print the board function
	for column in range(NUM_COLUMN):
		print('   ' + str(chr(column + 65)), end='')		#convert the number to letter using ASCII table

	print("\n +" + "---+"* NUM_COLUMN)			

	for row in range(NUM_ROW):
		print(' | ', end = '')
		for col in range(NUM_COLUMN):
			print(board[row][col] + ' | ', end = '')
		print("\n +" + "---+"*NUM_COLUMN)					#similar to the assignment1, here I print the 2D Board

def create_players(number_of_player):
	CHECKERS_DEFAULT = ["X", "O", "V", "H", "M"]	#based on the number of the players, the number pf checkers will change
	return CHECKERS_DEFAULT[0:number_of_player]     

def player_take_turn(current_player_index):
	if current_player_index < NUM_PLAYERS-1:       #if the current player is not the last one in the list PLAYERS, then the counter increases by one
	#next player will be the next checker in the list
		next_player_index = current_player_index + 1 
		return next_player_index       #switch turn to the next one and return its index in the list
	else:
		next_player_index = 0     #if the current player is the last one in the list, the next turn will be the first one in the list
		return next_player_index   #switch turn and return its index in the list

def occupy_the_lowest_space(column):   #this funtion take the index the column, and return the lowest row available
	count_empty = 0   #accumulate through a for loop
	for i in range(NUM_ROW):    #in user's entered column, check how many empty space are there
		if board[i][column] == " ":
			count_empty += 1
	if count_empty == 0:         #if there is no empty row in the column, return False
	#this will return a TypeError when trying to add the checker
		return False
	else:
		for j in range(NUM_ROW-1, -1,  -1): #if there is empty row in the column, find the lowest one from the bottom
			if board[j][column] == " ":
				return j        #return the lowest row
def check_the_winner():						#this function will help me check if there are four checkers connected vertically, horizontally, or diagonally
	for i in range(0, NUM_ROW):			#since the stop of range will be exclusive, i use NUM_ROW - 3 instead NUM_ROW - 4
		for j in range(0, NUM_COLUMN):
			if j < NUM_COLUMN - 3:
				if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] != " ":   #horizontally
					return True
			if i < NUM_ROW -3:
				if board[i][j] ==  board[i+1][j] == board[i+2][j] == board[i+3][j] != " ": #vertically
					return True
			if i < NUM_ROW -3 and j < NUM_COLUMN - 3:
				if board[i][j] ==  board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] != " ":#diagonally
					return True
			if i >= 3 and j < NUM_COLUMN - 3:
				if board[i][j] ==  board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3] != " ":
					return True
	return False    #if no one wins, return False

def check_draw():#define check_draw as how many empty space in the list, if there is none, and no one wins
#detect the end of the game, and print "draw"
	empty_space = 0				#iterate through the board to calculate how many empty space there
	for i in range(NUM_ROW):
		for j in range(NUM_ROW):
			if board[i][j] == " ":
				empty_space += 1
	if empty_space == 0:   #if there is no empty space, game is over 
		return True
	else:
		return False      #if there is empty space, game continues
		
import random
import os, time

NUM_ROW = 6
NUM_COLUMN = 7
NUM_PLAYERS = 2
############################################
board = []
for row in range(NUM_ROW):					#create a nested list named board 
	row_list = []
	for column in range(NUM_COLUMN):
		row_list.append(" ")
	board.append(row_list)	
##############################################

		#first print the board 
PLAYERS = create_players(NUM_PLAYERS)		#second create the players

random_starter = random.randrange(0, NUM_PLAYERS, 1) #generate a random starter based on the number of players
checker_in_turn = PLAYERS[random_starter]    #use the index to select the player

#Games start here 

column_input = True    #I set this true for the while loop at leat to run once
while column_input:
	print_board()
	checker_now = PLAYERS.index(checker_in_turn)    #checker_now is the index of current player
	print("Player", checker_in_turn, end = ' ')     #check_in_turn is the current checker of the player, as "X"  "O"  "M"...
	column_input = input("Please enter the column here: ") 
	if len(column_input) != 1 or column_input.isalpha() == False:   #test if the input is in the correct format
		print("Sorry your input coordinate is invalid. Please try again")  #if not, continue and re-enter
		time.sleep(2)
		os.system("clear")
		column_input = True #Set this back to True    
		continue 
	else:
		index_column = ord(column_input) - 65           #if the input in the correct format, convert it to index of the column using ASCII table
		if index_column > NUM_COLUMN - 1:				#if the entered letter is out of range, ask the user to re-enter
			print("Sorry your input coordinate is invalid. Please try again")
			time.sleep(2)
			os.system("clear")
			column_input = True
			continue
		else:											#if the input in the correct format
			try:	#first try to put the checker to the designated column, by calling the occupy_the_lowest_space function
					#occupy_the_lowest_space(index_column) will return you a lowest row in the column, then use it as the row index
				board[occupy_the_lowest_space(index_column)][index_column] = checker_in_turn #add the current player's checker to the board
				if check_the_winner() == True:    #check if any one wins
					os.system('clear')
					print_board()
					print("Player", checker_in_turn, "Congratulations! You win!")		
					break
				elif check_draw() == True: #check if the games ends and there is a draw
					os.system('clear')
					print_board()
					print("Draw. End of the Game")
					break
				else:
					checker_in_turn = PLAYERS[player_take_turn(checker_now)] #if none of those are True, continue the game and switch the players
					time.sleep(1)
					os.system('clear')
					continue
			except TypeError:    #Handling exceptions
			 #if there is no empty row in the column, occupy_the_lowest_space(index_column) return a TypeError
				print(checker_in_turn, "Your input is not valid. Sorry you lose this turn") 
				if check_the_winner() == True:
					os.system('clear')
					print_board()				#first check if any one connect the four checkers
					print("Player", checker_in_turn, "Congratulations! You win!")	#if so, break and congrats the winner
					break
				elif check_draw() == True:
					os.system('clear')
					print_board() #then check if the game ends and if there is a draw
					print("Draw. End of the Game")
					break
				else:
					checker_in_turn = PLAYERS[player_take_turn(checker_now)]  #the current player lose its turn and alternate the turn
					time.sleep(1)
					os.system("clear")
					continue

