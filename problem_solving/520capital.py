def detectCapitalUse(word):
    """
    :type word: str
    :rtype: bool
    """
    is_correct = True
    is_upper = word[0].isupper()
    if is_upper:
        new_word = word[1:]
        is_upper = None
    else:
        new_word = word

    for w in new_word:
        new_upper = w.isupper()

        if is_upper != new_upper and is_upper is not None:
            is_correct = False
            break

        is_upper = new_upper

    return is_correct
