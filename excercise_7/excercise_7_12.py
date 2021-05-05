# 연습문제 7-12
def faulty_rate(diameters):
    """베어링의 지름을 담은 리스트를 전달받아 불량률을 계산하여 반환한다.
    베어링의 지름이 0.99mm 이상 1.01mm 미만이면 정상 제품으로 판단한다."""
    faulty = list(filter(lambda diameter: not (0.99 <= diameter < 1.01), diameters))
    return len(faulty) / len(diameters)


# 함수의 동작 확인
diameters = [0.985, 0.992, 1.004, 0.995, 0.899, 1.001, 1.002, 1.003, 1.009, 0.998]
print(faulty_rate(diameters))
