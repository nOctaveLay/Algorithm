
def solution(nums):
    '''
    input: n마리 폰켓몬의 종류 번호가 담긴 배열 nums 1차원 배열
    1 <= n <= 10000
    1 <= 종류 번호 <= 200000
    가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아
    폰켓몬 종류 번호의 개수를 return하도록 만들어라.
    '''
    # 중복되지 않는 폰켓몬 종류가 담겨 있는 배열이 있다면
    # 이 수가 len(nums) // 2보다 작다면 그만큼만 가져갈 수 있는 거고
    # 그것보다 크다면 len(nums) // 2까지만 가져갈 수 있는 거네?
    
    no_overlap_nums = set(nums)

    answer = len(nums) // 2 if len(no_overlap_nums) > (len(nums) // 2) else len(no_overlap_nums)
    return answer