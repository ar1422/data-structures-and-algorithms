
def max_crossing_subarray(array, low, mid, high):

    left_sum = float("-inf")
    curr_sum = 0
    left_mark = mid
    for i in range(mid, low-1, -1):
        curr_sum += array[i]
        if curr_sum > left_sum:
            left_sum = curr_sum
            left_mark = i

    right_sum = float("-inf")
    curr_sum = 0
    right_mark = mid

    for j in range(mid+1, high):
        curr_sum += array[j]
        if curr_sum > right_sum:
            right_sum = curr_sum
            right_mark = j

    return left_mark, right_mark, (left_sum + right_sum)


def max_sum_subarray(array, low, high):
    if low == high:
        return low, high, array[low]

    mid = (low + high)//2
    left_low, left_high, left_sum = max_sum_subarray(array, low, mid)
    right_low, right_high, right_sum = max_sum_subarray(array, mid+1, high)
    mid_low, mid_high, mid_sum = max_crossing_subarray(array, low, mid, high)

    if left_sum >= mid_sum and left_sum >= right_sum:
        return left_low, left_high, left_sum
    elif right_sum >= mid_sum and right_sum >= left_sum:
        return right_low, right_high, right_sum

    else:
        return mid_low, mid_high, mid_sum


def main():
    array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(max_sum_subarray(array, 0, 15))
    return None


if __name__ == '__main__':
    main()
