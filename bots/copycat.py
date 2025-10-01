def bananabid(my_player_number, my_bananas, monkey_position, opponent_bananas, past_bid_list, turn_number):

	if turn_number == 1:
		return 25

	last_turn = past_bid_list[-1]
	opponent_bid = last_turn[2 - my_player_number]

	if my_bananas >= opponent_bid:
		return opponent_bid
	else:
		return my_bananas