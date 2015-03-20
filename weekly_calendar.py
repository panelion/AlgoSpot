import sys


day_of_week = {
    "Sunday":       0,
    "Monday":       1,
    "Tuesday":      2,
    "Wednesday":    3,
    "Thursday":     4,
    "Friday":       5,
    "Saturday":     6
}

month_end_day = {
    "1": 31,
    "2": 28,
    "3": 31,
    "4": 30,
    "5": 31,
    "6": 30,
    "7": 31,
    "8": 31,
    "9": 30,
    "10": 31,
    "11": 30,
    "12": 31,
}


def get_last_month_end_day(str_this_month):
    if str_this_month == '1':
        return month_end_day['12']

    return month_end_day[str(int(str_this_month) - 1)]

rl = lambda: sys.stdin.readline()
n = int(rl())

for i in xrange(n):
    str_month, str_day, str_day_of_week = str(rl()).strip().split(' ')

    index_day_of_week = -1
    if str_day_of_week in day_of_week:
        index_day_of_week = day_of_week[str_day_of_week]

    int_month_end_day = -1
    if str_month in month_end_day:
        int_month_end_day = month_end_day[str_month]

    week_start_day = int(str_day) - index_day_of_week

    int_last_month_end_day = -1
    if week_start_day <= 0:
        int_last_month_end_day = get_last_month_end_day(str_month)

    arr_week = []
    tomorrow = 0
    for j in xrange(week_start_day, week_start_day + 7, 1):
        if j <= 0:
            tomorrow = int_last_month_end_day - abs(j)
        else:
            tomorrow = j
            if tomorrow > int_month_end_day:
                tomorrow = tomorrow - int_month_end_day

        arr_week.append(tomorrow)

    print ' '.join([str(e) for e in arr_week])