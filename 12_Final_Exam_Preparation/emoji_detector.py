import re

text_string = input()
pattern = r'([:]{2}|[*]{2})([A-Z]{1}[a-z]{2,})(\1)' # -> в предишните решения, регекска беше объркан
pattern_digit = r'\d+'

matches = re.findall(pattern, text_string)
matches_digits = re.findall(pattern_digit, text_string)

cool_threshold = 1
for char in text_string:
    if char.isdigit():
        cool_threshold *= int(char)

cool_emoji = []
for match in matches:
    counter = sum(ord(char) for char in match[1])

    if counter > cool_threshold:
        cool_emoji.append(match)
        counter = 0

print(f"Cool threshold: {cool_threshold}")
if len(matches) > 0: # -> в предишните решения не съм направил проверка дали дължината е по-голяма от 1
    print(f"{len(matches)} emojis found in the text. The cool ones are:")
    emoji = []
    for current_emoji in cool_emoji:
        emoji_string = current_emoji[0] + current_emoji[1] + current_emoji[0]
        emoji.append(emoji_string)

    for em in emoji:
        print(f"{em} ")