with open("input.txt") as f:
    lines = f.readlines()

    ans = 0

    for line in lines:
        game_split = line.split(": ")
        game_num = int(game_split[0][5:])

        min_cubes = {}
        
        set_split = game_split[1].split("; ")
        for cube_set in set_split:
            cube_split = cube_set.split(", ")
            
            for cube in cube_split:
                temp = cube.split(" ")
                cube_num = int(temp[0])
                cube_color = temp[1].strip()
                if cube_color not in min_cubes:
                    min_cubes[cube_color] = cube_num
                else:
                    min_cubes[cube_color] = max(min_cubes[cube_color], cube_num)
        
        power = 1
        for cube in min_cubes.values():
            power *= cube
        ans += power


    print("Answer is:", ans)