def main():
    # q0 = gcd(30, 24)
    # print('%s' % q0)

    # q1 = gcd(24, 30)
    # print('%s' % q1)

    # q2 = gcd(409119243, 87780243)
    # print('%s' % q2)

    # q3 = gcd(87780243, 409119243)
    # print('%s' % q3)
    getInverse()

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def getInverse():
    for i in range(1, 66):
        inverse = (17 * i) % 66
        print("(%s * %s) m %s = %s" %(17, i, 66, inverse))


if __name__ == '__main__':
    main()

