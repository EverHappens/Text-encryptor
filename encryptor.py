import sys
from getopt import getopt
import argparse

alphabet_size = 26
digit_size = 10
uppercase_start = 65
lowercase_start = 97
digit_start = 48
upper = ascii.uppercase
lower = ascii.lowercase
digit = ascii.digit
cyrillic = "А,Б,В,Г,Д,Е,Ё,Ж,З,И,Й,К,Л,М,Н,О,П,Р,С,Т,У,Ф,Х,Ц,Ч,Ш,Щ,Ъ,Ы,Ь,Э,Ю,Я"
upper_cyrillic = cyrillic.split(',')
lower_cyrillic = cyrillic.lower().split(',')


def caesar_shift(text, shift):
    shift = int(args.key)
    cipher_text = ''
    for line in orig_text:
        new_line = ''
        for character in line:
            char = ord(character)
            new_char = character
            if char in upper:
                new_char = chr(uppercase_start + (char - uppercase_start + alphabet_size + shift) % alphabet_size)
            elif char in lower:
                new_char = chr(lowercase_start + (char - lowercase_start + alphabet_size + shift) % alphabet_size)
            elif char in digit:
                new_char = chr(digit_start + (char - digit_start + alphabet_size + shift) % digit_size)
            new_line += new_char
        cipher_text.append(new_line)
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
                elif line[u] in upper_cyrillic:
                    new_char = upper_cyrillic[(cyrillic_size + i + upper_cyrillic.index(line[i]) * way) % cyrillic_size]
                new_line.join(new_char)
        cipher_text.append(new_line)
    return cipher_text


def encode(cipher, orig_text, key):
    cipher_text = []
    if args.cipher == 'caesar':
        try:
            cipher_text = caesar_shift(orig_text, key)
        except:
            raise TypeError('Key must be an integer')
    elif cipher == 'vigenere':
        try:
            cipher_text = vigenere_shift(orig_text, key, 1)
        except:
            raise RuntimeError('Vigenere encode function error')
    return cipher_text


def decode(cipher, orig_text, key):
    cipher_text = []
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
    letter_frequency = {'e': 12.7, 't': 9.06, 'a': 8.17, 'o': 7.51, 'i': 6.97, 'n': 6.75, 's': 6.33, 'h': 6.09,
                        'r': 5.99, 'd': 4.25, 'l': 4.03, 'c': 2.78, 'u': 2.76, 'm': 2.41, 'w': 2.36, 'f': 2.23,
                        'g': 2.02, 'y': 1.97, 'p': 1.93, 'b': 1.29, 'v': 0.98, 'k': 0.77, 'j': 0.15, 'x': 0.15,
                        'q': 0.10, 'z': 0.07}
    length = len(orig_text)
    counter = Counter(orig_text)
    return sum(
        [100 * abs(counter.get(letter, 0) / length) - letter_frequency[letter] for letter in orig_text]) / alphabet_size


def hack_caesar(orig_text):
    best_text = orig_text
    orig_text = input_file.readlines()
    best_difference = difference(cipher_text)
    for i in range(25):
        # shift
        new_text = caesar_shift(cipher_text, 1)
        new_difference = difference(new_text)
        if best_difference > new_difference:
            best_text = new_text
            best_difference = new_difference
    return best_text


if __name == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('option', choices=['encode', 'decode', 'hack'])
    parser.add_argument('--cipher', choices=['caesar', 'vigenere'], required=True)
    parser.add_argument('--key', required=True)
    parser.add_argument('--input-file', dest='input_file', default='input.txt')
    parser.add_argument('--output-file', dest='output_file', default='output.txt')
    args = parser.parse_args()
    with open(args.input_file) as input_file:
        orig_text = input_file.readlines()
        if args.option == 'encode':
            cipher_text = encode(args.cipher, orig_text, args.key)
        elif args.option == 'decode':
            cipher_text = decode(args.cipher, orig_text, args.key)
        elif args.option == 'hack':
            cipher_text = hack(args.cipher, orig_text, args.key)
            with open(args.output_file) as output_file:
                orig_stdout = sys.stdout
                for line in cipher_text:
                    output_file.write(line)
                output_file.close()
    input_file.close()
