import bisect

def read_map(f):
    dic = {}
    # Two buffer lines between each input
    f.readline()
    line = f.readline()
    while line and line != "\n":
        parsed_line = [int(x) for x in line.strip().split()]
        dic[parsed_line[1]] = (parsed_line[0], parsed_line[2])
        line = f.readline()
    return dic

def get_floor_key(arr, key):
    index = bisect.bisect_right(arr, key)
    if index:
        return arr[index - 1]
    return -1

def get_translated_dict(input, translation_dict):
    translation_keys = sorted([x for x in translation_dict.keys()])
    ret = set()
    for x in input:
        floor_key = get_floor_key(translation_keys, x)
        if floor_key != -1 and floor_key + translation_dict[floor_key][1] > x:
            ret.add(x + translation_dict[floor_key][0] - floor_key)
        else:
            ret.add(x)
    return ret


with open("input.txt") as f:
    seeds = [int(x) for x in f.readline().strip().split(": ")[1].split()]
    f.readline()

    seed_to_soil = read_map(f)
    soil = get_translated_dict(seeds, seed_to_soil)

    soil_to_fertilizer = read_map(f)
    fertilizer = get_translated_dict(soil, soil_to_fertilizer)

    fertilizer_to_water = read_map(f)
    water = get_translated_dict(fertilizer, fertilizer_to_water)

    water_to_light = read_map(f)
    light = get_translated_dict(water, water_to_light)

    light_to_temperature = read_map(f)
    temperature = get_translated_dict(light, light_to_temperature)

    temperature_to_humidity = read_map(f)
    humidity = get_translated_dict(temperature, temperature_to_humidity)

    humidity_to_location = read_map(f)
    location = get_translated_dict(humidity, humidity_to_location)

    print("Answer is:", min(location))