#!/usr/bin/python3
import json
import glob
from colorama import Fore, init
import os
import sys

init(autoreset=True)
symbol = '[x]'

def banner():
    print(Fore.RED + '*' * 20)
    print(Fore.RED + 'PrivEsc Grimoire')
    print(Fore.RED + '*' * 20, '\n')

def load_from_file():
        with open('gtfobins.json', 'r') as f:
            pe_dict = json.load(f)
        return pe_dict

def find_pe(pe_dict, bin):
        pe = list(filter(lambda pe: pe['bin'] == bin, pe_dict))
        if len(pe) > 0:
            return pe[0]
        else:
            print(Fore.RED + 'Binary not found')
            return False

# print all the options(funcs names)
def print_funcs(pe):
    print()
    for i in range(0, len(pe['funcs'])):
        print("{} - {}".format(i, pe['funcs'][i]['func']))
    print('\nother keys - all')

def print_manual(i, pe):
    print()
    if type(i) == int and 0 <= i <= len(pe['funcs']) -1:
        print(Fore.RED + pe['funcs'][i]['func'])
        print(pe['funcs'][i]['man'])
    else:
        for p in pe['funcs']:
            print(Fore.RED + p['func'])
            print(p['man'])

# ***************** __main__ *************************
if __name__ == '__main__':
    banner()
    jsonexists = glob.glob('gtfobins.json')
    if not jsonexists:
        print(Fore.RED + symbol, " Can't find file 'gtfobins.json'.")
        download = str(input(Fore.RED + symbol + Fore.RESET + '  Do you want me to download it from https://raw.githubusercontent.com/0xyy66/PrivEsc-Grimoire/main/gtfobins.json?[Y/n] '))
        if download.lower() == 'y':
            print(Fore.RED + symbol, " Downloading...")
            os.system('wget https://raw.githubusercontent.com/0xyy66/PrivEsc-Grimoire/main/gtfobins.json -O gtfobins.json')
        else:
            print(Fore.RED + "Can't work without file gtfobins.json")
            sys.exit(0)
    else:
        print(Fore.RED + symbol, " File 'gtfobins.json' found, proceed to load data")
    pe_dict = load_from_file()
    pe = False
    while not pe:
        bin = str(input('\n' + Fore.RED + symbol + Fore.RESET + "  Binary to find: "))
        pe = find_pe(pe_dict, bin)
    print_funcs(pe)
    func = str(input('\n' + Fore.RED + symbol + Fore.RESET + '  Enter index: '))
    try:
        func = int(func)
    except ValueError:
        func = 'all'
    print_manual(func, pe)
