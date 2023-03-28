nums = [1,2,3,4,5,6,7,8,9,10]


#갯수가 정해져있는 경우 for문 사용이 더 빠름
#10에서 두개 뽑기
for i in range(10):
    for j in range(i+1,10):
        print(i,j)
        
#10개중에 세개뽑기
for i in range(8):
    for j in range(i+1,9):
        for k in range(j+1,10):
        print(i,j,k)