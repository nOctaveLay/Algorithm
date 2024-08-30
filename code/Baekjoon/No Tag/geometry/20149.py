# https://www.acmicpc.net/problem/20149
# ccw 안 쓴 풀이
#l1
x1, y1, x2, y2 = map(int,input().split())
p1 = [x1,y1]
p2 = [x2,y2]

#l2
x3, y3, x4, y4 = map(int,input().split())
p3 = [x3,y3]
p4 = [x4,y4]

def get_intersection_point(p1,p2,p3,p4):
    x1, y1 = p1
    x2, y2 = p2
    l1_dx = (x1 - x2)
    l1_dy = (y1 - y2)
    l1_matrix_mul = (x1*y2 - x2*y1)

    x3, y3 = p3
    x4, y4 = p4
    l2_dx = (x3 - x4)
    l2_dy = (y3 - y4)
    l2_matrix_mul = (x3*y4 - x4*y3)

    slove = (l1_dx * l2_dy - l1_dy * l2_dx)

    intersection_x = (l1_matrix_mul * l2_dx - l2_matrix_mul * l1_dx) / slove
    intersection_y = (l1_matrix_mul * l2_dy - l1_dy * l2_matrix_mul) / slove

    return (intersection_x, intersection_y)

# 전체 범위가 빗겨난다면, 영원히 만날 일은 없다.
if min(x1, x2) > max(x3, x4) or min(x3, x4) > max(x1, x2) or \
        min(y1, y2) > max(y3, y4) or min(y3, y4) > max(y1, y2):
    print(0)
    quit()

if (x4-x3) * (y2-y1) == (x2-x1) * (y4-y3): # 기울기가 같다.
    l1_b = ((x2-x1) * y1 - (y2-y1) * x1) 
    l2_b = ((x4-x3) * y3 - (y4-y3) * x3)

    # 일치할 경우 --> y = mx + b 에서 b가 같다.
    if (x4-x3) * l1_b == (x2-x1) * l2_b:
        print(1)
        # 그 중에서도 범위가 한 좌표만 겹치는 경우
        if max(x1,x2) == min(x3,x4) or max(x3,x4) == min(x1,x2):
            if x1 in [x3,x4]:
                print(x1,y1)
            else:
                print(x2,y2)
    # 평행할 경우
    else:
        print(0)
else: # 기울기가 다를 경우
    inter_x, inter_y = get_intersection_point(p1,p2,p3,p4)
    if min(x1,x2) <= inter_x <= max(x1,x2) and min(y1,y2) <= inter_y <= max(y1,y2) and\
        min(x3,x4) <= inter_x <= max(x3,x4) and min(y3,y4) <= inter_y <= max(y3,y4):
        print(1)
        print(inter_x,inter_y)
    else:
        print(0)