from collections import deque

def read_map(f):
    dic = {}
    # Two buffer lines between each input
    f.readline()
    line = f.readline()
    while line and line != "\n":
        dst_start, src_start, range_len = [int(x) for x in line.strip().split()]
        dic[(src_start, src_start + range_len)] = dst_start - src_start
        line = f.readline()
    return dic

def merge_intervals(intervals):
    intervals.sort()
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

# This took longer than I liked to figure out
def get_translated_intervals(intervals, translation_dict):
    ret_intervals = []
    translation_intervals = deque(sorted(translation_dict.keys()))
    sorted_intervals = deque(sorted(intervals))
    
    while sorted_intervals:
        if not translation_intervals:
            ret_intervals.append(sorted_intervals.popleft())
            continue
        # Interval start lower than translation start
        if sorted_intervals[0][0] < translation_intervals[0][0]:
            # No overlap, add as is
            if sorted_intervals[0][1] <= translation_intervals[0][0]:
                ret_intervals.append(sorted_intervals.popleft())
            # Overlaps at end, add beginning as original, next loop takes care of rest
            else:
                ret_intervals.append([sorted_intervals[0][0], translation_intervals[0][0]])
                sorted_intervals[0] = [translation_intervals[0][0], sorted_intervals[0][1]]
        # Interval start is higher than translation start
        else:
            # Translation end before interval start, remove translation
            if translation_intervals[0][1] <= sorted_intervals[0][0]:
                translation_intervals.popleft()
            # Translation end after interval start, overlaps in some way
            else:
                # Translation end after interval end, whole interval is translated
                if translation_intervals[0][1] >= sorted_intervals[0][1]:
                    interval = sorted_intervals.popleft()
                    translation = translation_dict[translation_intervals[0]]
                    ret_intervals.append([interval[0] + translation, interval[1] + translation])
                # Translation end before interval end, translated interval added
                else:
                    translation = translation_dict[translation_intervals[0]]
                    ret_intervals.append([sorted_intervals[0][0] + translation, translation_intervals[0][1] + translation])
                    sorted_intervals[0] = [translation_intervals[0][1], sorted_intervals[0][1]]
                    translation_intervals.popleft()

    return merge_intervals(ret_intervals)

with open("input.txt") as f:
    seeds = [int(x) for x in f.readline().strip().split(": ")[1].split()]
    seed_intervals = []
    for i in range(0, len(seeds) - 1, 2):
        seed_intervals.append((seeds[i], seeds[i] + seeds[i + 1]))
    seed_intervals = merge_intervals(seed_intervals)

    f.readline()

    seed_to_soil = read_map(f)
    soil_intervals = get_translated_intervals(seed_intervals, seed_to_soil)

    soil_to_fertilizer = read_map(f)
    fertilizer_intervals = get_translated_intervals(soil_intervals, soil_to_fertilizer)

    fertilizer_to_water = read_map(f)
    water_intervals = get_translated_intervals(fertilizer_intervals, fertilizer_to_water)

    water_to_light = read_map(f)
    light_intervals = get_translated_intervals(water_intervals, water_to_light)

    light_to_temperature = read_map(f)
    temperature_intervals = get_translated_intervals(light_intervals, light_to_temperature)

    temperature_to_humidity = read_map(f)
    humidity_intervals = get_translated_intervals(temperature_intervals, temperature_to_humidity)

    humidity_to_location = read_map(f)
    location_intervals = get_translated_intervals(humidity_intervals, humidity_to_location)

    print("Answer is:", min(location_intervals)[0])