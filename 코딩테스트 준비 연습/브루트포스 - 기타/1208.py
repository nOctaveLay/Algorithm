
from functools import partial


l = []
def partial_sum(idx,end,idx_sum):
    if idx == end:
        l.append(idx_sum)
        return
    partial_sum(idx+1,end,idx_sum+arr[idx])
    partial_sum(idx+1,end,idx_sum)
