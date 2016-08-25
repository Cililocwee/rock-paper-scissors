import random

def main():

	game_bank = {0: 'rock', 1: 'paper', 2: 'scissors'}
	
	def rpsGame(x, y):
	
		if x == 'rock' and y == 'paper':
			print('You chose rock and the game chose paper, you lose')
			
		elif x == 'rock' and y == 'rock':
			print('You chose rock and the game chose rock, it\'s a tie')
			
		elif x == 'rock' and y == 'scissors':
			print('You chose rock and the game chose scissors, you win')
			
		elif x == 'paper' and y == 'paper':
			print('You chose paper and the game chose paper, it\'s a tie')
			
		elif x == 'paper' and y == 'rock':
			print('You chose paper and the game chose rock, you win')
			
		elif x == 'paper' and y == 'scissors':
			print('You chose paper and the game chose scissors, you lose')
			
		elif x == 'scissors' and y == 'paper':
			print('You chose scissors and the game chose paper, you win')
			
		elif x == 'scissors' and y == 'rock':
			print('You chose scissors and the game chose rock, you lose')
			
		elif x == 'scissors' and y == 'scissors':
			print('You chose scissors and the game chose scissors, it\'s a tie')
			
		else:
			print('Try again, your input was wrong.')
				
		

	while True:
		
		user_choice = input('Please enter "rock", "paper", or "scissors". \n>')
		if user_choice == 'r':
			user_choice = 'rock'
		elif user_choice == 's':
			user_choice = 'scissors'
		elif user_choice == 'p':
			user_choice = 'paper'
	
		
		game_choice = random.choice(game_bank)
		
		rpsGame(user_choice, game_choice)
		
			
	
	


if __name__ == '__main__':
	main()