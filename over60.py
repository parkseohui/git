#60점 이상 통과
marks=[90,25,67,45,80]
number=0
for mark in marks:
    number=number+1
    if mark>=60:
        print("%d번 학생을 합격입니다."%number)
    else:
        print("%d번 학생은 불합격입니다."%number)

        
#continue
number=0
for mark in marks:
    number=number+1
    if mark>=60:
        print("%d번 학생은 합격입니다."%number)
    else:
        continue


#range
for number in range(len(marks)):
    if marks[number]<60:
        continue
    print("%d번 학생 축하합니다. 합격"%(number+1))
    
          
