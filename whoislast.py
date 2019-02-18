#마지막 승자를 가리는 게임
'''약 2,000년 전에는 전쟁에서 병사들이 적들에 의해 동굴에 갇히게 되는 경우가 종종 있었다고 한다.

그들은 포로가 되는것을 방지하기 위해 동그랗게 서서 마지막 한 사람이 남을 때 까지 순서대로 돌아가며 세번째에 해당되는 사람을 죽여 나갔다고 한다.

마지막으로 남게되는 사람은 자살하기로 약속되어 있었지만 보통 적들에게 항복을 하는 경우가 많았다고 한다.

여러분이 풀어야 할 문제는 총 인원수(N)와 간격(K)이 주어졌을 때 가장 마지막에 살아남는 병사의 위치(the safe position)를 알아내는 것이다.

예를 들어 병사수가 총 10명이고 돌아가며 세번째에 해당되는 병사를 제거하는 경우는 다음과 같다:


N = 10, K = 3

위의 경우 다음과 같은 순서로 병사들이 제거된다. (괄호는 제거되는 병사를 의미한다)
1st round: 1 2 (3) 4 5 (6) 7 8 (9) 10
2nd round:                            1 (2) 4 5 (7) 8 10
3rd round:                                                (1) 4 5 (8) 10
4th round:                                                               4 (5) 10
5th round:                                                                        4 (10)


위 예에서 끝가지 살아남는 병사는 4, 즉 4번째 병사이다.

입력 데이터는 총 병사수 N과 간격 K이다.
출력 데이터는 마지막까지 살아남는 병사의 위치이다.

(단, 최초 시작은 1번 병사부터이다.)

입출력 예는 다음과 같다:
initial data:
10 3

answer:
while len(size)!=1:

'''
size,n=map(int,input('입력하세요').strip().split())
n_list=list(range(1,size+1))

n
count = 1
n_list
count
n_list

#n_list 추출할 리스트, n: n번째 건너뛰기, count: 현재 위치 n만큼되면 0으로 초기화
def recursive(n_list, n, count):
    #print(n_list)
    if len(n_list) == 1:
        return n_list
    else:
        new_list=[]
        for i in range(len(n_list)):
            if count == n: # n번째가 되면 append를 쓰지않고 넘어감.
                count = 1
                continue
            new_list.append(n_list[i])
            count += 1
        #print(new_list)
        return recursive(new_list, n, count)

recursive(n_list, n, count)
new_list
n_list

for i in range(len(size)):
    if count==2:
        continue
    list1.append(size[count])
    count+=1
    if count==2:
        count=0

list1
size
