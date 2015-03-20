import sys


def get_divisors(number):
    arr_divisors = [1]
    if 0 < number <= 500000:
        for num in xrange(2, number / 2 + 1):
            if number % num == 0:
                arr_divisors.append(num)

    return arr_divisors


def is_weird(arr_list, index, sum_num, standard_num):
    if sum_num == standard_num:
        return True
    if sum_num < standard_num or standard_num < 0:
        return False

    if is_weird(arr_list, index - 1, sum_num - arr_list[index], standard_num - arr_list[index]):
        return True

    return is_weird(arr_list, index - 1, sum_num - arr_list[index], standard_num)


def sum_subset(arr_subset):
    sum_score = 0
    for subset_num in arr_subset:
        sum_score += int(subset_num)

    return sum_score


rl = lambda: sys.stdin.readline()
n = int(rl())
for i in xrange(n):
    n = int(rl())

    is_wired = False

    divisors = get_divisors(n)
    sum_divisors = int(sum_subset(divisors))

    if sum_divisors > n:
        if not is_weird(divisors, len(divisors) - 1, sum_divisors, n):
            is_wired = True

    if is_wired:
        print "weird"
    else:
        print "not weird"