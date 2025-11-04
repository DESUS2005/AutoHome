def is_year_leap(year):
    return year % 4 == 0


year = 2024  # Можно изменить этот год


result = is_year_leap(year)

print(f"год {year}: {result}")
