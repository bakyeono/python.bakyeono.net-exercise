# 연습문제 11-4
def cp(src, dst):
    """원본 경로(src)의 파일을 목적 경로(dst)에 복사한다."""
    with open(src) as src_file, open(dst, 'w') as dst_file:
        dst_file.write(src_file.read())


cp('original.txt', 'clone.txt')
