def duplicate_count(text):
    text_list = [char for char in text.lower()]
    my_dict = {}
    for char in text_list:
        point = text_list.count(char)
        if text_list.count(char) > 1:
            my_dict[char] = point
    return len(my_dict)


text = input()
print(duplicate_count(text))