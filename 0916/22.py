# 깊이가 깊어서 22번에서 오류 / 상현님이 dfs 로 풀었음 / 한번 참고하기
# bfs 로 풀어보기
def dfs(r, c, cnt):
    global maxcnt
    global visited
    for i in range(4):
        rr = r + d[i][0]
        cc = c + d[i][1]
        if 0 <= rr < n and 0 <= cc < n and [rr, cc] not in visited:
            if arr[rr][cc] == arr[r][c] + 1:
                r = rr
                c = cc
                visited.append([r, c])
                cnt = dfs(r, c, cnt+1)
    return cnt

for t in range(1, int(input())+1):
    n = int(input())
    lst = [[0]*n for _ in range(n)]
    arr = [list(map(int, input().split())) for _ in range(n)]
    maxcnt = 0
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for r in range(n):
        for c in range(n):
            visited = []
            visited.append([r, c])
            lst[r][c] = dfs(r, c, 1)

    idx = 0
    ret_max = 0

    ret_num = []
    for p in range(n):
        for q in range(n):
            if lst[p][q] >= ret_max:
                ret_max = lst[p][q]

    for g in range(n):
        for gg in range(n):
            if lst[g][gg] == ret_max:
                ret_num.append(arr[g][gg])

    print(f'#{t}', min(ret_num), ret_max)

