import sys


rl = lambda: sys.stdin.readline()
n = int(rl())

result = []
for i in range(n):
    subject = str(rl()).strip()
    values = str(rl()).strip().split(' ')

    sum_value = 0
    for j in range(0, len(values)):
        sum_value += int(values[j])

    print "YES" if int(subject) >= sum_value else "NO"