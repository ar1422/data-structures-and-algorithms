import random


def find_k_th_smallest(array, k):
    rand_obj = random.Random()
    index = rand_obj.randint(0, len(array))
    left = []
    equal = []
    right = []
    for num in array:
        if num < array[index]:
            left.append(num)
        elif num == array[index]:
            equal.append(num)
        else:
            right.append(num)

    if len(left) >= k:
        return find_k_th_smallest(left, k)
    elif len(equal) >= k - len(left):
        return array[index]
    else:
        return find_k_th_smallest(right, k - len(left) - len(equal))


def main():
    array = [1, 4, 2, 6, 7, 3, 2, 1, 4, 5, 6]
    print(find_k_th_smallest(array, 8))
    return None


if __name__ == '__main__':
    main()