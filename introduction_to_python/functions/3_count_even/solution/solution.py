def count_even(*args):
    count= 0
    for num in args:
        if num % 2 == 0:
            count += 1
    return count