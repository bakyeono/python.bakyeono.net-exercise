# 연습문제 5-6
stations = []
stations.append('서울')
stations += (['수원', '대전'])
stations.extend(['밀양', '부산'])
stations.insert(3, '동대구')

print(stations)  # 출력 1
print(stations.pop())  # 출력 2
print(stations.remove('수원'))  # 출력 3
print(stations)  # 출력 4
