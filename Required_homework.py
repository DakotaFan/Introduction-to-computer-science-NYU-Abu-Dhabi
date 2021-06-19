#Obstruction game. 
NUM_ROW = 10
NUM_COLUMN = 10
CHECKER_1= "O"
CHECKER_2 = "x"
LANDMINE = "#"
board = []
# first create the board with 6 rows and columns
for row in range(NUM_ROW):
	row_list = []
	for column in range(NUM_COLUMN):
		row_list.append(" ")
	board.append(row_list)			#create the board first with the space string

#################Next print out the board##########################
for column in range(NUM_COLUMN):
	print('   ' + str(chr(column + 65)), end='')		#convert the number to letter using ASCII table

print("\n +" + "---+"* NUM_COLUMN)			

for row in range(NUM_ROW):
	print(str(row)+ '| ', end = '')
	for col in range(NUM_COLUMN):
		print(board[row][col] + ' | ', end = '')
	print("\n +" + "---+"*NUM_COLUMN)

import random
import os
num_players = 2
#create a list, so I can use indices to randomly choose a user to start
players = [CHECKER_1, CHECKER_2]	#checker_1 is the player using "O", and checker_2 is the player using "X"
first_turn = random.randint(0, num_players - 1)	#generate a random game starter, could be "x" or "O"
checker_now = True      # I set this to be true in order for the while loop to run at least once, then the inner loop will update the real checker position

empty_coordinate = 0		#check how many space strings are left in the board,useful to detect the end of the game

