#!/usr/bin/env python3

def merge(L1, L2):
    merged_list = []
    i = 0  # Index for L1
    j = 0  # Index for L2

    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            merged_list.append(L1[i])
            i += 1
        else:
            merged_list.append(L2[j])
            j += 1

    # Append any remaining elements from L1 and L2
    while i < len(L1):
        merged_list.append(L1[i])
        i += 1

    while j < len(L2):
        merged_list.append(L2[j])
        j += 1

    return merged_list

if __name__ == "__main__":
    # Test cases
    L1 = [1, 3, 5]
    L2 = [2, 4, 6]
    result = merge(L1, L2)
    print(result)  # Should print [1, 2, 3, 4, 5, 6]

    L3 = [10, 20, 30]
    L4 = [5, 15, 25]
    result = merge(L3, L4)
    print(result)  # Should print [5, 10, 15, 20, 25, 30]