import sys
from getopt import getopt
import argparse

alphabet_size = 26
digit_size = 10
uppercase_start = 65
lowercase_start = 97
digit_start = 48
upper = ascii.uppercase
lower = ascii.lowercase
digit = ascii.digit
cyrillic = "А,Б,В,Г,Д,Е,Ё,Ж,З,И,Й,К,Л,М,Н,О,П,Р,С,Т,У,Ф,Х,Ц,Ч,Ш,Щ,Ъ,Ы,Ь,Э,Ю,Я"
upper_cyrillic = cyrillic.split(',')
lower_cyrillic = cyrillic.lower().split(',')


def caesar_shift(text, shift):
    shift = int(args.key)
    cipher_text = ''
    for line in orig_text:
        new_line = ''
        for character in line:
            char = ord(character)
            new_char = character
            if char in upper:
                new_char = chr(uppercase_start + (char - uppercase_start + alphabet_size + shift) % alphabet_size)
            elif char in lower:
                new_char = chr(lowercase_start + (char - lowercase_start + alphabet_size + shift) % alphabet_size)
            elif char in digit:
                new_char = chr(digit_start + (char - digit_start + alphabet_size + shift) % digit_size)
            new_line += new_char
        cipher_text.append(new_line)
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
                elif line[u] in upper_cyrillic:
                    new_char = upper_cyrillic[(cyrillic_size + i + upper_cyrillic.index(line[i]) * way) % cyrillic_size]
                new_line.join(new_char)
        cipher_text.append(new_line)
    return cipher_text


def encode(cipher, orig_text, key):
    cipher_text = []
    if args.cipher == 'caesar':
        try:
            cipher_text = caesar_shift(orig_text, key)
        except:
            raise TypeError('Key must be an integer')
    elif cipher == 'vigenere':
        try:
            cipher_text = vigenere_shift(orig_text, key, 1)
        except:
            raise RuntimeError('Vigenere encode function error')
    return cipher_text


def decode(cipher, orig_text, key):
    cipher_text = []
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
    letter_frequency = {'e': 12.7, 't': 9.06, 'a': 8.17, 'o': 7.51, 'i': 6.97, 'n': 6.75, 's': 6.33, 'h': 6.09,
                        'r': 5.99, 'd': 4.25, 'l': 4.03, 'c': 2.78, 'u': 2.76, 'm': 2.41, 'w': 2.36, 'f': 2.23,
                        'g': 2.02, 'y': 1.97, 'p': 1.93, 'b': 1.29, 'v': 0.98, 'k': 0.77, 'j': 0.15, 'x': 0.15,
                        'q': 0.10, 'z': 0.07}
    length = len(orig_text)
    counter = Counter(orig_text)
    return sum(
        [100 * abs(counter.get(letter, 0) / length) - letter_frequency[letter] for letter in orig_text]) / alphabet_size


def hack_caesar(orig_text):
    best_text = orig_text
    orig_text = input_file.readlines()
    best_difference = difference(cipher_text)
    for i in range(25):
        # shift
        new_text = caesar_shift(cipher_text, 1)
        new_difference = difference(new_text)
        if best_difference > new_difference:
            best_text = new_text
            best_difference = new_difference
    return best_text


if __name == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('option', choices=['encode', 'decode', 'hack'])
    parser.add_argument('--cipher', choices=['caesar', 'vigenere'], required=True)
    parser.add_argument('--key', required=True)
    parser.add_argument('--input-file', dest='input_file', default='input.txt')
    parser.add_argument('--output-file', dest='output_file', default='output.txt')
    args = parser.parse_args()
    with open(args.input_file) as input_file:
        orig_text = input_file.readlines()
        if args.option == 'encode':
            cipher_text = encode(args.cipher, orig_text, args.key)
        elif args.option == 'decode':
            cipher_text = decode(args.cipher, orig_text, args.key)
        elif args.option == 'hack':
            cipher_text = hack(args.cipher, orig_text, args.key)
            with open(args.output_file) as output_file:
                orig_stdout = sys.stdout
                for line in cipher_text:
                    output_file.write(line)
                output_file.close()
    input_file.close()
