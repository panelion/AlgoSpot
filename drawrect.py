import sys


def find_missing_point(ar):
    return ar[0] if ar[1] == ar[2] else ar[1] if ar[0] == ar[2] else ar[2]
    
rl = lambda: sys.stdin.readline()
n = int(rl())

result = []
for i in range(n):
    left_array = []
    right_array = []

    for count in range(3):
        left, right = rl().split(' ')

        left_array.append(int(left))
        right_array.append(int(right))

    result.append("%s %s" % (find_missing_point(left_array), find_missing_point(right_array)))

for r in result:
    print r