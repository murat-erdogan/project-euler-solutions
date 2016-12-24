f = open("p022_names.txt", "r")
dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
strg = f.read()
name = strg.split()
i = 0
total = 0
for current_name in name:
    i += 1
    sum = 0
    for j in range(len(current_name)):
        sum += dict[current_name[j]]
    total += sum * i

print(total)