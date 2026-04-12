# policies.py --> Defines policies

# Policy 1: if hand >= 17 stick, else hit
def policy_1(hand, dealer_upcard=None):
    return hand.get_value() < 17

# Policy 2: if hand >= 17 AND hard --> stick, else hit (unless hand = 21)
def policy_2(hand, dealer_upcard=None):
    value = hand.get_value()

    # Always stand on 21
    if value == 21:
        return False

    # Stand only if hard 17+
    if value >= 17 and not hand.is_soft():
        return False

    # Otherwise hit
    return True

# Policy 3: always stick
def policy_3(hand, dealer_upcard=None):
    return False

# Policy 4 (Custom 1): Soft-hand agressive strategy
def policy_4(hand, dealer_upcard=None):
    if hand.is_soft():
        return hand.get_value() < 19
    return hand.get_value() < 17

# Policy 5 (Custom 2): Dealer-aware Strategy
def policy_5(hand, dealer_upcard):
    value = hand.get_value()
    
    # Normalize dealer value
    dealer_value = 11 if dealer_upcard == 1 else dealer_upcard

    # Always stand on 21
    if value == 21:
        return False

    # Hard 17+
    if not hand.is_soft() and value >= 17:
        return False

    # Soft hands
    if hand.is_soft():
        # stand on soft 19+
        if value >= 19:
            return False
        
        # soft 18 behavior depends on dealer
        if value == 18:
            # stand vs weak dealer, otherwise hit
            if dealer_value in [2, 3, 4, 5, 6]:
                return False
            return True
        
        # soft 17 or lower always hit
        return True

    # Hard 12–16
    if 12 <= value <= 16:
        # stand vs weak dealer
        if dealer_value in [2, 3, 4, 5, 6]:
            return False
        return True

    # Hard 11 or less always hit
    if value <= 11:
        return True

    # fallback (should rarely be reached)
    return False