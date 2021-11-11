import random 

while True:
	raction_list = ['paper', 'scissors', 'stone']

	raction = random.choice(raction_list)

	action = input('Enter "quit" to exit anytime\nPick the action - "Paper/Stone/Scissors": ')

	print(f"Computer pick - {raction}\n")

	if raction == 'paper' and action.lower() == 'stone':
		print('Computer won the battle\n')
	elif raction == 'paper' and action.lower() == 'paper':
		print('Tie!\n')
	elif raction == 'paper' and action.lower() == 'scissors':
		print('You won the battle\n')

	elif raction == 'stone' and action.lower() == 'stone':
		print('Tie!\n')
	elif raction == 'stone' and action.lower() == 'paper':
		print('You won the battle\n')
	elif raction == 'stone' and action.lower() == 'scissors':
		print('Computer won the battle\n')

	elif raction == 'scissors' and action.lower() == 'scissors':
		print('Tie!\n')
	elif raction == 'scissors' and action.lower() == 'paper':
		print('Computer won the battle\n')
	elif raction == 'scissors' and action.lower() == 'stone':
		print('You won the battle\n')
	
	if action == 'quit':
		break
	else:
		print('Something went wrong')

		



