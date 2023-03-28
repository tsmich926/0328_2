# https://velog.io/@tks7205/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-OSI-7%EA%B3%84%EC%B8%B5-1-1%EA%B3%84%EC%B8%B5-2%EA%B3%84%EC%B8%B5

#탐욕알고리즘
#규칙을 중간에 바꾸지 않는것이 원칙

#최소의 거스름돈 남겨주기

#배낭짐싸기는 탐욕적으로 접근해도 안풀림 부분집합과 비슷
#아이템 부분집합 무게의 합이 배낭무게 이하이면서 최대가 되도록 선택
#knapsack 문제의 패턴 0-1 두가지 물건을 통으로 넣거나 빼거나(문화재), fractional 잘라서 넣거나(금괴)//

#회의시간 배정



#부분집합을 재귀로 만들기
def f(i,k): #bit[i]를 결정하는 함수
    if i==k: #bit의 모든 원소 결정
        print(*bit)
    else:
        bit[i] = 0
        f(i+1,k)
        bit[i]=1
        f(i+1,k)


A = [7,2,5,3,4]
N = len(A)

bit = [0] * N #bit[i] A[i]원소가 부분집합에 포함되는지를 표시
f(0,N)
