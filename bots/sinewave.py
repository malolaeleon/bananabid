import math, random

initial_random_offset = random.randint(0, 360)

def bananabid(my_player_number, my_bananas, monkey_position, opponent_bananas, past_bid_list, turn_number):

	degrees_per_turn = 39
	degrees_now = (initial_random_offset + (degrees_per_turn * turn_number)) % 360

	scale_factor = 50
	curve = int(scale_factor * math.sin(math.radians(degrees_now)) + scale_factor)

	if curve <= my_bananas:
		return curve
	else:
		return my_bananas