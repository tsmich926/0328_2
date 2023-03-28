#오른쪽이나 아래로만 이동 오른쪽으로 가는경우/아래으로 가는경우
#부분 집합 문제와 유사

def solve(row,col,curs):
    global minv

    if minv < curs: #속도개선작업 굳이 내려보내필요가 없다. 이전에 더 작은 값이 나왔으므로
        return

    if row==N-1 and col==N-1:
        if curs < minv:
            minv = curs
        # print(curs)
        return

    if col+1<N:
        solve(row,col+1,curs+arr[row][col+1])
    if row + 1 < N:
        solve(row+1,col,curs+arr[row+1][col])

T = int(input())
for tc in range(1,T+1):
    N =int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    print(arr)

    minv = 10*13*13
    solve(0,0,arr[0][0])
    print(minv)