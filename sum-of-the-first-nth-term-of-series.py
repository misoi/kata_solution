"""
Task:

Your task is to write a function which returns the sum of following series upto nth term(parameter).

Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
Rules:

You need to round the answer upto 2 decimal places and return it as String.
If the given value is 0 then it should return 0.00
You will only be given Natural Numbers as arguments.
"""

def series_sum(n):
    return "{:..}".format(sum([1.0/(1+i*3) for i in range(n)]))

#Test.assert_equals(series_sum(1), "1.00")
#Test.assert_equals(series_sum(2), "1.25")
#Test.assert_equals(series_sum(3), "1.39")
