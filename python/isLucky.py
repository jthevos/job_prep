def sum(ns):
    """Simple sum function taking in a string"""
    total = 0
    for number in ns:
        total += int(number)
    return total

def isLucky(n):
    """
    Ticket numbers usually consist of an even number of digits.
    A ticket number is considered lucky if the sum of the first half of the
    digits is equal to the sum of the second half.

    Given a ticket number n, determine if it's lucky or not.

    
    Here, we want to cast n to a string so we can access its indices.
    We then need to get the halfway point.
    Using slices, we can simply compare both halves.
    """
    str_n = str(n)
    halfway = int(len(str_n)/2)

    return sum(str_n[:halfway]) == sum(str_n[halfway:])
