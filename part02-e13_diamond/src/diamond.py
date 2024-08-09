#!/usr/bin/env python3

import numpy as np

def diamond(n):
    if n <= 0:
        return np.array([])
    
    top_part = np.eye(n, dtype=int)
    top_part = np.concatenate((top_part[:, ::-1], top_part[:, 1:]), axis=1)
    
    bottom_part = top_part[:-1, :]
    
    diamond_shape = np.concatenate((top_part, bottom_part[::-1, :]), axis=0)
    
    return diamond_shape
