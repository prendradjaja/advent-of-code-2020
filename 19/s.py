import sys
import re
import functools
from util import ints


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    rules_section, messages_section = f.read().split('\n\n')
    rules_lines = [l.rstrip('\n') for l in rules_section.split('\n')]
    messages = [l.rstrip('\n') for l in messages_section.split('\n')]

    rules = {}
    for line in rules_lines:
        idx, rule = line.split(': ')
        idx = int(idx)
        rules[idx] = rule

    @functools.cache
    def pattern(idx):
        rule = rules[idx]
        if '"' in rule:
            return rule.strip('"')
        else:
            parts = [*ints(rule.split(' '))]
            result = ''
            for each in parts:
                if each == '|':
                    result += '|'
                else:
                    result += '(' + pattern(each) + ')'
            return result

    matches = 0
    for message in messages:
        if re.fullmatch(pattern(0), message):
            matches += 1
    print(matches)


if __name__ == '__main__':
    main()
