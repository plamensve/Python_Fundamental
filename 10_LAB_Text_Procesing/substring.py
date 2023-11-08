word = input()
banned_word = input()

while word in banned_word:
    banned_word = banned_word.replace(word, '')

print(banned_word)

