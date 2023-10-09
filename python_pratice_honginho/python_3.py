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
                    # print(rand)
                cnt=0
                for q in range(k):
                    x=random.uniform(0,1)
                    y=random.uniform(0,1)
                    if x*x + y*y <= 1:
                        cnt +=1
                pi = (cnt/k)*4
                print(f"10000000번 시행 후 파이는 {pi}(으)로 계산되었습니다.")
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
        #a1, b1, c1 =map(int, input("1번 다항식 계수: ").split())
        #a2, b2, c2 = map(int, input("2번 다항식 계수: ").split())
        #g = "x"
        #o = input("연산자 (+, -, * 중 선택):")  # o는 연산자 변수
        count = 0
        while True:
            a1, b1, c1 = map(int,input("1번 다항식 계수: ").split())
            a2, b2, c2 = map(int,input("2번 다항식 계수: ").split())
            operator = input("연산자 (+, -, * 중 선택):")  # o는 연산자 변수
            q = "x"
            count += 1
            if "+" in operator:
                result_a = a1 +a2
                result_b = b1 +b2
                result_c = c1 + c2
                if result_b >= 0 and result_c >=0:
                    print(f"결과=({result_a}x^2+{result_b}x+{result_c})")
                elif result_b < 0:
                    print(f"결과=({result_a}x^2-{abs(result_b)}x+{result_c})")
                elif result_c < 0:
                    print(f"결과=({result_a}x^2+{result_b}x-{abs(result_c)})")
                elif result_b <0 and result_c<0:
                    print(f"결과=({result_a}x^2-{abs(result_b)}x-{abs(result_c)})")
                else:
                    print(f"결과=({result_a}x^2+{result_b}x+{result_c})")
                print("프로그램이 종료됩니다.")
                break
            elif "-" in operator:
                result_a = a1 - a2
                result_b = b1 - b2
                result_c = c1 - c2
                if result_b >= 0 and result_c >=0:
                    print(f"결과=({result_a}x^2+{result_b}x+{result_c})")
                elif result_b < 0:
                    print(f"결과=({result_a}x^2-{abs(result_b)}x+{result_c})")
                elif result_c < 0:
                    print(f"결과=({result_a}x^2+{result_b}x-{abs(result_c)})")
                elif result_b <0 and result_c<0:
                    print(f"결과=({result_a}x^2-{abs(result_b)}x-{abs(result_c)})")
                else:
                    print(f"결과=({result_a}x^2+{result_b}x+{result_c})")
                print("프로그램이 종료됩니다.")
                break
            elif "*" in operator:
                result_a = a1 * a2
                result_b = (a1*b2) + (b1*a2)
                result_c = (a1*c2) + (a2*c1) + (b1*b2)
                result_d = (b1*c2) + (b2*c1)
                result_e = c1*c2
                print(f"결과=({result_a}x^4{result_b}x^3{result_c}x^2{result_d}x{result_e})")
                print("프로그램이 종료됩니다.")
                break
            else:
                print("연산자 오류입니다. 다시 입력해 주세요.")
                continue
        break
    elif d == 0:
        print("프로그램이 종료되었습니다.")
        break
    else:
        print("오류입니다. 1, 2, 0 중 하나를 입력하세요.")
    continue


