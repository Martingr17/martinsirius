seconds = int(input())
year = 365*24*60*60
now_year = seconds // year
result = 1970 + now_year
print(result)