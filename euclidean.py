import time


def main():
    factors = []
    num1, num2 = input("ENTER 2 NUMBERS TO FIND GCD (FORMAT => NUM1<SPACE>NUM2)\n").split()
    num2 = int(num2)
    big = int(num1)
    small = int(num2)
    if num2 > big:
        big = num2
        small = num1
    start_time = time.perf_counter()
    gcd = eudi(big, small, factors)
    end_time = time.perf_counter()
    total_time = "{:.20f}".format(end_time - start_time)

    print(f'greatest common factor of {big} and {small} is \n{gcd}\nexecution time {total_time}')


def eudi(a, b, factors):
    a = int(a)
    b = int(b)
    q = int(a / b)
    r = a - b * q
    if r != 0:
        factors.append(r)
        print(b, r)
        return eudi(b, r, factors)
    else:
        return factors[-1]


if __name__ == "__main__":
    main()
