def main():
    factors = []
    num1, num2 = input("ENTER 2 NUMBERS TO FIND GCD (FORMAT => NUM1<SPACE>NUM2)\n").split()
    num2 = int(num2)
    big = int(num1)
    small = int(num2)
    if num2 > big:
        big = num2
        small = num1
    gcd = euclidean(big, small, factors)
    print(f'greatest common factor of {big} and {small} is \n{gcd}')


def euclidean(a, b, factors):
    q = int(a / b)
    r = a - b * q
    if r != 0:
        factors.append(r)
        print(b, r)
        return euclidean(b, r, factors)
    else:
        return factors[-1]


if __name__ == "__main__":
    main()
