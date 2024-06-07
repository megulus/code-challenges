import re


# Code

def string_reverser(our_string):
    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """
    result = ''
    for i in range(len(our_string) - 1, -1, -1):
      result += our_string[i]
    return result

# Test Cases


# print("Pass" if ('retaw' == string_reverser('water')) else "Fail")
# print("Pass" if ('!noitalupinam gnirts gnicitcarP' ==
#                  string_reverser('Practicing string manipulation!')) else "Fail")
# print("Pass" if ('3432 :si edoc esuoh ehT' ==
#                  string_reverser('The house code is: 2343')) else "Fail")



# Code

def anagram_checker(str1, str2):
    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """
    alpha = re.

# Test Cases

# print("Pass" if not (anagram_checker('water', 'waiter')) else "Fail")
# print("Pass" if anagram_checker('Dormitory', 'Dirty room') else "Fail")
# print("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
# print("Pass" if not (anagram_checker('A gentleman', 'Elegant men')) else "Fail")
# print("Pass" if anagram_checker('Time and tide wait for no man',
#                                 'Notified madman into water') else "Fail")

# Code


def word_flipper(our_string):
    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """

    # TODO: Write your solution here

    pass

# Test Cases


# print("Pass" if ('retaw' == word_flipper('water')) else "Fail")
# print("Pass" if ('sihT si na elpmaxe' ==
#                  word_flipper('This is an example')) else "Fail")
# print("Pass" if ('sihT si eno llams pets rof ...' ==
#                  word_flipper('This is one small step for ...')) else "Fail")


# Code

def hamming_distance(str1, str2):
    """
    Calculate the hamming distance of the two strings

    Args:
       str1(string),str2(string): Strings to be used for finding the hamming distance
    Returns:
       int: Hamming Distance
    """

    # TODO: Write your solution here

    pass

# Test Cases


# print("Pass" if (10 == hamming_distance('ACTTGACCGGG', 'GATCCGGTACA')) else "Fail")
# print("Pass" if (1 == hamming_distance('shove', 'stove')) else "Fail")
# print("Pass" if (None == hamming_distance(
#     'Slot machines', 'Cash lost in me')) else "Fail")
# print("Pass" if (9 == hamming_distance('A gentleman', 'Elegant men')) else "Fail")
# print("Pass" if (2 == hamming_distance(
#     '0101010100011101', '0101010100010001')) else "Fail")
