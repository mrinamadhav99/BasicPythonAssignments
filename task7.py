def collect_values():
    numbers = []
    count = int(input('Enter the number of values to store: '))
    print('Enter the values:')
    for _ in range(count):
        numbers.append(int(input()))
    return numbers

def find_maximum(numbers):
    max_value = 0
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

def find_minimum(numbers):
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def main():
    numbers = collect_values()
    max_value = find_maximum(numbers)
    min_value = find_minimum(numbers)
    total_sum = calculate_sum(numbers)
    print('Maximum number:', max_value)
    print('Minimum number:', min_value)
    print('Sum of numbers:', total_sum)

if __name__ == '__main__':
    main()
