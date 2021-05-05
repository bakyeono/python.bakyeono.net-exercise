# 연습문제 5-11
식재료별_칼로리 = {
    '밀가루': 364.0 / 100,
    '피망': 20.1 / 100,
    '올리브': 115.0 / 100,
    '돼지고기': 242.1 / 100,
}


def 칼로리(음식종류, 섭취량):
    """음식의 종류와 섭취량을 매개변수에 전달받아 총 칼로리를 반환한다."""
    return 식재료별_칼로리.get(음식종류, 0) * 섭취량


# 함수의 동작 확인
print(칼로리('돼지고기', 500))
print(칼로리('소고기', 300))
