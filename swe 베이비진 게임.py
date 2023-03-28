# 같은 숫자가 세개면 triple
# 연속숫자면 run


def getTriRun(result,strV):
    strV = list(map(int,strV))
    tri = run = 0
    if strV[result[0]]==strV[result[1]] and strV[result[1]] ==strV[result[2]]:
        tri += 1
    if strV[result[3]] == strV[result[4]] and strV[result[4]] == strV[result[5]]:
        tri += 1
    # if 0,1,2 run확인
    if strV[result[0]] + 1 == strV[result[1]] and strV[result[1]] + 1 == strV[result[2]]:
        run += 1
    # if 3,4,5 run확인
    if strV[result[3]] + 1 == strV[result[4]] and strV[result[4]] + 1 == strV[5]:
        run += 1

    return tri+run


# 모든 경우의 수를 다 구해본다-완전검색으로 푸는법
def per(k,strV,used):
    if k==N:        
        if getTriRun(strV,result)==2:
            return True
        return False

    for i in range(N):
        if not used[i]:
            used[i] = True
            result[k] = i
            if per(k+1,strV,used):
                return True
            used[i] = False


    return False

    # N = 6
    # used = [False] * N
    result = [-1] * N
    # per(0)

# 문자열이 Babygin인지 확인하고 t/f를 return
def isBabygin(strV):
    used = [False] * 6
    return per(0, strV, used)

result = [-1] * 6
N = 6
print(isBabygin("123483"))
print(isBabygin("667767"))
print(isBabygin("054060"))
print(isBabygin("101123"))



        #3개씩 잘라서 babygin 인지 확인하는 작업
        # if 0,1,2번째 값이 같으면
        # if strV[0]==strV[1] and strV[1] ==strV[2]:
        #     tri += 1
        # if  3,4,5번째 값이 같으면
        # if strV[3] == strV[4] and strV[4] == strV[5]:
        #     tri += 1
        # if 0,1,2 run확인
        # if strV[0]+1 == strV[1] and strV[1]+1 ==strV[2]:
        #     run +=1
        # if 3,4,5 run확인
        # if strV[0] + 1 == strV[1] and strV[1] + 1 == strV[2]:
        #     run+=1
        #
        # if tri+run == 2:
        #     return True
        # return False




# 667767라는 숫자열이 들어오면
# 012345로 순서가 부여된다
# {0,1,2,3,4,5} 순열 조합이 만들어질 수 있다.
# 여러가지 순열조합중 {5,0,3,1,4,2}가 만들어 졌다고 하면
# result는 위치값이니까
# result[0] 번째 값은 5 이고
# result[1]번째 값은 0이다
# result[2]번째 값은 3이다.
# 5,0,3는 트리플도 run도 아니다.
# result[3],result[4],result[5]는 차례로 1,4,2가 된다.
# 이 경우는 아무 조건도 만족하지 못했으므로 babygin이 아니다.