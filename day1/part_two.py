DIGITS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

class TrieNode:
    def __init__(self, value=None):
        self.children = {}
        self.end = False
        self.value = value


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, value):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end = True
        node.value = value
    
    def getRoot(self):
        return self.root


digit_trie = Trie()
for digit in DIGITS:
    digit_trie.insert(digit, DIGITS[digit])


with open("input.txt") as f:
    lines = f.readlines()
    
    ans = 0
    root = digit_trie.getRoot()

    for line in lines:
        line_len = len(line)
        first, last = -1, -1
        first_idx, last_idx = line_len, -1

        possible_digits = []

        for i, v in enumerate(line):
            if v.isdigit():
                if first == -1:
                    first = int(v)
                    first_idx = i
                last = int(v)
                last_idx = i
            else:  # Assume alphabetical
                temp = []
                for possible_digit in possible_digits:
                    if v in possible_digit.children:
                        if possible_digit.children[v].end:
                            if i < first_idx:
                                first = possible_digit.children[v].value
                                first_idx = i
                            if i > last_idx:
                                last = possible_digit.children[v].value
                                last_idx = i
                        else:
                            temp.append(possible_digit.children[v])
                if v in root.children:
                    temp.append(root.children[v])
                possible_digits = temp

        if first != -1:
            ans += first*10 + last

    print("Answer is:", ans)