import numpy as np
def solution(num_list, n):
    list = np.array(num_list).reshape(-1,n)
    return list.tolist()