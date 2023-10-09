import random
a = "1. 몬테카를로 시뮬레이션으로 파이 계산"
b = "2. 다항식 연산"
c = "0. 프로그램 종료"
print(a)
print(b)
print(c)

count = 0
while True:
    count += 1
    d = int(input("선택: "))  #d는 어떤 항목을 선택할지 결정하는 변수다.
    if d == 1:
        count = 0  # 초기화
        while True:
            k = int(input("시뮬레이션 횟수를 정수로 입력하세요 (단 10^6 이상): "))
            count += 1
            if k >= 10 ** 6:
                cnt = 0
                for j in range(k):
                    x = random.random()
                    y = random.random()
                    if x * x + y * y <= 1:
                        cnt += 1
                pi = (cnt / k) * 4
                print(f"{k}번 시행 후 파이는 {pi}(으)로 계산되었습니다.")
                print("프로그램이 종료되었습니다.")
                break  # 반복문 탈출
            elif k < 10**6:
                continue  # 반복 처음으로 되돌아가기
        break
    elif d == 2:
        count = 0  # 초기화
        while True:  # 반복문
            a1, b1, c1 = map(int,input("1번 다항식 계수: ").split())  # map함수를 통해 굳이 하나하나씩 안써도 됨
            a2, b2, c2 = map(int,input("2번 다항식 계수: ").split())
            count += 1
            cnt = 0
            while True:
                operator = input("연산자 (+, -, * 중 선택):")  # operator는 연산자 변수
                cnt += 1
                if "+" in operator:  # operator 안에 +가 있다는 조건
                    result_a = a1 + a2
                    result_b = b1 + b2
                    result_c = c1 + c2
                    if result_b >= 0 and result_c >=0:  # 둘 다 0보다 크거나 같은 조건
                        print(f"결과=({result_a}x^2+{result_b}x+{result_c})")
                    elif result_b < 0:  # result_b만 0보다 작은 조건
                        print(f"결과=({result_a}x^2-{abs(result_b)}x+{result_c})")  # 절댓값 표시 해줌 abs를 통해서
                    elif result_c < 0:  # result_c만 0보다 작을 때 조건
                        print(f"결과=({result_a}x^2+{result_b}x-{abs(result_c)})")
                    elif result_b <0 and result_c<0:  # 둘 다 0보다 작을 때 조건
                        print(f"결과=({result_a}x^2-{abs(result_b)}x-{abs(result_c)})")
                    else:  # 아무 조건 없을 때
                        print(f"결과=({result_a}x^2+{result_b}x+{result_c})")
                    print("프로그램이 종료됩니다.")
                    break
                elif "-" in operator:
                    result_a = a1 - a2
                    result_b = b1 - b2
                    result_c = c1 - c2
                    if result_b >= 0 and result_c >=0:  # +일 때와 동일
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
        break
    elif d == 0:
        print("프로그램이 종료되었습니다.")
        break  # 반복문 탈출
    else:
        print("오류입니다. 1, 2, 0 중 하나를 입력하세요.")
    continue  # 처음으로 되돌아가기