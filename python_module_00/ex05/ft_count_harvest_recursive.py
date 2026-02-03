def recursive_active(days, start):

    if start <= days:
        print("Day", start)
        return recursive_active(days, start + 1)


def ft_count_harvest_recursive():

    start = 1
    days = int(input("Days until harvest :"))
    recursive_active(days, start)
