import random

def simulate_match(bot1, bot2, verbose=False, bot1_name="", bot2_name=""):

    player1_bananas = player2_bananas = 200
    bids = []
    monkey_pos = 0
    turn_no = 1

    p1_bid = p2_bid = 0

    while (not monkey_pos in [-3, 3]) and player1_bananas + player2_bananas > 0:
        try:
            p1_bid = bot1(
                my_player_number = 1,
                my_bananas = player1_bananas,
                monkey_position = monkey_pos,
                opponent_bananas = player2_bananas,
                past_bid_list = bids,
                turn_number = turn_no
            )
        except Exception as e:
            print(f"!!! Player 1 ({bot1_name}) threw an exception:", e, "\nData:", player1_bananas, monkey_pos, player2_bananas, bids, turn_no)
            raise e

        try:
            p2_bid = bot2(
                my_player_number = 2,
                my_bananas = player2_bananas,
                monkey_position = monkey_pos,
                opponent_bananas = player1_bananas,
                past_bid_list = bids,
                turn_number = turn_no
            )
        except Exception as e:
            print(f"!!! Player 2 ({bot2_name}) threw an exception:", e, "\nData:", player2_bananas, monkey_pos, player1_bananas, bids, turn_no)
            raise e
   

        p1_bid = min(max(0, int(p1_bid)), player1_bananas)
        p2_bid = min(max(0, int(p2_bid)), player2_bananas)

        player1_bananas -= p1_bid
        player2_bananas -= p2_bid

        if p1_bid > p2_bid:
            monkey_pos -= 1
        elif p2_bid > p1_bid:
            monkey_pos += 1

        if verbose:
            print(f"Turn {str(turn_no).rjust(3, "0")}: Player 1 ({bot1_name}) bids {str(p1_bid).rjust(3, "0")} and player 2 ({bot2_name}) bids {str(p2_bid).rjust(3, "0")}. The monkey moves to {monkey_pos}")

        bids.append([p1_bid, p2_bid])
        turn_no += 1

    if monkey_pos == -3:
        verbose and print(f"Player 1 is the winner!")
        return 1
    elif monkey_pos == 3:
        verbose and print(f"Player 2 is the winner!")
        return 2
    else:
        verbose and print("Both players lose.")
        return 0


def get_bots():
    import bots
    bot_list = {}
    for key in (bots.__dict__.keys()):
        if key.startswith('__') or key in ['os', 'module']:
            continue
        try:
            bot_list[key] = getattr(bots, key).bananabid
        except Exception as e:
            print("There was an error trying to import bananabid from", key + ". Make sure your python file has a function called bananabid!")

    return bot_list

def play_tourney(count=1000):
    bots = get_bots()
    
    # play each bot against one another 1000 times
    output_count = {}
    for bot_name in bots.keys():
        wins = losses = 0
        every_other_bot = filter(lambda name: not (name == bot_name), bots.keys())
        for other_bot in every_other_bot:
            for _ in range(count):
                winner = simulate_match(
                    *random.sample([bots[bot_name],
                    bots[other_bot]], 2)
                )
                if winner == 1:
                    wins += 1
                else:
                    losses += 1

        output_count[bot_name] = [wins, losses]

    return output_count
                
def tournament_output():
    results = play_tourney()
    leaderboard = sorted(list(zip(results.keys(), results.values())), key = lambda x: x[1][0], reverse = True)
    for idx, bot in enumerate(leaderboard):
        print(f"Place {idx + 1}: {bot[0]} with {bot[1][0]} wins and {bot[1][1]} losses.")



if __name__ == "__main__":
    print("Bananabid test harness")
    choice = None
    while not choice in [1, 2, 3, 4]:
        try:
            choice = int(input("""Select an option:
                1) Play tournament of all bots
                2) Play verbose 1v1 between two bots
                3) List bots available in bots folder
                4) Exit\nSelect: """))
        except:
            print("Please enter a number from 1 to 4.")

    match choice:
        case 1:
            tournament_output()
        case 2:
            print("Available bots to 1v1:\n" + '\n'.join([str(idx) + ") " + key for idx, key in enumerate(get_bots().keys())]))
            bot1 = bot2 = -1
            num_bots = len(get_bots().keys())

            while not bot1 in range(num_bots):
                try:
                    bot1 = int(input("Enter player 1's bot number for 1v1: "))
                except:
                    print("That isn't a valid integer!")

            while not bot2 in range(num_bots):
                try:
                    bot2 = int(input("Enter player 2's bot number for 1v1: "))
                except:
                    print("That isn't a valid integer!")

            k = list(get_bots().keys()) # Nooooo you can't convert an unordered type to an ordered one noooo what if the hash changes nooo
            print("Playing match between", k[bot1], "and", k[bot2] + ". Make sure to test your bot in both players 1 and 2 if it depends on that!")
            simulate_match(get_bots()[k[bot1]], get_bots()[k[bot2]], verbose=True, bot1_name=k[bot1], bot2_name=k[bot2])
        case 3:
            print("Available bots:", ", ".join(get_bots().keys()))
            print("Make sure your bot is a Python (.py) file in the bots folder and has a function called bananabid.")
        case 4:
            pass