while checker_now:
	print("player", players[first_turn], "It is your turn!")#generate a random starter
	checker_now = input("Please enter the coordinate here, your coordinate should consist of a Capital letter followed by a digit, eg. B4, C1, A5, D3 : " )
	if len(checker_now) != 2 or checker_now[0].isalpha() == False or checker_now[1].isdigit() == False:   #if the user's input is not in length of 2, or the format is not a letter followed by a number
		print("Sorry your input coordinate is invalid. Please try again")
		checker_now = True     
		continue    
	else:	#if the user's input is in the right format, proceed
		index_row = int(checker_now[1])					#the row location of the checker
		index_column = ord(checker_now[0]) - 65			#the column location of the checker
		if 0 <= index_row <= NUM_ROW -1 and 0 <= index_column <= NUM_COLUMN -1:#check if the entered coordinate is in the range or has not been occupied
			if board[index_row][index_column] == " " and 0 < index_row < NUM_ROW -1 and 0 < index_column < NUM_COLUMN -1: #the most common cases when users enter a coordinate and all the surrounding position will be blocked
				board[index_row][index_column] = (players[first_turn])
				board[index_row + 1][index_column] = LANDMINE
				board[index_row ][index_column + 1] = LANDMINE
				board[index_row + 1][index_column + 1] = LANDMINE
				board[index_row - 1][index_column] = LANDMINE
				board[index_row][index_column -1] = LANDMINE
				board[index_row - 1][index_column -1 ] = LANDMINE
				board[index_row + 1][index_column-1] = LANDMINE
				board[index_row - 1][index_column + 1] = LANDMINE
			elif board[index_row][index_row] == " " and index_row == 0 and index_column == 0: #when user enter A0, make sure the it only block three adjacent positions
				board[index_row][index_column] = (players[first_turn])
				board[index_row + 1][index_column] = LANDMINE
				board[index_row + 1][index_column + 1] = LANDMINE
				board[index_row][index_column + 1] = LANDMINE
			elif board[index_row][index_column] == " " and index_row == NUM_ROW - 1 and index_column == 0:#when user enter A5, it only block three adjacent positions
				board[index_row][index_column] = (players[first_turn])
				board[index_row - 1][index_column] = LANDMINE
				board[index_row - 1][index_column + 1] = LANDMINE
				board[index_row ][index_column +1 ] = LANDMINE
			elif board[index_row][index_column] == " " and index_row == 0 and index_column == NUM_COLUMN - 1:#when user enter F0, it only block three adjacent positions
				board[index_row][index_column] = players[first_turn]
				board[index_row][index_column - 1] = LANDMINE
				board[index_row + 1][index_column -1 ] = LANDMINE
				board[index_row + 1][index_column] = LANDMINE
			elif board[index_row][index_column] == " " and index_row == NUM_ROW - 1 and index_column == NUM_COLUMN - 1:#when the user enter F5, same as above
				board[index_row][index_column] = players[first_turn]
				board[index_row - 1][index_column] = LANDMINE
				board[index_row - 1][index_column - 1] = LANDMINE
				board[index_row][index_column - 1] = LANDMINE
			elif board[index_row][index_column] == " " and index_column == 0: #when the user choose the A colomn but not the corners
				board[index_row][index_column] = players[first_turn]
				board[index_row + 1][index_column] = LANDMINE
				board[index_row][index_column+1] = LANDMINE
				board[index_row  + 1 ][index_column+1] = LANDMINE
				board[index_row - 1][index_column+1] = LANDMINE
				board[index_row - 1][index_column] = LANDMINE
			elif board[index_row][index_column] == " " and index_row == 0:#when the user choose the 0 row but not the corners
				board[index_row][index_column] = players[first_turn]
				board[index_row][index_column - 1] = LANDMINE
				board[index_row + 1][index_column - 1] = LANDMINE
				board[index_row + 1][index_column] = LANDMINE
				board[index_row + 1][index_column + 1] = LANDMINE
				board[index_row][index_column + 1] = LANDMINE
			elif board[index_row][index_column] == " " and index_row == NUM_ROW - 1:#when the user choose the 5 row but not the corners
				board[index_row][index_column] = players[first_turn]
				board[index_row][index_column - 1] = LANDMINE
				board[index_row -1][index_column - 1] = LANDMINE
				board[index_row - 1][index_column] = LANDMINE
				board[index_row - 1][index_column + 1] = LANDMINE
				board[index_row][index_column + 1] = LANDMINE
			elif board[index_row][index_column] == " " and index_column == NUM_COLUMN - 1:#when the user choose the F column but not the corners
				board[index_row][index_column] = players[first_turn]
				board[index_row + 1 ][index_column] = LANDMINE
				board[index_row -1][index_column] = LANDMINE
				board[index_row - 1][index_column - 1] = LANDMINE
				board[index_row + 1][index_column - 1] = LANDMINE
				board[index_row][index_column - 1] = LANDMINE
		#if their input is not valid, then return the sorry message and ask the same user to try again
			else:
				print("Sorry this input coordinate has been occupied. Please try again")
				checker_now = True 	#go back to the while loop, ask the user to re-enter a valid coordinate
				continue
		else:
			print("Sorry the coordinate is invalid. Please try again")
			checker_now = True
			continue

	#if the input is valid, then show checkers and the landmines in the board
	os.system("clear")
	for column in range(NUM_COLUMN):
		print('   ' + str(chr(column + 65)), end='')	
	print("\n +" + "---+"* NUM_COLUMN)
	for row in range(NUM_ROW):
		print(str(row)+ '| ', end = '')
		for col in range(NUM_COLUMN):
			print(board[row][col] + ' | ', end = '')
		print("\n +" + "---+"*NUM_COLUMN)
	
	for lst in board:#keep track of how many space strings left in the board, if not, detect who is the winner, and break the while loop
		for element in lst:
			if element == " ":
				empty_coordinate += 1
	if empty_coordinate == 0:
		print("Player", players[first_turn], "Congratulations! You win")#print out the Congrats message for the winner
		break
	else:
		empty_coordinate = 0     #set it back to zero after each turn

	#this following if statement helps me to switch turns between different players			
	if CHECKER_1 == players[first_turn]:#if current player is checker 1
		first_turn = 1  #set the next player to be checker 2, using players[1]
		checker_now = True
		continue	#go back to the while loop
	else:
		first_turn = 0   #if the current player is checker 2, switch next turn to checker 1
		checker_now = True
		continue



