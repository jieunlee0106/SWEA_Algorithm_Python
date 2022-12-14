from itertools import combinations
def cook():
    global ret, visited

    for A in dish:
        if A not in visited:
            visited += [[A]]
            B = []
            for b in lst:
                if b not in A:
                    B += [b]
            visited += [[B]]
            A_dish = 0
            B_dish = 0
            for ar in range(len(A)):
                for ac in range(len(A)):
                    if ar != ac:
                        A_dish += arr[A[ar]][A[ac]]
            for br in range(len(B)):
                for bc in range(len(B)):
                    if br != bc:
                        B_dish += arr[B[br]][B[bc]]
            abab = abs(A_dish - B_dish)
            ret = min(ret, abab)

for tc in range(1, int(input())+1):
    n = int(input())
    lst= [i for i in range(n)]
    arr = [list(map(int, input().split())) for _ in range(n)]
    dish = []
    visited = []
    for i in combinations(lst, n//2):
        dish += [i]

    ret = 100000
    cook()
    print(f'#{tc} {ret}')
