# main.py

from simulator import simulate, simulate_multiple
from policies import policy_1, policy_2, policy_3, policy_4, policy_5


def main():
    policies = {
        "Policy 1 (>=17)": policy_1,
        "Policy 2 (hard/soft 17)": policy_2,
        "Policy 3 (always stick)": policy_3,
        "Policy 4 (soft aggressive)": policy_4,
        "Policy 5 (dealer-aware)": policy_5
    }

    deck_types = ["infinite", "single"]
    num_games = 1000000  # increase to 500000 or 1M for final report

    #single Player Simulation

    for deck_type in deck_types:
        print("\n===================================")
        print(f"DECK TYPE: {deck_type.upper()}")
        print("===================================\n")

        results_table = []

        for name, policy in policies.items():
            results = simulate(policy, deck_type, num_games)

            results_table.append((name, results))

            print(f"{name}")
            print(f"  Win Rate:  {results['win_rate']:.4f}")
            print(f"  Loss Rate: {results['loss_rate']:.4f}")
            print(f"  Draw Rate: {results['draw_rate']:.4f}")
            print(f"  Expected Value: {results['expected_value']:.4f}")
            print("-----------------------------------")

        
    #multi player simulation 

    print ("\n===== Multi Player Sim ====\n")

    table = [
        policy_5, 
        policy_3, 
        policy_1, 
        policy_4, 
        policy_2, 
    ]
    print("RUNNING MULTIPLAYER SIMULATION...")
    results = simulate_multiple(table, deck_type='infinite', num_games=1000000)

    print(f"Multi Player Simulation Results (Your position):")
    print(f"  Win Rate:  {results['win_rate']:.4f}")
    print(f"  Loss Rate: {results['loss_rate']:.4f}")   
    print(f"  Draw Rate: {results['draw_rate']:.4f}")
    print(f"  Expected Value: {results['expected_value']:.4f}")

    #expirment with different tables (all bad vs all good)

    print("\n===== Multi Player Experiment ====\n")
    #You are alwsy the frist player
    #Bad Table (eveyone plays bad _ )
    bad_table = [
        policy_5, #YOU
        policy_3, 
        policy_3,
        policy_3, 
        policy_3
    ]

    #Good Table (eveyone plays well) 
    good_table = [
        policy_5, 
        policy_5, 
        policy_5, 
        policy_5, 
        policy_5
    ]

    for deck_type in ['infinite', 'single']:
        print(f"\n--- {deck_type.upper()} DECK ---")

        bad_results = simulate_multiple(bad_table, deck_type,1000000)
        good_results = simulate_multiple(good_table, deck_type, 1000000)

        print("\nBad Table Results:")
        print(f"  Win Rate:  {bad_results['win_rate']:.4f}")
        print(f"  Loss Rate: {bad_results['loss_rate']:.4f}")
        print(f"  Draw Rate: {bad_results['draw_rate']:.4f}")
        print(f"  Expected Value: {bad_results['expected_value']:.4f}")

        print("\nGood Table Results:")
        print(f"  Win Rate:  {good_results['win_rate']:.4f}")
        print(f"  Loss Rate: {good_results['loss_rate']:.4f}")
        print(f"  Draw Rate: {good_results['draw_rate']:.4f}")
        print(f"  Expected Value: {good_results['expected_value']:.4f}")

if __name__ == "__main__":
    main()