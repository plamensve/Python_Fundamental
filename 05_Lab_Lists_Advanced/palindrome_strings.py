words_in_string = input().split()
palindrome_word_count = input()

palindrome_list = []
counter = 0
for word in words_in_string:
    if word == word[::-1]:
        palindrome_list.append(word)
        if word == palindrome_word_count:
            counter += 1

print(palindrome_list)
print(f"Found palindrome {counter} times")
# test


