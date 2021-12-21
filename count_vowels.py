def count_vowel(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in sentence.lower():
        if i in vowels:
            count += 1

    return count


if __name__ == "__main__":
    print(count_vowel(input("Enter a sentence")))