def palindrome_filtered(word):
    if word == word[::-1]:
        return word


words = input().split()
palindrome_word = input()

palindrome_list = [word for word in words if palindrome_filtered(word)]
palindrome_counter = palindrome_list.count(palindrome_word)

print(palindrome_list)
print(f"Found palindrome {palindrome_counter} times")

# words_in_string = input().split()
# palindrome_word_count = input()
#
# palindrome_list = []
# counter = 0
# for word in words_in_string:
#     if word == word[::-1]:
#         palindrome_list.append(word)
#         if word == palindrome_word_count:
#             counter += 1
#
# print(palindrome_list)
# print(f"Found palindrome {counter} times")
