"""
A simple substitution cipher replaces one character from an alphabet with a character from an alternate alphabet, where each character's position in an alphabet is mapped to the alternate
alphabet for encoding or decoding.

map1 = "abcdefghijklmnopqrstuvwxyz";
map2 = "etaoinshrdlucmfwypvbg"

her = Cipher(map1, map2);
cipher.encode("abc") # => "eta"
cipher.encode("xyz") # => "qxz"
cipher.encode("aeiou") # => "eirfg"

cipher.decode("eta") # => "abc"
cipher.decode("qxz") # => "xyz"
cipher.decode("eirfg") # => "aeiou"

If a character provided is not in the opposing alphabet, simply leave it as be.
"""
from string import maketrans

class Cipher(object):

    def __init__(self, map1, map2):
        self.table = maketrans(map1, map2)
        self.rtable = maketrans(map2, map1)

    def encode(self, string):
        return string.translate(self.table)

    def decode(self, string):
        return string.translate(self.rtable)


def encode(map1, map2, string):
    return "".join(map(lambda x: map2[map1.index(x)] if x in map1 else x, string))

def decode(map1, map2, string):
    return "".join(map(lambda x: map1[map2.index(x)] if x in map2 else x, string))

print(encode("abc", "edf", "a2xc"))
print(decode("abc", "edf", "e2xf"))

map1 = "abcdefghijklmnopqrstuvwxyz";
map2 = "etaoinshrdlucmfwypvbgkjqxz";

from tests import test

cipher = Cipher(map1, map2)
test.assert_equals(cipher.encode("abc"), "eta");
test.assert_equals(cipher.encode("xyz"), "qxz");
test.assert_equals(cipher.decode("eirfg"), "aeiou");
test.assert_equals(cipher.decode("erlang"), "aikcfu");

map2 = 'tfozcivbsjhengarudlkpwqxmy';
cipher = Cipher(map1, map2);
test.assert_equals(cipher.encode('abc'), 'tfo');
test.assert_equals(cipher.decode('tfo'), 'abc');
test.assert_equals(cipher.decode('kjpphi'), 'tjuukf');
test.assert_equals(cipher.encode('ajqqtb'), 'tjuukf');
