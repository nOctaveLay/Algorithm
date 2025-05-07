import sys

input=sys.stdin.readline

num_of_city = int(input())

city_lengths = list(map(int,input().split()))
city_costs = list(map(int,input().split()))


# city cost가 작은 곳에서 한 번 끊어가는 게 무조건 최소 금액이 나온다.
# 총 금액을 result_cost라고 하자.
result_cost = 0

# 처음 시작은 0번 부터 시작한다.
min_city_index = 0
min_cost = city_costs[0]

for city_index in range(1, num_of_city):

    # 만약 city cost가 min_cost 보다 작은 곳을 만났다면 한 번 끊어간다.
    if city_costs[city_index] < min_cost:

        # 그간 달려온 금액을 정산한다.
        result_cost += sum(city_lengths[min_city_index:city_index]) * min_cost
        # print(result_cost)

        # min_cost를 갱신해주고, 현재 위치까지 정산되었음을 알려주는 min_city_index를 업데이트 한다.
        min_cost = city_costs[city_index]
        min_city_index = city_index
        # print("min_city_index",min_city_index)

# 만약 min_city_index가 한 번 갱신된 후로 min_city가 나타나지 않았다면, 끝까지 갱신을 해주어야 한다.

# print("final min_city_index", min_city_index)
if min_city_index != num_of_city -1:
    result_cost += sum(city_lengths[min_city_index:]) * min_cost

print(result_cost)

