import sys

conversion = dict()


def define_conversion():
    global conversion
    conversion = {
        "kg": {
            "value": 1,
            "unit": "kg",
            "convert_value": 2.2046,
            "convert_unit": "lb"
        },
        "lb": {
            "value": 2.2046,
            "unit": "lb",
            "convert_value": 0.4536,
            "convert_unit": "kg"
        },
        "l": {
            "value": 1,
            "unit": "l",
            "convert_value": 0.2642,
            "convert_unit": "g"
        },
        "g": {
            "value": 0.2642,
            "unit": "g",
            "convert_value": 3.7854,
            "convert_unit": "l"
        }
    }

define_conversion()

rl = lambda: sys.stdin.readline()
n = int(rl())

result = []
for i in range(n):
    value, unit = str(rl()).strip().split(' ')
    # if unit in mapping:
    #     convert_unit = mapping[unit]
    if unit in conversion:
        entity = conversion[unit]
        converted_value = float(value) * float(entity["convert_value"])
        print "%d %0.4f %s" % ((i + 1), round(converted_value, 4), entity["convert_unit"])