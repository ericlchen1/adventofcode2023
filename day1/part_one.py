with open('input.txt') as f:
    lines = f.readlines()
    
    ans = 0

    for line in lines:
        first, last = -1, -1
        for v in line:
            if v.isdigit():
                if first == -1:
                    first = int(v)
                last = int(v)
        if first != -1:
            ans += first*10 + last

    print("Answer is:", ans)