number_of_snowballs = int(input())

last_highest_value = 0
weight_of_snowballs = 0
needed_time_to_target = 0
quality_of_snowballs = 0

for snowball in range(number_of_snowballs):
    current_weight_of_snowballs = int(input())
    current_needed_time_to_target = int(input())
    current_quality_of_snowballs = int(input())
    value_of_snowball = (current_weight_of_snowballs / current_needed_time_to_target) ** current_quality_of_snowballs

    if value_of_snowball > last_highest_value:
        last_highest_value = value_of_snowball
        weight_of_snowballs = current_weight_of_snowballs
        needed_time_to_target = current_needed_time_to_target
        quality_of_snowballs = current_quality_of_snowballs

print(f"{weight_of_snowballs} : {needed_time_to_target} = {int(last_highest_value)} ({quality_of_snowballs})")
