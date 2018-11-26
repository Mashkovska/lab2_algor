from math import floor


def place_cow(stall, cow, dis):
    counter = 1
    current_element = stall[0]
    for i in range(0, len(stall)):
        next_element = stall[i]
        if next_element - current_element >= dis:
            counter += 1
            if counter == cow:
                return 1
            current_element = next_element
    return 0


def binary_search(stajnia, cow):
    stajnia.sort()
    length = len(stajnia)
    start_index = 0
    end_index = stajnia[length - 1]

    while end_index - start_index > 1:
        mid_index = start_index + floor((end_index - start_index) / 2)

        if place_cow(stajnia, cow, mid_index):
            start_index = mid_index
        else:
            end_index = mid_index
    print(start_index)


if __name__ == '__main__':
    s, c = input().split(' ')
    stack = []

    for j in range(int(s)):
        stack.append(int(input()))

    binary_search(stack, int(c))
