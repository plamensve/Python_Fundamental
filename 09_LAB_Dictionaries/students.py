line = input()
searched_course = ''
course_info = {}
students_id = {}

while True:
    try:
        student, ID, course = line.split(':')
        course_info[student] = course
        students_id[student] = ID
        line = input()

    except ValueError:
        searched_course = line
        break


for k, v in course_info.items():
    if v[0:3] == searched_course[0:3]:
        print(f'{k} - {students_id[k]}')
