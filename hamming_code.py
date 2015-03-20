import sys

first_check_bit_index = [0, 2, 4, 6]
second_check_bit_index = [1, 2, 5, 6]
third_check_bit_index = [3, 4, 5, 6]

decode_bit_index = [2, 4, 5, 6]


def xor(arr_bits, arr_index):
    count_one_bit = 0
    for i in arr_index:
        if int(arr_bits[i]) == 1:
            count_one_bit += 1

    return 1 if count_one_bit % 2 == 1 else 0


def find_corrupted_bit_index(arr_bits):
    first_xor_value = xor(arr_bits, first_check_bit_index)
    second_xor_value = xor(arr_bits, second_check_bit_index)
    third_xor_value = xor(arr_bits, third_check_bit_index)

    return ((third_xor_value * 2 ** 2) + (second_xor_value * 2) + first_xor_value) - 1


def get_corrected_bits(arr_bits):
    corrupted_bit_index = find_corrupted_bit_index(arr_bits)

    if corrupted_bit_index in decode_bit_index:
        if int(arr_bits[corrupted_bit_index]) == 1:
            arr_bits = arr_bits[:corrupted_bit_index] + "0" + arr_bits[corrupted_bit_index + 1:]
        else:
            arr_bits = arr_bits[:corrupted_bit_index] + "1" + arr_bits[corrupted_bit_index + 1:]

    decoded_message = ''
    for bit_index in decode_bit_index:
        decoded_message += arr_bits[bit_index]

    return decoded_message
