# main.py

from simulator import simulate
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

        print("\nSummary complete for:", deck_type)


if __name__ == "__main__":
    main()