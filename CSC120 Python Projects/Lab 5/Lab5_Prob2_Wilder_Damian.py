

def main():
    nums = []
    keep_going = 'y'
    while keep_going.lower() != 'n':
        nums.append(int(input('Enter an integer from 1 to 10: ')))
        keep_going = input('Enter another integer?[y/n] ')
    print(f'Number list: {nums}')
    print(f'Largest element: {max(nums)}')
    print(f'Smallest element: {min(nums)}')
    print(f'Sum of all elements: {sum(nums)}')
    print(f'Length of list: {len(nums)}')
    print(f'Average: {sum(nums) / len(nums)}')
    nums.reverse()
    print(f'List reversed: {nums}')
    nums.insert(0, nums.pop(-1))
    print(f'Last element moved to front: {nums}')


main()
