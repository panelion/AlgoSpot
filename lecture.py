import sys

rl = lambda: sys.stdin.readline()
n = int(rl())

result = []
for i in range(n):
    str_contents = str(rl()).strip()
    split_list = [str_contents[j:j+2] for j in range(0, len(str_contents), 2)]
    split_list.sort()
    print "".join(split_list)