def loading_bar(some_number):
    if number == 100:
        return '100% Complete!\n[%%%%%%%%%%]'
    percent_count = some_number // 10
    return f"{some_number}% [{percent_count * '%'}{(10 - percent_count) * '.'}]\nStill loading..."


number = int(input())
print(loading_bar(number))
