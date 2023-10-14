text = input().split()
text_list = [word for word in text if len(word) % 2 == 0]
print("\n".join(text_list))
