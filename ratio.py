import sys


def calc_ratio(try_count, win_count):
    return long(float(win_count) * 100 / float(try_count))


def calc(try_count, win_count):
    MAX_NUM = 2000000000
    MIN_NUM = 0
    next_ratio = calc_ratio(try_count, win_count) + 1
    if next_ratio <= 100:
        search_num = search(MIN_NUM, MAX_NUM, next_ratio, try_count, win_count)
        if search_num >= MAX_NUM:
            return -1
        elif search_num <= MIN_NUM:
            return -1
        else:
            return search_num

    return -1


def search(min_num, maximum_num, standard_ratio, try_count, win_count):
    while min_num + 1 < maximum_num:
        mid_num = (min_num + maximum_num) / 2
        c_ratio = calc_ratio(try_count + mid_num, win_count + mid_num)

        if c_ratio >= standard_ratio:
            maximum_num = mid_num

        elif c_ratio < standard_ratio:
            min_num = mid_num

    return maximum_num

rl = lambda: sys.stdin.readline()
n = int(rl())
for i in xrange(n):
    try_count, win_count = str(rl()).strip().split(' ')
    print calc(int(try_count), int(win_count))