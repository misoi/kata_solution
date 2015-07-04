"""
Task:

You have to write a function pattern which creates the following pattern(See Examples) upto desired number of rows.

If the Argument is 0 or a Negative Integer then it should return "" i.e. empty string.
Examples:

pattern(9):

123456789
234567891
345678912
456789123
567891234
678912345
789123456
891234567
912345678

pattern(5):

12345
23451
34512
45123
51234
Note: There are no spaces in the pattern
"""

def _roate(i, b):
    x = i % b
    if x == 0:
        return b
    return x

def pattern(n):
    # Happy Coding ^_
    if n <= 0:
        return ""
    return "\n".join(["".join([str(_roate(i+j, n)) for j in range(n)]) for i in range(1, n+1)])


def pattern2(n):
    li = map(str, range(1, n+1))
    return "\n".join("".join(li[i:] + li[:i]) for i in range(n))


print pattern2(5)
