def main():
    gcd(409119243, 87780243)

SYMBOLS = 'ABCDEFGHIJKLMNOP'
al = 'abcdefghijklmnopqrstuvwxyz'

def test():
    key = 15
    for i in range(len(SYMBOLS)):
        print('%s * %s = %s, (mod 16: %s)' % (i, key, i * key, (i * key) % 16))

def test2():
    for i in range(2, 26):
        g = gcd(26, i)
        print('gcd(%s, %s) = %s' % (26, i, g))

def gcd(a, b):
    while b != 0:
        print('gcd(%s, %s)' % (a, b))
        a, b = b, a % b
    print('gcd(%s, %s)' % (a, b))
    return a

if __name__ == '__main__':
    main()
