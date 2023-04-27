#!/usr/bin/python3
''' Define a peak-finding algorithm '''


def find_peak(list_of_integers):
    ''' Find a peak in a list of unsorted integers '''
    loi = list_of_integers
    if loi == []:
        return None

    size = len(loi)
    if size == 1:
        return loi[0]
    if size == 2:
        return max(loi)

    mid = int(size / 2)
    if loi[mid - 1] < loi[mid] > loi[mid + 1]:
        return loi[mid]
    if loi[mid + 1] > loi[mid - 1]:
        return find_peak(loi[mid:])
    return find_peak(loi[:mid])
