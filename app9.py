country_file = open('C:/Users/HP/countries.txt', 'r')
for lines in country_file.readlines():
    print(lines)
country_file.close()