version = input().split(".")
connected_string = "".join(version)
next_version = int(connected_string) + 1
result = ".".join(str(next_version))
print(result)