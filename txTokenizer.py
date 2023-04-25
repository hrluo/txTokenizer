#usage: python script.py body.txt name.txt list1.txt list2.txt list3.txt list4.txt list5.txt list6.txt list7.txt list8.txt list9.txt list10.txt
#python txTokenizer.py "body.txt" "name.txt" "list1.txt" "list2.txt" "list3.txt" "list4.txt" "list5.txt" "list6.txt" "list7.txt" "list8.txt" "list9.txt" "list10.txt"

import os
import subprocess
import argparse
import glob
import re

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

def replace_tokens(body, tokens):
    for i, token in enumerate(tokens, 1):
        body = body.replace(f'[[token{i}]]', token)
    return body

def write_latex_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

def compile_latex(filename):
    subprocess.run(['pdflatex', filename])

def main(args):
    # Read input files
    body = read_file(args.body)
    print(body)
    names = read_file(args.name)
    lists = [read_file(lst) for lst in args.list_files]

    # Check the number of tokens
    body_str = ''.join(body)  # Convert the list into a single string
    tokens = re.findall(r'\[\[token\d+\]\]', body_str)
    tokens_count = len(set(tokens))

    if tokens_count != len(args.list_files):
        print('The number of tokens in body.txt',tokens_count)    
        print('the number of list*.txt files.',len(args.list_files))
        print("Error: The number of tokens in 'body.txt' does not match the number of 'list*.txt' files.")
        return

    if len(names) != len(lists[0]):
        print("Error: The number of names in 'name.txt' does not match the number of rows in 'list*.txt' files.")
        return

    # Process and generate output files
    for i, name in enumerate(names):
        tokens = [lst[i] for lst in lists]
        new_body = replace_tokens(body_str, tokens)
        filename = f'body_{name}.tex'
        write_latex_file(filename, new_body)
        #compile_latex(filename)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process template and replace tokens.')
    parser.add_argument('body', help='Body template file')
    parser.add_argument('name', help='Names file')
    parser.add_argument('list_files', nargs='+', help='List of files containing token values')
    args = parser.parse_args()
    print(args)
    main(args)

