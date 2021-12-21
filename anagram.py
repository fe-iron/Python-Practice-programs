import re


def anagram(s1, s2):
    if sorted(s1) == sorted(s2):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")


if "__main__" == __name__:
    str1 = input("Enter the first string.. ").lower()
    str2 = input("Enter the second string.. ").lower()

    str1 = re.sub(r'[^a-zA-Z0-9]', '', str1)
    str2 = re.sub(r'[^a-zA-Z0-9]', '', str2)
    anagram(str1, str2)
