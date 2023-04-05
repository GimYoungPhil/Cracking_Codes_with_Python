import cryptomath

def main():
    q0 = cryptomath.gcd(24, 32)
    print('%s' % q0)

    q1 = cryptomath.gcd(37, 41)
    print('%s' % q1)

    q2 = cryptomath.findModInverse(7, 26)
    print('%s' % q2)

    q3 = cryptomath.findModInverse(8953851, 26)
    print('%s' % q3)


if __name__ == '__main__':
    main()

