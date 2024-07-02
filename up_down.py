import random

def up_down_game():
    # 가장 빨리 맞춘 횟수, 즉 최고기록을 출력하기 위해 min_cnt 변수 할당
    min_cnt = float('inf')

    while True:
        random_num = random.randint(1, 100)
        cnt = 0

        while True:
            # 숫자가 아닌 문자가 잘못 들어갈 경우 에러가 남, 따로 예외처리
            try:
                user_num = int(input("숫자를 입력하세요 : "))

                # 범위 밖의 숫자를 입력하거나 문자가 섞인 경우 경고문 출력
                if user_num < 1 or user_num > 100:
                    print("1부터 100 사이의 수를 입력하세요.")
                    continue

                cnt += 1

                if user_num < random_num:
                    print("업")
                elif user_num > random_num:
                    print("다운")
                else:
                    print(f"맞았습니다.\n시도한 횟수 :", cnt)

                    # 현재 cnt와 비교해서 최고기록을 업데이트
                    if cnt < min_cnt:
                        min_cnt = cnt
                    break

            except ValueError:
                print("유효한 숫자를 입력해주세요")

        # y이면 retry 탈출 후 다시 게임 반복문 시작, n이면 return을 통한 함수 종료, 그외 경고문 출력
        while True:
            retry = input("다시 하시겠습니까? (y/n): ")
            if retry == 'y':
                print("이전 게임 플레이어 최고 시도 횟수 :", min_cnt)
                break
            elif retry == 'n':
                print("게임을 종료합니다.")
                return
            else:
                print("y 또는 n을 입력해주세요.")

up_down_game()