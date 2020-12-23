# Write your code here
def divisible_by_3(*args):
    by_3 = []
    for num in args:
        if num % 3 == 0:
            by_3.append(num)
    return by_3