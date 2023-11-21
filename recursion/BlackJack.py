
# This is way too inefficient to be used in a real game of blackjack?
def slowProbDealerBust(startingHand, target=21):
    if startingHand > target:
        return 1
    elif startingHand >= target-4:
        return 0
    else:
        return (0.1 * slowProbDealerBust(startingHand + 1) 
                + 0.1 * slowProbDealerBust(startingHand + 2)
                + 0.1 * slowProbDealerBust(startingHand + 3)
                + 0.1 * slowProbDealerBust(startingHand + 4)
                + 0.1 * slowProbDealerBust(startingHand + 5)
                + 0.1 * slowProbDealerBust(startingHand + 6)
                + 0.1 * slowProbDealerBust(startingHand + 7)
                + 0.1 * slowProbDealerBust(startingHand + 8)
                + 0.1 * slowProbDealerBust(startingHand + 9)
                + 0.1 * slowProbDealerBust(startingHand + 10))

def fastProbDealerBust(startingHand, target=21):
    """
    Calculate the probability of the dealer busting in a card game, 
    starting with a given hand, using memoization for efficiency.

    This function serves as a wrapper for the recursive function calculateProbDealerBust.

    Args:
        startingHand (int): The initial value of the dealer's hand.
        target (int, optional): The threshold value at which the dealer busts. Defaults to 21.

    Returns:
        float: The probability of the dealer busting, starting with the given hand.
    """
    memo = {}  # Initialize an empty dictionary for memoization
    return calculateProbDealerBust(startingHand, target, memo)
    
def calculateProbDealerBust(currentHand, target, memo):
    """
    Recursively calculate the probability of busting for a given hand value, 
    utilizing memoization to store and reuse previously computed probabilities.

    Args:
        currentHand (int): The current value of the hand being evaluated.
        target (int): The threshold value at which the dealer busts.
        memo (dict): A dictionary for storing previously computed probabilities to avoid redundant calculations.

    Returns:
        float: The probability of busting for the current hand.
    """
    # Check if the current hand's probability has already been computed
    if currentHand in memo:
        return memo[currentHand]
    # Base case: If the current hand exceeds the target, the dealer has busted
    elif currentHand > target:
        return 1
    # Base case: If the current hand is close enough to the target, assume dealer will stop drawing cards
    elif currentHand >= target-4:
        return 0
    else:
        totalProb = 0  # Initialize total probability
        # Iterate through all possible next card values (1 to 10)
        for nextCard in range(1, 11):
            # Recursively calculate the probability for each possible next hand
            # Assuming each card has an equal probability (0.1) of being drawn
            totalProb += 0.1 * calculateProbDealerBust(currentHand + nextCard, target, memo)

        # Store the computed probability in memoization dictionary
        memo[currentHand] = totalProb
        return totalProb

    
prob = fastProbDealerBust(5, 100)

print(f'Probability of dealer busting: {prob}')