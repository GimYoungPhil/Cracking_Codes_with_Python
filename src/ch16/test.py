def main():
    result = factorial(26)

    print('%s! = %s' % (26, result))


def factorial(value):
    if value <= 1:
        return 1
    
    result = 1
    for i in range(1, value + 1):
        result *= i

    return result

if __name__ == '__main__':
    main()
