################################################################
# http://en.wikipedia.org/wiki/Eight_queens_puzzle
# http://en.wikipedia.org/wiki/Bitwise_operation
# https://helloacm.com/n-queen-problem-in-back-tracing-bit-logics/
################################################################

import sys


"""
    Number of Queens : 5

    Queen's position : 0b11111, left to right : 0b11111000, right to left : 0b110
    Queen's position : 0b11111, left to right : 0b11111000, right to left : 0b110
    Queen's position : 0b11111, left to right : 0b11111000, right to left : 0b1001
    Queen's position : 0b11111, left to right : 0b101110100, right to left : 0b101
    Queen's position : 0b11111, left to right : 0b11111000, right to left : 0b1001
    Queen's position : 0b11111, left to right : 0b110110010, right to left : 0b11
    Queen's position : 0b11111, left to right : 0b101110100, right to left : 0b101
    Queen's position : 0b11111, left to right : 0b110110010, right to left : 0b11
    Queen's position : 0b11111, left to right : 0b1001101100, right to left : 0b11
    Queen's position : 0b11111, left to right : 0b1001101100, right to left : 0b11

    Total Count : 10
"""
def queen(bit_number_of_queens, bit_where_is_queens, left_to_right_diagonal, right_to_left_diagonal):
    if bit_where_is_queens == bit_number_of_queens:
        print "Queen's position : {0}, left to right : {1}, right to left : {2}"\
            .format(bin(bit_where_is_queens), bin(left_to_right_diagonal), bin(right_to_left_diagonal))
        return 1

    bit_positions = bit_number_of_queens & (~(bit_where_is_queens | left_to_right_diagonal | right_to_left_diagonal))

    answer_count = 0

    while bit_positions != 0:
        p = bit_positions & (-bit_positions)
        bit_positions -= p
        answer_count += queen(bit_number_of_queens,
                              bit_where_is_queens + p,
                              (left_to_right_diagonal + p) << 1,
                              (right_to_left_diagonal + p) >> 1)

    return answer_count


def run(number_of_queens):
    # if n is 12, LIM is 111111111111 ( (1 << n) - 1 )
    bit_values = (1 << number_of_queens) - 1
    print queen(bit_values, 0, 0, 0)


rl = lambda: sys.stdin.readline()
n = int(rl())

for i in range(n):
    n = int(rl())
    run(n)

# import cProfile
# cProfile.run('run(5)')