def build_heap(data):
    swaps = []
    n = len(data)
    
    # Starting from the last parent node, recursively sort the subtree rooted at i
    for i in range(n // 2, -1, -1):
        sort(data, i, swaps)

    return swaps


def sort(data, i, swaps):
    n = len(data)
    right = 2 * i + 2
    left = 2 * i + 1
    lir = i 
    
    # If the left child is smaller than the current root, set it as the new root
    if left < n and data[left] < data[lir]:
        lir = left
        
    # If the right child is smaller than the current root, set it as the new root
    if right < n and data[right] < data[lir]:
        lir = right
        
    # If the root has changed, swap the values and add the indices to the swaps list
    if i != lir:
        data[i], data[lir] = data[lir], data[i]
        swaps.append((i, lir))
        
        # Recursively sort the subtree rooted at the new root
        sort(data, lir, swaps)


def main():
    test = input()
    
    # If F is in the input, read data from a file
    if 'F' in test:
        test_file = input()
        with open("tests/" + test_file, 'r') as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
    else:
        # Otherwise, read data from the command line
        n = int(input())
        data = list(map(int, input().split()))

    assert len(data) == n
    
    # Build the heap and get the swaps list
    swaps = build_heap(data)

    print(len(swaps))
    
    # Print the indices of each swap
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
