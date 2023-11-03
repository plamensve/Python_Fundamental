country_names = [country for country in input().split(', ')]
capital_cities = [capital for capital in input().split(', ')]

result = zip(country_names, capital_cities)
total_result = {key: value for key, value in result}
for k, v in total_result.items():
    print(f"{k} -> {v}")
