def find_max_chars(inputArray):
    max = 0
    for entry in inputArray:
        if len(entry) > max:
            max = len(entry)

    return max

def allLongestStrings(inputArray):

    array = []
    max_chars = find_max_chars(inputArray)

    for entry in inputArray:
        if len(entry) == max_chars:
            array.append(entry)

    return array
