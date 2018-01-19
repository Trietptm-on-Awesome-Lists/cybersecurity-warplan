def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    sentence_list = s.split(" ")
    reverse_sentence = ""
    for word in sentence_list:
        reverse_sentence += word[::-1] + " "
    return reverse_sentence[:-1]

res = reverseWords("Let's take LeetCode contest")
print(res)
