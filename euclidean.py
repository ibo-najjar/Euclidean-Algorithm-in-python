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
    start_time2 = time.perf_counter()
    gcd2 = normal(big, small)
    end_time2 = time.perf_counter()
    total_time2 = "{:.20f}".format(end_time2 - start_time2)
    print(
        f'greatest common factor of {big} and {small} using the Euclidean algorithm is \n{gcd}\nexecution time {total_time} seconds')
    print(
        f'greatest common factor of {big} and {small} using the GCD function is \n{gcd2}\nexecution time {total_time2} seconds')


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


def normal(x, y):
    gcd = 1
    if x % y == 0:
        return y
    for i in range(int(y / 2), 0, -1):
        if x % i == 0 and y % i == 0:
            gcd = i
            break
    return gcd


if __name__ == "__main__":
    main()
