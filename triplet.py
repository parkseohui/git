#a + b + c = 1000 인 피타고라스 수 a, b, c  (여기서 a < b < c ).
for a in range(1,500):
    for b in range(a,500):
        for c in range(b,500):
            if a*a+b*b==c*c:
                if a+b+c==1000:
                    print('a는',a,'b는',b,'c는',c)
