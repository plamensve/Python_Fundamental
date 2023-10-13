def alphabetical_order(string):
    sorted_string = sorted(string)
    sorted_by_len = sorted(sorted_string, key=len, reverse=True)
    return sorted_by_len


single_string = input().split(', ')
result = alphabetical_order(single_string)
print(result)
