#!/usr/bin/env python3


def detect_ranges(numbers):
    if not numbers:
        return []

    sorted_numbers = sorted(numbers)
    result = []
    start = sorted_numbers[0]
    end = sorted_numbers[0]

    for num in sorted_numbers[1:]:
        if num == end + 1:
            end = num
        else:
            if start == end:
                result.append(start)
            else:
                result.append((start, end + 1))
            start = end = num

    if start == end:
        result.append(start)
    else:
        result.append((start, end + 1))

    return result

