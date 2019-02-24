list1=[3,1,2,4,5]
def mergesort(li): # 재귀함수
    n=len(li)
    if n==1: #리스트의 크기가 1이되면 리스트를 반환하고 끝냄
        return li
    mid=n//2 #중간값, 그룹을 나눔
    sg=mergesort(li[:mid]) #중간값을 기준으로 작은그룹
    lg=mergesort(li[mid:]) #큰그룹
    result=[] #최종반환할 리스트임
    while sg and lg: #두개의 리스트에 원소가 존재할때만 돌아감
            if sg[0]<lg[0]: #sg그룹의 0번째가 더 작으면 result에 sg[0]이 들어감
                result.append(sg.pop(0))
            else: #lg그룹의 0번째가 더 작으면 result에 lg[0]이 들어감
                result.append(lg.pop(0))

    while sg: #sg만 남았을때 sg의 원소들을 차례로 넣기
        result.append(sg.pop(0))
    while lg: #lg만 남았을때 lg의 원소를 차례로 넣기
        result.append(lg.pop(0))
    return result #리스트를 반환

print(mergesort(list1))
