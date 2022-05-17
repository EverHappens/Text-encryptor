import sys
import argparse
import string
from collections import Counter

alphabet_size = 26
digit_size = 10
cyrillic_size = 33
uppercase_start = 65
lowercase_start = 97
digit_start = 48
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digit = '0123456789'
upper_cyrillic = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
lower_cyrillic = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'


def caesar_shift(orig_text, shift):
    shift = int(shift)
    cipher_text = ''
    for line in orig_text:
        new_line = ''
        for character in line:
            new_char = character
            if character in upper:
                new_char = chr(
                    uppercase_start + (ord(character) - uppercase_start + alphabet_size + shift) % alphabet_size)
            elif character in lower:
                new_char = chr(
                    lowercase_start + (ord(character) - lowercase_start + alphabet_size + shift) % alphabet_size)
            elif character in digit:
                new_char = chr(digit_start + (ord(character) - digit_start + alphabet_size + shift) % digit_size)
            new_line = ''.join([new_line, new_char])
        cipher_text = ''.join([cipher_text, new_line])
    return cipher_text


def vigenere_shift(orig_text, key, way):
    cipher_text = ''
    for line in orig_text:
        new_line = ''
        for i in range(len(line)):
            new_char = line[i]
            if line[i] != ' ':
                if line[i] in upper:
                    new_char = chr(uppercase_start + (alphabet_size + ord(line[i]) - uppercase_start + (
                            (ord(key[i % len(key)]) - uppercase_start) * way)) % alphabet_size)
                elif line[i] in lower:
                    new_char = chr(lowercase_start + (alphabet_size + ord(line[i]) - lowercase_start + (
                            (ord(key[i % len(key)]) - lowercase_start) * way)) % alphabet_size)
                elif line[i] in digit:
                    new_char = chr(digit_start + (digit_size + ord(line[i]) - digit_start + (
                            (ord(key[i % len(key)]) - digit_start) * way)) % digit_size)
                elif line[i] in lower_cyrillic:
                    new_char = lower_cyrillic[(cyrillic_size + i + lower_cyrillic.index(line[i]) * way) % cyrillic_size]
                elif line[i] in upper_cyrillic:
                    new_char = upper_cyrillic[(cyrillic_size + i + upper_cyrillic.index(line[i]) * way) % cyrillic_size]
            new_line = ''.join([new_line, new_char])
        cipher_text = ''.join([cipher_text, new_line])
    return cipher_text


def encode(cipher, orig_text, key):
    cipher_text = ''
    if args.cipher == 'caesar':
        try:
            cipher_text = caesar_shift(orig_text, key)
        except TypeError:
            raise TypeError('Key must be an integer')
    elif cipher == 'vigenere':
        try:
            cipher_text = vigenere_shift(orig_text, key, 1)
        except:
            raise RuntimeError('Vigenere encode function error')
    return cipher_text


def decode(cipher, orig_text, key):
    cipher_text = ''
    if cipher == 'caesar':
        try:
            cipher_text = caesar_shift(orig_text, -key)
        except:
            raise TypeError('Key must be an integer')
    elif cipher == 'vigenere':
        try:
            cipher_text = vigenere_shift(orig_text, key, -1)
        except:
            raise RuntimeError('Vigenere decode function error')
    return cipher_text


def difference(orig_text):
    letter_frequency = Counter({'e': 12.7, 't': 9.06, 'a': 8.17, 'o': 7.51, 'i': 6.97, 'n': 6.75, 's': 6.33, 'h': 6.09,
                                'r': 5.99, 'd': 4.25, 'l': 4.03, 'c': 2.78, 'u': 2.76, 'm': 2.41, 'w': 2.36, 'f': 2.23,
                                'g': 2.02, 'y': 1.97, 'p': 1.93, 'b': 1.29, 'v': 0.98, 'k': 0.77, 'j': 0.15, 'x': 0.15,
                                'q': 0.10, 'z': 0.07})
    length = len(orig_text)
    counter = Counter(orig_text)
    return sum(
        [100 * abs(counter.get(letter, 0) / length) - letter_frequency[letter] for letter in
         orig_text.lower()]) / alphabet_size


def hack_caesar(orig_text):
    best_text = orig_text
    best_difference = difference(''.join(orig_text))
    for i in range(1, 26):
        new_text = caesar_shift(orig_text, i)
        new_difference = difference(new_text)
        if best_difference > new_difference:
            best_text = new_text
            best_difference = new_difference
    return ''.join(best_text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='option')
    parser_encode = subparser.add_parser('encode')
    parser_encode.add_argument('--cipher', choices=['caesar', 'vigenere'], required=True)
    parser_encode.add_argument('--key', required=True)
    parser_decode = subparser.add_parser('decode')
    parser_decode.add_argument('--cipher', choices=['caesar', 'vigenere'], required=True)
    parser_decode.add_argument('--key', required=True)
    parser_hack = subparser.add_parser('hack')
    parser.add_argument('--input-file', dest='input_file', default='input.txt')
    parser.add_argument('--output-file', dest='output_file', default='output.txt')
    args = parser.parse_args()
    with open(args.input_file) as input_file:
        orig_text = input_file.readlines()
    cipher_text = ''
    if args.option == 'encode':
        cipher_text = encode(args.cipher, orig_text, args.key)
    elif args.option == 'decode':
        cipher_text = decode(args.cipher, orig_text, args.key)
    elif args.option == 'hack':
        cipher_text = hack_caesar(orig_text)
    with open(args.output_file, 'w') as output_file:
        orig_stdout = sys.stdout
        output_file.write(cipher_text)
