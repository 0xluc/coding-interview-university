def search(numbers, target, min, max):
    if max < min:
        return -1
    else:
        mid = (max + min) // 2
        print(mid)
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            search(numbers, target, mid + 1, max)
        else:
            search(numbers, target, min, mid - 1)
