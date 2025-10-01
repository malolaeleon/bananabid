def bananabid(my_player_number, my_bananas, monkey_position, opponent_bananas, past_bid_list, turn_number):
    
    bid_attempt = 10 * (2 ** (turn_number - 1))
    if bid_attempt <= my_bananas:
        return bid_attempt
    else:
        return my_bananas    