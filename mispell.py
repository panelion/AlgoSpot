import sys

rl = lambda: sys.stdin.readline()
n = int(rl())

result = []
for i in range(n):
    index, str_contents = str(rl()).strip().split(' ')
    print str(i + 1) + " " + str_contents[0:int(int(index)-1)] + str_contents[int(index):len(str_contents)]