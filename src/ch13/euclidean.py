
def main():
    q0 = gcd(30, 24)
    print('%s' % q0)

    q1 = gcd(24, 30)
    print('%s' % q1)

    q2 = gcd(409119243, 87780243)
    print('%s' % q2)

    q3 = gcd(87780243, 409119243)
    print('%s' % q3)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    main()

