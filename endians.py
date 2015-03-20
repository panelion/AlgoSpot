import sys

rl = lambda: sys.stdin.readline()
n = int(rl())

result = []
for i in range(n):
    input_number = int(rl())
    bit_array = [input_number >> i & 1 for i in range(31, -1, -1)]
    reverse_bit_array = []
    for j in range(32, -1, -8):
        reverse_bit_array.extend(bit_array[j - 8:j])

    result.append(int("".join(str(j) for j in reverse_bit_array), 2))

for r in result:
    print r