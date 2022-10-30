'''
The key thought process for part 2 was:

- Understanding the new rules
    8: 42 | 42 8
    11: 42 31 | 42 11 31
  Notice that 42 and 31 are still finite (they can match a finite set of
  messages). So, treating 42 and 31 as black boxes: Rule 8 means "42 at least
  once". Rule 11 means "42 at least once, then 31 at least once (but exactly
  the same number of times as 42)".

- Understanding rule 0
    0: 8 11
  This means "42 at least once, then 31 at least once (but 42 must appear more
  times than 31)".

- We can't just use a regex anymore for rules 8 and 11 (and therefore 0), but
  we still can for 42 and 31 and everything else.
'''

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

    def matches_rule_0(message):
        matches_rule_42, count42, rest = matches_pattern_plus(message, pattern(42))
        if not matches_rule_42:
            return False
        matches_rule_31, count31, rest = matches_pattern_plus(rest, pattern(31))
        return (
            matches_rule_31
            and rest == ''
            and count42 > count31
        )

    matches = 0
    for message in messages:
        if matches_rule_0(message):
            matches += 1
    print(matches)


def matches_pattern_plus(message, pattern):
    '''
    Given a MESSAGE and a PATTERN, (call it p) determine if the message matches
    the pattern /p+/ (i.e. p one or more times).

    This is "matches" in the sense of re.match(), not re.fullmatch(): Look
    from the start of the string, and allow extra characters at the end.

    Returns a tuple:
    (is_match, count_matches, extra_characters)

    >>> matches_pattern_plus('Hello', r'Hello')
    (True, 1, '')
    >>> matches_pattern_plus('HelloHello', r'Hello')
    (True, 2, '')
    >>> matches_pattern_plus('Hello world', r'Hello')
    (True, 1, ' world')
    >>> matches_pattern_plus('HelloHello world', r'Hello')
    (True, 2, ' world')
    >>> matches_pattern_plus('', r'Hello')
    (False, None, None)
    >>> matches_pattern_plus('world', r'Hello')
    (False, None, None)
    >>> matches_pattern_plus('world Hello', r'Hello')
    (False, None, None)
    '''
    count = 0
    while message:
        if match := re.match(pattern, message):
            message = message[match.end():]
            count += 1
        else:
            break
    if count:
        return (True, count, message)
    else:
        return (False, None, None)


if __name__ == '__main__':
    main()
