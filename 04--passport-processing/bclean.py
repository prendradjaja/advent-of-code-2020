import fileinput
import re

ports = []
port = set()

def h(v):
    if 'cm' in v:
        n, r = v.split('cm', maxsplit=1)
        return r == '' and 150 <= int(n) <= 193
    if 'in' in v:
        n, r = v.split('in', maxsplit=1)
        return r == '' and 59 <= int(n) <= 76
    return False


def validate(pair):
    key, value = pair.split(':')
    if key == 'byr':
        return len(value) == 4 and 1920 <= int(value) <= 2002
    if key == 'iyr':
        return len(value) == 4 and 2010 <= int(value) <= 2020
    if key == 'eyr':
        return len(value) == 4 and 2020 <= int(value) <= 2030
    if key == 'hgt':
        return h(value)
    if key == 'hcl':
        return re.fullmatch(r'#[0-9a-f]{6}', value)
    if key == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth',]
    if key == 'pid':
        return re.fullmatch(r'[0-9]{9}', value)
    if key == 'cid':
        return True

for line in fileinput.input():
    line = line.strip()
    if not line:
        ports.append(port)
        port = set()
    else:
        pairs = line.split(' ')
        for pair in pairs:
            key = pair.split(':')[0]
            if validate(pair):
                port.add(key)

def valid(p):
    p = set(p)
    p.add('cid')
    p.remove('cid')
    return len(p) == 7

print(len(list(x for x in ports if valid(x))))
