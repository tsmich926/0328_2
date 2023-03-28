#s는 이전단계에서 결정한 값
def comb(k,s):
    if k==N:
        # print(result)
        for i in result:
            print(nums[i], end=' ')
        print()
        return

    for i in range(s+1,N): #시간에 문제가 되면 N대신 N-K+2로 바꿔준다
        result[k]=i
        comb(k+1,i+1)

k= 3
N=5
nums = [7,3,2,1,5]
result = [-1] * k

comb(0,0)

