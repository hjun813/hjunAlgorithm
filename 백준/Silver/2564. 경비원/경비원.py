row, col = map(int, input().split())
n = int(input())
store = []
answer = 0

for i in range(n):
    x, y = map(int, input().split())
    nx = 0
    ny = 0
    if x == 1:
        nx = 0
        ny = y
    elif x == 2:
        nx = col
        ny = y
    elif x == 3:
        nx = y
        ny = 0
    elif x == 4:
        nx = y
        ny = row
    store.append([nx,ny,x, y])

dong_x, dong_y = map(int, input().split())
check = 0
nx = 0
ny = 0
if dong_x == 1:
    check = 2
    nx = 0
    ny = dong_y
elif dong_x == 2:
    check = 1
    nx = col
    ny = dong_y
elif dong_x == 3:
    check = 4
    nx = dong_y
    ny = 0 
elif dong_x == 4:
    check = 3
    nx = dong_y
    ny = row

for i in range(n):
    r_a, r_b, a, b = store.pop()
    short = 0
    if check == a: # 반대편
        if check == 1 or check == 2:
            answer += col
            short = min(r_b + ny, row*2 - r_b - ny)
            answer += short
        else:
            answer += row
            short = min(r_a + nx, col*2 - r_a - nx)
            answer += short       
    else:
        answer += abs(r_a - nx)
        answer += abs(r_b - ny)

print(answer)
        

# for i in range(n):
#     x, y = map(int, input().split())
#     nx = 0
#     ny = 0
#     if x == 1:
#         nx = 0
#         ny = y
#     elif x == 2:
#         nx = col
#         ny = y
#     elif x == 3:
#         nx = y
#         ny = 0
#     elif x == 4:
#         nx = y
#         ny = row
#     d = x
#     store.append([nx,ny,d])
# print(store)
# dong_x, dong_y = map(int, input().split())
# xx = 0
# yy = 0
# if dong_x == 1:
#     xx = 0
#     yy = dong_y
# elif dong_x == 2:
#     xx = col
#     yy = dong_y
# elif dong_x == 3:
#     xx = dong_y
#     yy = 0
# elif dong_x == 4:
#     xx = dong_y
#     yy = row
# print(xx, yy,dong_x)

# for i in range(n)):
#     s_x, s_y, s_d = store.pop()
#     if dong_x == s_d: # 방향이 일치
#         answer += abs(xx - s_x)
#         answer += abs(yy - s_y)
#         continue
        
#     elif 
    