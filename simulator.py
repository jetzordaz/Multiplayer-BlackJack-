# simulator.py --> Monte Carlo simulation
from game import BlackjackGame
from deck import Deck

def simulate(policy, deck_type='infinite', num_games=100):
    wins = 0
    losses = 0
    draws = 0

    for _ in range(num_games):
        deck = Deck(deck_type)
        game = BlackjackGame(deck)
        result = game.play(policy)

        if result == 1:
            wins += 1
        elif result == -1:
            losses += 1
        else:
            draws += 1

    win_rate = wins / num_games
    loss_rate = losses / num_games
    draw_rate = draws / num_games

    expected_value = win_rate - loss_rate

    return {
        "wins": wins,
        "losses": losses,
        "draws": draws,
        "win_rate": win_rate,
        "loss_rate": loss_rate,
        "draw_rate": draw_rate,
        "expected_value": expected_value
    }

def simulate_multiple(policies, deck_type='infinite', num_games=100):
    wins = 0
    losses = 0
    draws = 0

    for _ in range(num_games):
        deck = Deck(deck_type)
        game = BlackjackGame(deck)
        results = game.play_multiple(policies)
       # print("FULL result:", results)   Debugging line to see the full results



        result = results[0] # You are first player
        # print("First player reslut:", result)  Debugging line to see the first player's result

        if result == 1:
            wins += 1
        elif result == -1:
            losses += 1
        else:
            draws += 1

    win_rate = wins / num_games
    loss_rate = losses / num_games
    draw_rate = draws / num_games

    expected_value = win_rate - loss_rate

    return {
        "wins": wins,
        "losses": losses,
        "draws": draws,
        "win_rate": win_rate,
        "loss_rate": loss_rate,
        "draw_rate": draw_rate,
        "expected_value": expected_value
    }