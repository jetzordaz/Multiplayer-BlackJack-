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

# Policy 3: always stick
def policy_3(hand):
    return False

# Policy 4 (Custom 1): Soft-hand agressive strategy
def policy_4(hand):
    if hand.is_soft():
        return hand.get_value() < 19
    return hand.get_value() < 17

# Policy 5 (Custom 2): Risk-averse (avoids bust)
def policy_5(hand):
    value = hand.get_value()
    if value >= 17:
        return False
    if value == 16:
        return False
    return True