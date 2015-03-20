import sys

dict_special_character = {
    "%20": " ",
    "%21": "!",
    "%24": "$",
    "%25": "%",
    "%28": "(",
    "%29": ")",
    "%2a": "*"
}

rl = lambda: sys.stdin.readline()
n = int(rl())

for i in range(n):
    str_uri = str(rl()).strip()

    special_character = ""
    result = ""
    for j in str_uri:
        if j == '%' or (0 < len(special_character) < 3):
            special_character += j
            if len(special_character) == 3:
                result += dict_special_character[special_character]
                special_character = ""
        else:
            result += j

    print result