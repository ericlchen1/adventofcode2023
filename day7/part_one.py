from collections import Counter
import heapq

CARD_VALUES = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
}

def get_card_value(card):
    if card in CARD_VALUES:
        return CARD_VALUES[card]
    return int(card)

def get_priority(cards):
    card_values = [get_card_value(card) for card in cards]
    counts = Counter(card_values)
    most_common_cards = counts.most_common(2)

    if counts[most_common_cards[0][0]] == 5:
        return [6] + card_values
    elif counts[most_common_cards[0][0]] == 4:
        return [5] + card_values
    elif counts[most_common_cards[0][0]] == 3 and counts[most_common_cards[1][0]] == 2:
        return [4] + card_values
    elif counts[most_common_cards[0][0]] == 3:
        return [3] + card_values
    elif counts[most_common_cards[0][0]] == 2 and counts[most_common_cards[1][0]] == 2:
        return [2] + card_values
    elif counts[most_common_cards[0][0]] == 2:
        return [1] + card_values
    else:
        return [0] + card_values

with open("input.txt") as f:
    lines = f.readlines()

    ans = 0
    hands_and_bids = []

    for line in lines:
        hand, bid = line.strip().split()
        heapq.heappush(hands_and_bids, (get_priority(hand), int(bid)))

    rank = 1
    while hands_and_bids:
        ans += heapq.heappop(hands_and_bids)[1] * rank
        rank += 1

    print("Answer is:", ans)
