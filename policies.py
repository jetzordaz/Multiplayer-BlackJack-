# policies.py --> Defines policies

# Policy 1: if hand >= 17 stick, else hit

def policy_1(hand):
    return hand.get_value() < 17

# Policy 2: if hand >= 17 AND hard --> stick, else hit (unless hand = 21)
def policy_2(hand):
    value = hand.get_value()
    if value == 21: return False
    if value >= 17 and not hand.is_soft():
        return False
    return True