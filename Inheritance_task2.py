class NumberList:
    def __init__(self):
        self.input_list = []  # Instance variable to store the input list

    def get_user_input(self):
        size = int(input('Enter the size of input_list: '))
        print('Enter the values:')
        for i in range(size):
            value = int(input())
            self.input_list.append(value)
            print(f'User-defined list: {self.input_list}')  # Print list once after input is complete

    def calculate_sum(self):
        return sum(self.input_list)  # Return sum of elements
        
    def find_max(self):
        return max(self.input_list)  # Return the maximum element
        
    def find_min(self):
        return min(self.input_list)  # Return the minimum element

    def display_results(self):
        print(f'Sum of elements is {self.calculate_sum()}')
        print(f'Maximum element is {self.find_max()}')
        print(f'Minimum element is {self.find_min()}')


# Main execution
if __name__ == "__main__":
    number_list = NumberList()
    number_list.get_user_input()  # Get user input and store in the object
    number_list.display_results()  # Display the results
