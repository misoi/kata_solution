"""
Task:

You have to write a function pattern which creates the following pattern upto n number of rows. If the Argument is 0 or a Negative Integer then it should return "" i.e. empty string.

Pattern:

(n)(n-1)(n-2)...4321
(n)(n-1)(n-2)...432
(n)(n-1)(n-2)...43
(n)(n-1)(n-2)...4
...............
..............
(n)(n-1)(n-2)
(n)(n-1)
(n)
Examples:

pattern(4):

4321
432
43
4
"""

def concat_digits(a, b):
    pow = 10
    while b >= pow:
        pow = pow * 10
    return a*pow + b


def pattern(n):
    return "\n".join([str(reduce(concat_digits, p)) for p in [range(n, i, -1) for i in range(n)]])

print(pattern(5))

print reduce(concat_digits, [5, 4, 3])

assert concat_digits(1, 2) == 12
assert concat_digits(5, 4) == 54
assert concat_digits(54, 3) == 543
assert concat_digits(11, 10) == 1110
assert concat_digits(111, 110) == 111110
