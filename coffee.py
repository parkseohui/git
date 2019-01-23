coffee =10
while True:
    money=int(input("돈을 넣어주세요: "))
    if money==300:
        print("커피한잔나왓씁니다.")
        coffee=coffee-1
    elif money>300:
        print("거스름돈 %d를 주고 커피한잔! " %(money-300))
        coffee=coffee-1
    else:
        print("돈을 돌려드리겠습니다. 돈을 더 넣으십시요.")
        print("남은 커피양은 %d 입니다."%coffee)
    if coffee==0:
        print("we have no more coffee")
        break
    
