################## ex1 -- Generate Fib sequence using generator protocol, get U.B./len from user
from pint import UnitRegistry
from math import ceil, sqrt
from collections import Counter


def gen_fib_with_ub():
    N = int(input('Set an inclusive upper bound for generator Fibonacci sequence: '))
    n1, n2 = 0, 1
    while (n1 < N):
        yield n1
        next_fib = n1+n2
        n1, n2 = n2, next_fib

# for num in gen_fib_with_ub():
#     print(num)


def gen_fib_with_len():
    L = int(input('Set the length of the generator Fibonacci sequence: '))
    count, n1, n2 = 0, 0, 1
    while count < L:
        yield n1
        next_fib = n1+n2
        n1, n2 = n2, next_fib
        count += 1

# for num in gen_fib_with_len():
#     print(num)


############### ex2 -- Create decorator to extend multiple call feature onto a function
def make_multi_callable(func):
    def n_calls(n, *argv):
        for _ in range(n):
            func(*argv)
        print(f'{func} was called {n} times.')
    return n_calls


@make_multi_callable
def sum_ab(a, b):
    print(a+b)
#sum_ab(n=5, a=2, b=3)


@make_multi_callable
def say_hello():
    print('hello')
# say_hello(n=10)


########## ex3 -- Read in sample .txt file, find most common word
with open('sample.txt') as f:
    all_text_list = f.read().replace('\n', '').lower().split()
    counts = Counter(all_text_list)
    max_info = counts.most_common(1)[0]
    max_word = max_info[0]
    max_count = max_info[1]
    answer = f'Most frequent word: {max_word}\nFrequency: {max_count}'
    # print(answer)

########## ex4 -- Generate prime numbers until user wishes to stop
def gen_prime():
    num = 2
    while input("Enter 'y' for next prime, or any other key to exit: ") == 'y':
        yield num
        found = False
        while not found:
            found = True
            num += 1
            max_div = int(ceil(sqrt(num))) + 1
            for div in range(2, max_div):
                if num % div == 0:
                    found = False
                    break


# for prime in gen_prime():
#     print(prime)


########### ex6 -- create program to convert user value to specified units (requires install of pint)
from pint import UnitRegistry

def converter():
    ureg = UnitRegistry()
    wants_conversion = True
    while wants_conversion:
        try:
            inp_unit = ureg[input('Enter units of your input: ').rstrip('\n').lower()]
            inp_qnt = float(input('Enter quantity of input unit: ').rstrip('\n'))
            out_unit = ureg[input('Enter desired unit for quantity: ').rstrip('\n').lower()]
            inp = inp_qnt * inp_unit
            out = inp.to(out_unit)
            yield out
        except Exception:
            print('Input(s) are invalid.\n')
        instruction = input('Enter "y" for another conversion, or any other key to exit: ')
        wants_conversion = True if instruction == 'y' else False

# for val in converter():
#     print(f'{val}\n')


############ ex7 -- create program to generate RE pattern matches inputed by a user onto an inputed string
import re

def reg_matcher():
    wants_match = True
    while wants_match:
        try:
            str = input('Enter string: ').rstrip('\n')
            re_str = input('Enter RegEx pattern to match: ').rstrip('\n')
            re.compile(re_str)
            yield re.findall(re_str, str)
        except re.error:
            print('RegEx input is invalid.\n')
        instruction = input('Enter "y" for another RegEx match, or any other key to exit: ')
        wants_match = True if instruction == 'y' else False

# for matches in reg_matcher():
#     print('\nHere are your matches:')
#     for match in matches:
#         print(match)
#     print('\n')
    
