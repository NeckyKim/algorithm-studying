# Q10. 자물쇠와 열쇠
# 프로그래머스: https://school.programmers.co.kr/learn/courses/30/lessons/60059


# 키를 회전
def rotate(key):
    return list(zip(*key[::-1]))


# 자물쇠가 열리는지 확인
def check(new_lock):
    lock_size = len(new_lock) // 3

    # 자물쇠가 모두 1인지 확인
    for i in range(lock_size, lock_size * 2):
        for j in range(lock_size, lock_size * 2):

            # 하나라도 1이 아니면 False 반환
            if new_lock[i][j] != 1:
                return False

    # 모두 1이면 True 반환
    return True


def solution(key, lock):
    lock_size = len(lock)
    key_size = len(key)

    # new_lock: 자물쇠의 크기를 3배로 확장
    new_lock = [[0] * (lock_size * 3) for _ in range(0, lock_size * 3)]

    # new_lock 중앙에 기존의 좌물쇠를 배치
    for i in range(0, lock_size):
        for j in range(0, lock_size):
            new_lock[lock_size + i][lock_size + j] = lock[i][j]

    # 90, 180, 270, 360회전하여
    for _ in range(0, 4):
        # 열쇠를 회전
        key = rotate(key)

        for i in range(0, lock_size * 2):
            for j in range(0, lock_size * 2):

                # 자물쇠에 열쇠를 넣음
                for k in range(0, key_size):
                    for m in range(0, key_size):
                        new_lock[i + k][j + m] = new_lock[i + k][j + m] + key[k][m]

                # 자물쇠가 열리는지 검사
                if check(new_lock) == True:

                    # 하나의 경우의 수라도 자물쇠가 열쇠와 맞으면 바로 True 반환
                    return True

                # 자물쇠에 열쇠를 뺌
                for k in range(0, key_size):
                    for m in range(0, key_size):
                        new_lock[i + k][j + m] = new_lock[i + k][j + m] - key[k][m]

    # 모든 경우의 수를 검사해도 열리지 않으면 False 반환
    return False
