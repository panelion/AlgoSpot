import sys


symbols = {
    '[': ']',
    '{': '}',
    '(': ')',
    '<': '>'
}


class Symbol:
    start_symbol = ''
    end_symbol = ''
    int_order = 0

    def __init__(self, start_symbol, end_symbol, int_order):
        self.start_symbol = start_symbol
        self.end_symbol = end_symbol
        self.int_order = int_order

    def has_start_symbol(self, start_symbol):
        if self.start_symbol == start_symbol:
            return True

        return False

    def has_end_symbol(self, end_symbol):
        if self.end_symbol == end_symbol:
            return True

        return False

    def get_start_symbol(self):
        return self.start_symbol

    def get_end_symbol(self):
        return self.end_symbol

    def get_order(self):
        return self.int_order


def get_list_of_sequence_order(str_order_sequence):
    symbol_order_list = []
    for s in range(len(str_order_sequence)):
        char_symbol = str_order_sequence[s]
        if char_symbol in symbols.keys():
            symbol_order_list.append(Symbol(char_symbol, symbols[char_symbol], s + 1))

    return symbol_order_list


def find_match_sequence(str_mismatch_sequence, sequence_order_list):
    answer_list = [None for _ in xrange(len(str_mismatch_sequence))]
    stack_sequence = []

    for s in range(len(str_mismatch_sequence)):
        char_symbol = str_mismatch_sequence[s]

        if char_symbol in symbols.keys():
            stack_sequence.append({
                "index": s,
                "char_symbol": str(char_symbol)
            })
        else:
            if len(stack_sequence) > 0:
                s_sequence = stack_sequence.pop()
                start_symbol = None
                end_symbol = None

                for sequence_symbol in sequence_order_list:
                    if sequence_symbol.has_start_symbol(s_sequence['char_symbol']):
                        start_symbol = sequence_symbol
                    if sequence_symbol.has_end_symbol(char_symbol):
                        end_symbol = sequence_symbol

                if start_symbol is not None and end_symbol is not None:
                    if start_symbol.get_order() >= end_symbol.get_order():
                        answer_list[s_sequence['index']] = end_symbol.get_start_symbol()
                        answer_list[s] = end_symbol.get_end_symbol()

                    elif start_symbol.get_order() < end_symbol.get_order():
                        answer_list[s_sequence['index']] = start_symbol.get_start_symbol()
                        answer_list[s] = start_symbol.get_end_symbol()

    return answer_list

rl = lambda: sys.stdin.readline()
n = int(rl())

if 1 > n or n > 100:
    exit(-1)

for i in xrange(n):
    mismatch_sequence, order_sequence = str(rl()).strip().split(' ')

    if len(mismatch_sequence) > 100:
        continue

    if len(order_sequence) != 4:
        continue

    sequence_order_list = get_list_of_sequence_order(order_sequence)
    list_answer = find_match_sequence(mismatch_sequence, sequence_order_list)
    print ''.join(map(str, list_answer))