# Gets full number and fills with periods
def get_full_number(lines, i, j):
    total = 0
    idx = j
    offset = 0
    line_len = len(lines[i])
    while idx >= 0 and lines[i][idx].isdigit():
        total += int(lines[i][idx]) * 10**offset
        lines[i][idx] = "."
        idx -=1
        offset += 1
    
    idx = j + 1
    while idx < line_len and lines[i][idx].isdigit():
        total = total * 10 + int(lines[i][idx])
        lines[i][idx] = "."
        idx += 1
    
    return total

# Searches all directions for numbers
def search_total(lines, i, j):
    transformations = [-1, 0, 1]
    total = 0
    for t in transformations:
        for u in transformations:
            if t == 0 and u == 0:
                continue
            transform_i, transform_j = i+t, j+u
            # transformed index is a number
            if transform_i >= 0 and transform_j >= 0 and transform_i < len(lines) and transform_j < len(lines[transform_i]) and lines[transform_i][transform_j].isdigit():
                total += get_full_number(lines, transform_i, transform_j)
    return total


with open('input.txt') as f:
    lines = [list(x.strip()) for x in f.readlines()]
    ans = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            # lines[i][j] should be a symbol other than period
            if not lines[i][j].isalnum() and lines[i][j] != ".":
                ans += search_total(lines, i, j)

    print("Answer is:", ans)
