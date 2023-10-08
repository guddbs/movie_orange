import random

a = "1. 몬테카를로 시뮬레이션으로 파이 계산"
b = "2. 다항식 연산"
c = "0. 프로그램 종료"
print(a)
print(b)
print(c)


for i in range(1,3):
    d = int(input("선택: "))
    if d == 1:
#        k = int(input("시뮬레이션 횟수를 정수로 입력하세요 (단 10^6 이상): "))
        count = 0
        while True:
            k = int(input("시뮬레이션 횟수를 정수로 입력하세요 (단 10^6 이상): "))
            count += 1
            if k >= 10**6:
                for j in range(5):
                    rand = random.random()
                    print(rand)

                print(f"10000000번 시행 후 파이는 {rand}(으)로 계산되었습니다.")
                print("프로그램이 종료되었습니다.")
                break
            elif k < 10**6:
                continue
#        if k >= 10^6:
#            for j in range(5):
#                rand = random.random()
#                print(rand)
#        elif k < 10^6:
#           continue
        break
    elif d == 2:
        print(b)
        break
    elif d == 0:
        print("프로그램이 종료되었습니다.")
    else:
        print("오류입니다. 1, 2, 0 중 하나를 입력하세요.")
    continue


