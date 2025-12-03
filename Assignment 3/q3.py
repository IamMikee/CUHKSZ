from typing import List


def quick_sort(arr: List[int]) -> List[int]:
    """
    Perform quick-sort on a list of integers while tracking all comparisons.
    Parameters
    ----------
    arr : List[int]
        The input list.
    Returns
    -------
    sorted_arr : List[int]
        Sorted version of arr.
    """
    # TODO: implement quick-sort with:
    #   - partitioning
    #   - recursive sorting
    #   - tracking (count, sequence)
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less, more = [], []

    for num in arr[1:]:
        if num <= pivot:
            less.append(num)
        else:
            more.append(num)

    less = quick_sort(less)
    more = quick_sort(more)

    return less+[pivot]+more