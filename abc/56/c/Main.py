import math
import sys

x = int(input())

i = 1

if x == 1:
    print(1)
    exit()

while True:
    if ((i+1)*i) / 2 < x and x <= ((i+2)*(i+1)) / 2:
        print(i+1)
        break
    i += 1

# def is_ok(n):
#     # 条件を満たすかどうか？問題ごとに定義
#     return 

# def meguru_bisect(ng, ok):
#     '''
#     初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
#     まずis_okを定義すべし
#     ng ok は  とり得る最小の値-1 とり得る最大の値+1
#     最大最小が逆の場合はよしなにひっくり返す
#     '''
#     while (abs(ok - ng) > 1):
#         mid = (ok + ng) // 2
#         if is_ok(mid):
#             ok = mid
#         else:
#             ng = mid
#     return ok

# print(meguru_bisect(0, 10**9 + 1))