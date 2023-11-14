lines = int(input())
for info in range(lines):
    string = input()
    name_start = string.find('@')
    name_finish = string.find('|')
    age_start = string.find('#')
    age_finish = string.find('*')
    first_name = string[name_start + 1:name_finish]
    age_of_person = string[age_start + 1:age_finish]
    print(f"{first_name} is {age_of_person} years old.")
