from chinese_remainder_theorem import solve as solve_congruences


def main():
    desired_buses = open('in').read().splitlines()[1]
    answer = solve(desired_buses)
    print(answer)


def solve(desired_buses):
    '''
    >>> solve('7,13,x,x,59,x,31,19')
    1068781
    '''
    congruences = []
    for i, entry in enumerate(desired_buses.split(',')):
        if entry != 'x':
            bus_id = int(entry)
            modulus = bus_id
            value = -i % modulus
            congruences.append( (value, modulus) )
    return solve_congruences(congruences)


if __name__ == '__main__':
    main()
