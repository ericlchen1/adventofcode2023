BAG = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


with open("input.txt") as f:
    lines = f.readlines()

    ans = 0

    for line in lines:
        game_split = line.split(": ")
        game_num = int(game_split[0][5:])
        is_valid = True
        
        set_split = game_split[1].split("; ")
        for cube_set in set_split:
            cube_split = cube_set.split(", ")
            
            if is_valid:
                for cube in cube_split:
                    temp = cube.split(" ")
                    cube_num = int(temp[0])
                    cube_color = temp[1].strip()
                    if cube_color not in BAG or cube_num > BAG[cube_color]:
                        is_valid = False
                        break
        if is_valid:
            ans += game_num


    print("Answer is:", ans)