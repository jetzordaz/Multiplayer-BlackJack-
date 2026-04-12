# policies.py --> Defines policies

# Policy 1: if hand >= 17 stick, else hit
def policy_1(hand, dealer_upcard=None):
    return hand.get_value() < 17

# Policy 2: if hand >= 17 AND hard --> stick, else hit (unless hand = 21)
def policy_2(hand, dealer_upcard=None):
    value = hand.get_value()
    if value == 21: return False

    if value >= 17 and not hand.is_soft():
        return False
    
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

    dealer_value = dealer_upcard
    if dealer_upcard == 1:
        dealer_value = 11
    
    if value >= 17:
        return False
    
    if hand.is_soft():
        if value >= 19:
            return False
        
        if dealer_value in [2, 3, 4, 5, 6]:
            return value < 18
        
        return True
    
    if value <= 11:
        return True
    
    if 12 <= value <= 16:
        if dealer_value in [2, 3, 4, 5, 6]:
            return False
        else:
            return True
        
    return False