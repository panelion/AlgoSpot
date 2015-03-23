import sys


arr_start_bracket = {
    '[': ']',
    '{': '}',
    '(': ')'
}

rl = lambda: sys.stdin.readline()
n = int(rl())

if 1 > n or n > 100:
    exit(-1)

for i in xrange(n):
    str_brackets = str(rl()).strip()

    if len(str_brackets) > 10000:
        continue

    stack_start_bracket = []
    is_corrected = True
    for index_bracket in xrange(len(str_brackets)):
        char_bracket = str_brackets[index_bracket]
        if char_bracket in arr_start_bracket.keys():
            stack_start_bracket.append(char_bracket)
        else:
            if len(stack_start_bracket) > 0:
                char_start_bracket = stack_start_bracket.pop()
                if arr_start_bracket[char_start_bracket] != char_bracket:
                    is_corrected = False
                    break
            else:
                is_corrected = False
                break

    if len(stack_start_bracket) > 0:
        is_corrected = False

    if is_corrected:
        print "YES"
    else:
        print "NO"