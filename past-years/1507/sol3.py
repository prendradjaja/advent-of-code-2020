# This is really just a cleaned-up version of sol2 that doesn't
# require manually editing the input file

import re, sys

f = open(sys.argv[1])
lines = []

for line in f:
    line = (line
        .strip()
        .replace('->', '=')
        .replace('AND', '&')
        .replace('OR', '|')
        .replace('LSHIFT', '<<')
        .replace('RSHIFT', '>>')
        .replace('NOT', '65535 -'))
    # Some of the wire identifiers are Python keywords (e.g. `in`),
    # so add a prefix to make sure they're all valid Python
    # identifiers
    line = re.sub(r'([a-z]+)', r'var_\1', line)
    line = ' = '.join(reversed(line.split(' = ')))
    lines.append(line)

while lines:
    for line in lines[:]:
        try:
            exec(line)
            lines.remove(line)
        except NameError:
            pass

print(var_a)
