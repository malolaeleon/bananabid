import random

def bananabid(my_player_number, my_bananas, monkey_position, opponent_bananas, past_bid_list, turn_number):
	
	if opponent_bananas == 0 and my_bananas > 0:
		return 1
	else:
		if my_bananas >= 75:
			return random.randint(25, 75)
		elif my_bananas >= 25:
			return random.randint(25, my_bananas)
		else:
			return random.randint(0, my_bananas)