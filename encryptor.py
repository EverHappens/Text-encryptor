# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys
from getopt import getopt
import argparse


def encode(args):
    upper = {ascii: chr(ascii) for ascii in range(65, 91)}
    lower = {ascii: chr(ascii) for ascii in range(97, 123)}
    digit = {ascii: chr(ascii) for ascii in range(48, 58)}
    with open(args.input_file) as input_file:
        orig_text = input_file.readlines()
        cipher_text = []
        if args.cipher == 'caesar':
            try:
                shift = int(args.key)
                for line in orig_text:
                    new_line = ''
                    for character in line:
                        char = ord(character)
                        new_char = character
                        if char in upper:
                            new_char = chr(65 + (char - 65 + shift) % 26)
                        elif char in lower:
                            new_char = chr(97 + (char - 97 + shift) % 26)
                        elif char in digit:
                            new_char = chr(48 + (char - 48 + shift) % 10)
                        new_line += new_char
                    cipher_text.append(new_line)
                with open(args.output_file, 'w') as output_file:
                    orig_stdout = sys.stdout
                    for line in cipher_text:
                        output_file.write(line)
                    output_file.close()
            except:
                raise TypeError('Key must be an integer')
        elif args.cipher == 'vigenere':
            key = args.key
            for line in orig_text:
                new_line = ''
                for i in range(len(line)):
                    new_char = line[i]
                    if line[i] != ' ':
                        new_char = chr(97 + (ord(line[i]) - 97 + ord(key[i % len(key)]) - 97) % 26)
                    new_line += new_char
                cipher_text.append(new_line)
            with open(args.output_file, 'w') as output_file:
                orig_stdout = sys.stdout
                for line in cipher_text:
                    output_file.write(line)
                output_file.close()
        input_file.close()


def decode(args):
    upper = {ascii: chr(ascii) for ascii in range(65, 91)}
    lower = {ascii: chr(ascii) for ascii in range(97, 123)}
    digit = {ascii: chr(ascii) for ascii in range(48, 58)}
    with open(args.input_file) as input_file:
        orig_text = input_file.readlines()
        cipher_text = []
        if args.cipher == 'caesar':
            try:
                shift = int(args.key)
                for line in orig_text:
                    new_line = ''
                    for character in line:
                        char = ord(character)
                        new_char = character
                        if char in upper:
                            new_char = chr(65 + (char - 65 + 26 - shift) % 26)
                        elif char in lower:
                            new_char = chr(97 + (char - 97 + 26 - shift) % 26)
                        elif char in digit:
                            new_char = chr(48 + (char - 48 + 10 - shift) % 10)
                        new_line += new_char
                    cipher_text.append(new_line)
                with open(args.output_file, 'w') as output_file:
                    orig_stdout = sys.stdout
                    for line in cipher_text:
                        output_file.write(line)
                    output_file.close()
            except:
                raise TypeError('Key must be an integer')
        elif args.cipher == 'vigenere':
            key = args.key
            for line in orig_text:
                new_line = ''
                for i in range(len(line)):
                    new_char = line[i]
                    if line[i] != ' ':
                        new_char = chr(97 + (ord(line[i]) - 97 + 26 - ord(key[i % len(key)]) + 97) % 26)
                    new_line += new_char
                cipher_text.append(new_line)
            with open(args.output_file, 'w') as output_file:
                orig_stdout = sys.stdout
                for line in cipher_text:
                    output_file.write(line)
                output_file.close()
        input_file.close()


parser = argparse.ArgumentParser()
parser.add_argument('option', choices=['encode', 'decode'])
parser.add_argument('--cipher', choices=['caesar', 'vigenere'], required=True)
parser.add_argument('--key', required=True)
parser.add_argument('--input-file', dest='input_file', default='input.txt')
parser.add_argument('--output-file', dest='output_file', default='output.txt')

args = parser.parse_args()

if args.option == 'encode':
    encode(args)
elif args.option == 'decode':
    decode(args)

"""
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
"""
