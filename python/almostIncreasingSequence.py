def first_bad_pair(sequence):
    """Return the first index of a pair of elements where the earlier
    element is not less than the later elements. If no such pair
    exists, return -1."""
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            return i
    return -1

def almostIncreasingSequence(sequence):
    """Return whether it is possible to obtain a strictly increasing
    sequence by removing no more than one element from the array."""

    j = first_bad_pair(sequence)

    if j == -1:
        return True  # List is increasing

    # We know from j that all pairs before j are okay
    # Thus, we can only pass the REMAINING values from j-1:j
    # and then j+1 to end

    if first_bad_pair(sequence[j-1:j] + sequence[j+1:]) == -1:
        return True  # Deleting earlier element makes increasing

    # If deleting the first does not work, we need to check the
    # latter item. We do this with j:j+1 to j+2:
    if first_bad_pair(sequence[j:j+1] + sequence[j+2:]) == -1:
        return True  # Deleting later element makes increasing
    return False  # Deleting either does not make increasing


# The below works, but it is a brute force approach. It fails on time complexity
# def almostIncreasingSequence(sequence):
#
#     if len(sequence) == 2:
#         return True
#
#     length = len(sequence)
#     #break_point = length - 2
#
#     for i in range(length):
#         item = sequence.pop(i)
#
#         for j in range(length-2):
#             print(j)
#             if sequence[j] >= sequence[j+1]:
#                 sequence.insert(i, item)
#                 break
#
#             if j == length - 3:
#                 return True
#
#     return False
