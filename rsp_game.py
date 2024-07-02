import random

def rsp_game():
    rsp = ["가위", "바위", "보"]
    wins = 0
    losses = 0
    ties = 0

    while True:
        #user_rsp를 결정
        user_rsp = input("가위, 바위, 보 중 하나를 선택하세요 : ")
        while user_rsp not in rsp:
            print("유효한 입력이 아닙니다")
            user_rsp = input("가위, 바위, 보 중 하나를 선택하세요 : ")

        #computer_rsp를 결정
        computer_rsp = random.choice(rsp)

        #사용자와 컴퓨터 각각 뭐냈는지 출력
        print(f"사용자 : {user_rsp}, 컴퓨터 : {computer_rsp}")

        #승패 결정(승,패,무 각각 횟수 할당)
        if user_rsp == computer_rsp:
            print("비겼습니다!")
            ties += 1
        elif ((user_rsp == "가위" and computer_rsp == "보") or
              (user_rsp == "바위" and computer_rsp == "가위") or
              (user_rsp == "보" and computer_rsp == "바위")):
            print("사용자 승리!")
            wins += 1
        else:
            print("컴퓨터 승리!")
            losses += 1

        #재시작 여부 질문(y,n 이외의 문자를 입력하는 경우까지 대비)
        while True:
            retry = input("다시 하시겠습니까? (y/n): ")
            if retry.lower() == "y":
                break
            elif retry.lower() == "n":
                print("게임을 종료합니다")
                print(f"승 : {wins}, 패 : {losses}, 무승부 : {ties}")
                return
            else:
                print("y 또는 n을 입력해주세요")

rsp_game()