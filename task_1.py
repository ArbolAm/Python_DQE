import random


# create list of 100 random numbers from 0 to 1000
LIST = []
for i in range(100):
    rand_member = random.randint(0,1000)
    LIST.append(rand_member)


# sort list from min to max (without using sort())


def sort_list(lst):
    """
    Buble sort algorythm is used to sort given list
    :param lst:
    :return lst:
    """
    for i in range(len(lst)):
        swapped = False
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                swap_var = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = swap_var
                swapped = True
        # avoid unnecessary operations
        if not swapped:
            break
    return lst


print(sort_list(LIST))


# calculate average for even and odd numbers


def get_even_odd_avg(lst):
    """
    odds and evens quantity and sum are counted separately and then averages are calculated for each other.
    dictionary type returns more readable answer format
    :param lst:
    :return dict:
    """
    sum_odd, sum_even, cnt_odd, cnt_even = 0, 0, 0, 0
    for i in lst:
        if i in [0, 2]:
            continue
        elif i % 2 == 0:
            sum_even += i
            cnt_even += 1
        else:
            sum_odd += i
            cnt_odd += 1
    return {
        'odds': cnt_odd,
        'evens': cnt_even,
        'avg_odd': round(sum_odd/cnt_odd, 2),
        'avg_even': round(sum_even/cnt_even, 2)
    }


# print both average result in console


print(get_even_odd_avg(LIST))

