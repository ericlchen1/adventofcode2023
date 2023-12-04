from collections import defaultdict

with open('input.txt') as f:
    lines = f.readlines()

    ans = 0
    # dict of card_num: card_count
    cards = defaultdict(int)

    for line in lines:
        temp = line.split(":")
        card_num = int(temp[0].split()[1])
        split_card = temp[1].split("|")
        winning_card = split_card[0].strip().split()
        my_card = split_card[1].strip().split()

        value = 0
        winning_numbers = set([int(x) for x in winning_card])
        for num in my_card:
            if int(num) in winning_numbers:
                value += 1
        
        cards[card_num] += 1
        curr_card_count = cards[card_num]
        if value != 0:
            for i in range( value):
                cards[card_num + i + 1] += curr_card_count

    for card in cards.values():
        ans += card

    print("Answer is:", ans)