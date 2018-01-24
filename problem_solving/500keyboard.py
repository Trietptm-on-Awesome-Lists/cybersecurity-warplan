def findWords(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    keyboard = {"r1":"qwertyuiop","r2":"asdfghjkl","r3":"zxcvbnm"}

    letter_dictionary = {}

    for a in range(ord("a"),ord("z") + 1):
        for row in ["r1","r2","r3"]:
            if chr(a) in keyboard[row]:
                letter_dictionary[chr(a)] = row


    list_of_onerow_words = []
    for word in words:
        acceptable = None
        add = True
        for w in word:
            if acceptable is None:
                acceptable = letter_dictionary[w.lower()]
            elif letter_dictionary[w.lower()] != acceptable:
                add = False
                break

        if add:
            list_of_onerow_words.append(word)

    return list_of_onerow_words



w = ["Hello", "Alaska", "Dad", "Peace"]
res = findWords(w)
print(res)
