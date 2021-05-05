# 연습문제 7-4
happiness = {
    '호주': 7.95,
    '노르웨이': 7.9,
    '미국': 7.85,
    '일본': 6.2,
    '한국': 5.75,
}

for country_name, score in happiness.items():
    print(country_name, ' 사람들은 ', score, '만큼 행복합니다.', sep='')
