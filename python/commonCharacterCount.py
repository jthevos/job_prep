def unique(s):
    """Return a list of unique elements in s"""
    unique_array = []
    for i in s:
        if i not in unique_array:
            unique_array.append(i)
    return unique_array

def commonCharacterCount(s1, s2):
    """
    The smaller of the two strings will be the limiting factor.
    Thus, we find the unique values in the smaller string.

    Now, we get a count of each time that character occurs in BOTH strings.
    The lesser of the two is how many they have in common.
    """

    common_letters = 0

    if len(s1) < len(s2):
        key = unique(s1)
    else:
        key = unique(s2)

    for character in key:
        ss1 = s1.count(character)
        ss2 = s2.count(character)

        if ss1 < ss2:
            common_letters += ss1
        else:
            common_letters += ss2

    return common_letters
