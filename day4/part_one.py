with open('input.txt') as f:
    lines = f.readlines()

    ans = 0

    for line in lines:
        split_card = line.split(":")[1].split("|")
        winning_card = split_card[0].strip().split()
        my_card = split_card[1].strip().split()

        value = -1
        winning_numbers = set([int(x) for x in winning_card])
        for num in my_card:
            if int(num) in winning_numbers:
                value += 1
        
        if value != -1:
            ans += 2 ** value

    print("Answer is:", ans)