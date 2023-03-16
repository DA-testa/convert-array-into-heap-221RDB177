# python3


def build_heap(data):
    swaps = []
    
     n = len(data)

    # This loop sifts down all non-leaf nodes to create a max-heap
    for i in range(n // 2 - 1, -1, -1):
        j = i
        while 2 * j + 1 < n:
            k = j
            # Check if left child is smaller than current node
            if data[2 * j + 1] < data[k]:
                k = 2 * j + 1
            # Check if right child is smaller than current node and left child
            if 2 * j + 2 < n and data[2 * j + 2] < data[k]:
                k = 2 * j + 2
            if j != k:
                # Swap current node with smaller child
                data[j], data[k] = data[k], data[j]
                swaps.append((j, k))
                j = k
            else:
                break

    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
