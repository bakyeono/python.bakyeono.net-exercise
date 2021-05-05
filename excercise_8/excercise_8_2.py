# 연습문제 8-2
# 유형: '체스말'은 다음 키를 가지는 사전이다.
#     * 'type': '체스말'
#     * 'x': 말이 놓인 x축의 위치 (정수)
#     * 'y': 말이 놓인 y축의 위치 (정수)
#     * 'color': 말의 색 (문자열, 'black' 또는 'white')
#     * 'role': 말의 역할 (문자열)
체스말1 = {'type': '체스말', 'x': 'A', 'y': '8', 'color': 'black', 'role': '룩'}
체스말2 = {'type': '체스말', 'x': 'E', 'y': '1', 'color': 'white', 'role': '킹'}

# 유형: '바둑돌'은 다음 키를 가지는 사전이다.
#     * 'type': '바둑돌'
#     * 'x': 돌이 놓인 x축의 위치 (정수)
#     * 'y': 돌이 놓인 y축의 위치 (정수)
#     * 'order': 돌이 놓인 수 (정수)
#     * 'color': 돌의 색 (문자열, '흑' 또는 '백')
바둑돌1 = {'type': '바둑돌', 'x': 8, 'y': 14, 'order': 83, 'color': '흑'}
바둑돌2 = {'type': '바둑돌', 'x': 12, 'y': 3, 'order': 84, 'color': '백'}


def print_piece(piece):
    """체스말 또는 바둑돌 데이터를 전달받아 적절한 양식으로 화면에 출력한다."""
    if piece['type'] == '체스말':
        print(piece['color'],' ',piece['role'],'이 ',
              piece['x'],piece['y'],' 위치에 놓여 있어요.',
              sep='')
    elif piece['type'] == '바둑돌':
        print('제 ', piece['order'], ' 수: ', piece['color'],
              '을 (', piece['x'], ', ', piece['y'], ') 위치에 두었습니다.',
              sep='')


# 함수의 동작 확인
print_piece(체스말1)
print_piece(체스말2)
print_piece(바둑돌1)
print_piece(바둑돌2)
