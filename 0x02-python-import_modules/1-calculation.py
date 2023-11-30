#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    addition_result = add(a, b)
    subtraction_result = sub(a, b)
    multiplication_result = mul(a, b)
    division_result = div(a, b)

    print("{:d} + {:d} = {:d}".format(a, b, addition_result))
    print("{:d} - {:d} = {:d}".format(a, b, subtraction_result))
    print("{:d} * {:d} = {:d}".format(a, b, multiplication_result))
    print("{:d} / {:d} = {:d}".format(a, b, division_result))
