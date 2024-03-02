#!/usr/bin/env python3

list = [6, 2, 9, 4, 3, 8, 0, 5, 1, 7]
# list2 = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        print()
        print("Left", left)
        print("Right", right)

        merge_sort(left)
        merge_sort(right)

        left_i = right_i = main_i = 0

        print("Section", left + right)
        print()
        while left_i < len(left) and right_i < len(right):
            message += f"{left[left_i]} <= {right[right_i]}"

            if left[left_i] <= right[right_i]:
                array[main_i] = left[left_i]
                message += " True \n"
                left_i += 1

            else:
                array[main_i] = right[right_i]
                message += " False \n"
                right_i += 1

            main_i += 1
            print(message)

        while left_i < len(left):
            array[main_i] = left[left_i]
            left_i += 1
            main_i += 1

        while right_i < len(right):
            array[main_i] = right[right_i]
            right_i += 1
            main_i += 1

        print()
        print("Sorted Section", array)
        print()


merge_sort(list)
