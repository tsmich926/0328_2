#부분집합
# def par(k):
#     if k==N:
#         print(result)
#         for i in range(N):
#             if result[i]: #1인 경우만 출력
#                 print(nums[i],end=' ')
#         print()
#         return
#
#     result[k] = 1
#     par(k+1)
#     result[k] = 0
#     par(k+1)


#합이 10이상인 부분집합

# def par(k):
#     global cnt
#     if k==N:
#         print(result)
#         sumV = 0
#         for i in range(N):
#             if result[i]: #1인 경우만 출력
#                 sumV += nums[i]
#                 # print(nums[i],end=' ')
# 
# 
#         if sumV < 10:
#             cnt +=1
#         return
# 
#     result[k] = 1
#     par(k+1)
#     result[k] = 0
#     par(k+1)


#
# nums = [7,3,2,1,5]
# N = len(nums)
# result = [-1]*N
# cnt = 0
# par(0)
# print(cnt)



#순열-위치를 기준으로 나열

def par(k):
    if k==N:
        print(result)
        for idx in result:
            print(nums[idx], end=' ')
        print()
        return

    for i in range(N):
        if not used[i]:
            result[k] = i
            used[i] = True
            par(k+1)
            used[i] = False #원복시켜줘야 다음으로 넘어갈때 계산할 수 있음


nums = [7,3,2,1,5]
N = len(nums)
result = [-1]*N
used = [False]*N
par(0)

