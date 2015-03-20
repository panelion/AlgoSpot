import sys


dict_number = {
    "zero": {
        "num": 0,
        "spellings": {}
    },
    "one": {
        "num": 1,
        "spellings": {}
    },
    "two": {
        "num": 2,
        "spellings": {}
    },
    "three": {
        "num": 3,
        "spellings": {}
    },
    "four": {
        "num": 4,
        "spellings": {}
    },
    "five": {
        "num": 5,
        "spellings": {}
    },
    "six": {
        "num": 6,
        "spellings": {}
    },
    "seven": {
        "num": 7,
        "spellings": {}
    },
    "eight": {
        "num": 8,
        "spellings": {}
    },
    "nine": {
        "num": 9,
        "spellings": {}
    },
    "ten": {
        "num": 10,
        "spellings": {}
    },
}


def calculate_spellings():
    for str_num in dict_number.keys():
        dict_number[str_num]['spellings'] = count_alphabet(str_num)


def find_number(str_number):
    int_number = -1
    str_number = str(str_number).lower()

    if str_number in dict_number:
        int_number = dict_number[str_number]['num']
    else:
        compare_spellings = count_alphabet(str_number)
        for dict_value in dict_number.values():
            spellings = dict_value['spellings']
            is_contains = True
            for spell in spellings.keys():
                if spell not in compare_spellings or compare_spellings[spell] != spellings[spell]:
                    is_contains = False
                    break

            if is_contains:
                int_number = dict_value['num']
                break

    return int_number


def is_contains(str_number):
    return True if str_number in dict_number else False


def count_alphabet(str_number):
    dict_alphabet = dict()
    for alphabet in str_number:
        if alphabet not in dict_alphabet:
            dict_alphabet[alphabet] = 1
        else:
            dict_alphabet[alphabet] += 1

    return dict_alphabet

calculate_spellings()

rl = lambda: sys.stdin.readline()
n = int(rl())

for i in range(n):
    one_str_number, operator, two_str_number, equals_operator, answer_str_number = str(rl()).strip().split(' ')
    is_correct = False

    if is_contains(one_str_number) and is_contains(two_str_number):
        one_int_number = dict_number[one_str_number]['num']
        two_int_number = dict_number[two_str_number]['num']
        answer_int_number = find_number(answer_str_number)

        if 0 <= one_int_number <= 10 and 0 <= two_int_number <= 10 and 0 <= answer_int_number <= 10:
            real_answer_int_num = 0
            if operator == '+':
                real_answer_int_num = one_int_number + two_int_number
            elif operator == '-':
                real_answer_int_num = one_int_number - two_int_number
            elif operator == '*':
                real_answer_int_num = one_int_number * two_int_number

            if (0 <= real_answer_int_num <= 10) and real_answer_int_num == answer_int_number:
                is_correct = True

    if is_correct:
        print "Yes"
    else:
        print "No"