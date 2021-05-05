# 연습문제 11-5
import csv

# 파일 읽기
filename = 'countries.csv'
with open(filename) as file:
    countries = list(csv.reader(file))[1:]


# 인구 밀도 구하기
for country in countries:
    # country[1]: 인구, country[2]: 면적
    country.append(int(country[1]) / int(country[2]))


# 인구 밀도 내림차순으로 정렬하기
sorted_countries = sorted(countries, key=lambda row: row[3], reverse=True)


# 나라 이름과 인구밀도 출력하기
for country in sorted_countries:
    print(country[0], country[3])
