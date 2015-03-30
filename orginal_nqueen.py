from datetime import datetime
import sys

"""
This is slower than n_queen.py.
"""

arr_index_of_queens = [0 for _ in range(12)]
arr_left_to_right_blocking_diagonal = [0 for _ in range(24)]
arr_right_to_left_blocking_diagonal = [0 for _ in range(24)]


def travelling(int_number_of_queens, current_index):

    if int_number_of_queens == current_index:
        return 1

    total_count = 0

    for queen_index in xrange(int_number_of_queens):

        if arr_index_of_queens[queen_index] == 1:
            continue
        if arr_left_to_right_blocking_diagonal[queen_index + current_index] == 1:
            continue
        if arr_right_to_left_blocking_diagonal[queen_index - current_index + int_number_of_queens] == 1:
            continue

        index_left_diagonal = queen_index + current_index
        index_right_diagonal = queen_index - current_index + int_number_of_queens

        arr_index_of_queens[queen_index] = 1
        arr_left_to_right_blocking_diagonal[index_left_diagonal] = 1
        arr_right_to_left_blocking_diagonal[index_right_diagonal] = 1

        total_count += travelling(int_number_of_queens, current_index + 1)

        arr_index_of_queens[queen_index] = 0
        arr_left_to_right_blocking_diagonal[index_left_diagonal] = 0
        arr_right_to_left_blocking_diagonal[index_right_diagonal] = 0

    return total_count


def run(input_numbers):
    start_time = datetime.now()
    print travelling(input_numbers, 0)
    print "End time : " + str(datetime.now() - start_time)


rl = lambda: sys.stdin.readline()
n = int(rl())

result = []
for i in xrange(n):
    number_of_queens = int(rl())

    # Validation
    if number_of_queens < 1 or number_of_queens > 12:
        continue

    run(number_of_queens)


# import cProfile
# cProfile.run('print run(12)')