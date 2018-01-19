import random

allowed_chrs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz+/"
base_url = "http://tinyurl.com/"
class Codec:

    def __init__(self):
        self.url_dict = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        random_url_key = ''.join(random.choice(allowed_chrs) for i in range(10))
        self.url_dict[random_url_key] = longUrl
        return base_url+random_url_key

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.url_dict[shortUrl.split("tinyurl.com/")[-1]]

"""

converter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz+/"
print(len(converter))
def convert_to_base(number, base):
    ""
    Convert number to a base
    params: number number to be converted
        base: base to which we will convert
    return converted_number
    ""
    if number == 0:
        return ""
    else:
        return convert_to_base(number//base, base) + converter[number%base]

"""

url = "https://leetcode.com/problems/design-tinyurl"
codec = Codec()
print(codec.decode(codec.encode(url)))
