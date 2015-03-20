import sys


def get_avg_minimum_rent_cost(rent_days, team_count, arr_rent_cost):
    min_avg = 100.0
    for day in xrange(int(rent_days) - team_count + 1):
        arr_sum = sum(arr_rent_cost[day:day + team_count - 1])
        arr_count = float(team_count - 1)
        for rent_day in xrange(day + team_count - 1, rent_days, 1):
            arr_sum += arr_rent_cost[rent_day]
            arr_count += 1.0
            calc_avg = arr_sum / arr_count
            if min_avg > calc_avg:
                min_avg = calc_avg

    return min_avg


rl = lambda: sys.stdin.readline()
n = int(rl())
for i in xrange(n):
    rent_days, team_count = str(rl()).strip().split(' ')
    arr_rent_cost = map(int, str(rl()).strip().split(' '))
    print "%.10f" % get_avg_minimum_rent_cost(int(rent_days), int(team_count), arr_rent_cost)