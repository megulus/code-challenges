"""
Given an array of characters chars, compress it using the following algorithm:

- Begin with an empty string s. For each group of consecutive repeating characters in chars:
	- If the group's length is 1, append the character to s.
	- Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars.
Note that group lengths that are 10 or longer will be split into multiple characters in chars. After you are done
modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Example 1:
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Example 2:
Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.

Example 3:
Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

Constraints:
1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
"""


def compress_string(chars: list[str]) -> int:
    i = 0
    ans = 0
    while i < len(chars):
        group_length = 1
        while (i + group_length < len(chars)) and (chars[i + group_length] == chars[i]):
            group_length += 1
        chars[ans] = chars[i]
        ans += 1
        if group_length > 1:
            str_repr = str(group_length)
            chars[ans:ans+len(str_repr)] = list(str_repr)
            ans += len(str_repr)
        i += group_length
    print(f'chars: {chars}')
    return ans


if __name__ == '__main__':
    c1 = ["a", "a", "b", "b", "c", "c", "c"]
    c2 = ["a"]
    c3 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    c4 = ["a", "a", "a", "a", "a"]
    c5 = ["a", "b", "c", "d", "e"]
    for c in [c1, c2, c3, c4, c5]:
        print(f'original: {c} new length: {compress_string(c)}')
        print()


def compress_string_bad(chars: list[str]) -> int:
    curr = chars[0]
    count = 0
    location = 0
    pointer = 0
    s = []
    while pointer < len(chars):
        print()
        print(f'pointer: {pointer} curr: {curr}')
        if chars[pointer] == curr and pointer != len(chars) - 1:
            count += 1
        else:
            print('here')
            if pointer == len(chars) - 1:
                count += 1
            s.append(curr)
            chars[location] = curr
            print(f'location: {location}')
            # location += 1
            if count > 1:
                s.append(str(count))
                if count < 10:
                    chars[location] = str(count)
                else:
                    occurrences = str(count)
                    for j in range(len(occurrences)):
                        location += j
                        chars[location] = occurrences[j]
            # curr = chars[pointer]
            count = 1
            location += 1
        curr = chars[pointer]
        print(f'new curr: {curr}')
        pointer += 1
    print(f's: {''.join(s)} chars: {chars}')
    return len(s)
