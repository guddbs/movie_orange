price = int(input("물건 값 : "))
money1000 = int(input("1000원짜리 지폐개수 :"))
price1000 = (1000*money1000)
money500 = int(input("500원짜리 지폐개수 :"))
price500 = (500*money500)
money100 = int(input("100원짜리 지폐개수 :"))
price100 = (100*money100)

remain_money = -(price - price1000 - price500 - price100)
print("거스름돈", remain_money)
give_500 = remain_money // 500
give_100 = remain_money // 100
give_10 = (remain_money-(give_100*100)) // 10
give_1 = (remain_money - give_100*100 - give_10*10) // 1

print(give_500)
print(give_100)
print(give_10)
print(give_1)