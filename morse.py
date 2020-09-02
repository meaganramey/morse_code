#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Morse Code Decoder

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
"""
__author__ = 'Meagan Ramey'

from morse_dict import MORSE_2_ASCII
import re


def decode_bits(bits):
    bit_list = re.split(r'([0]+)', bits)
    shortest_len = len(bits)
    for bit in bit_list:
        if bit == '':
            bit_list.remove(bit)
    if '0' in bit_list[0]:
        bit_list.remove(bit_list[0])
    if '0' in bit_list[-1]:
        bit_list.remove(bit_list[-1])
    for bit in bit_list:
        if len(bit) < shortest_len:
            shortest_len = len(bit)
    code_list = []
    for bit in bit_list:
        if bit == '1'*shortest_len:
            code_list.append('.')
        elif bit == '111'*shortest_len:
            code_list.append('-')
        elif bit == '0'*shortest_len:
            code_list.append('')
        elif bit == '000'*shortest_len:
            code_list.append(' ')
        elif bit == '0000000'*shortest_len:
            code_list.append('   ')
    code_string = ''.join(code_list)
    return code_string


def decode_morse(morse):
    morse = morse.strip()
    morse_string = morse.replace(' ', '*')
    morse_list = morse_string.split('***')
    letter_list = []
    phrase = ''
    for code in morse_list:
        characters = code.split('*')
        for char in characters:
            letter_list.append(MORSE_2_ASCII.get(char))
        word = ''.join(letter_list) + ' '
        letter_list = []
        phrase += word
    return phrase.strip()


if __name__ == '__main__':
    hey_jude_morse = ".... . -.--   .--- ..- -.. ."
    hey_jude_bits = "1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011"  # noqa

    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")
    print()
    print("Part B:")
    print(f"'{hey_jude_bits}' -> {decode_morse(decode_bits(hey_jude_bits))}")

    print("\nCompleted.")
