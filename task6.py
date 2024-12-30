def collect_values():
    items = []
    total = int(input('Enter the number of values to store: '))
    print('Enter the values:')
    for _ in range(total):
        items.append(int(input()))
    return items

def count_frequency(elements, target_value):
    occurrences = 0
    for element in elements:
        if element == target_value:
            occurrences += 1
    return occurrences

def main():
    values = collect_values()
    target = int(input('Enter the value to search: '))
    frequency = count_frequency(values, target)
    print(f'{target} appears {frequency} times')

if __name__ == '__main__':
    main()
