import numpy as np


class DataAnalytics:

    def __init__(self):
        self.__arr = None

    def create_array(self):
        print("Select the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        choice = input("Enter your choice: ")

        if choice == "1":
            elements = list(map(int, input("Enter elements separated by space: ").split()))
            self.__arr = np.array(elements)

        elif choice == "2":
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))

            elements = list(map(int, input(
                f"Enter {rows * cols} elements separated by space: "
            ).split()))

            self.__arr = np.array(elements).reshape(rows, cols)

        elif choice == "3":
            layers = int(input("Enter the number of layers: "))
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))

            elements = list(map(int, input(
                f"Enter {layers * rows * cols} elements separated by space: "
            ).split()))

            self.__arr = np.array(elements).reshape(layers, rows, cols)

        else:
            print("Invalid choice!")
            return

        print("\nArray created successfully:")
        print(self.__arr)

    def index_slice(self):
        if self.__arr is None:
            print("Please create an array first!")
            return

        if self.__arr.ndim != 2:
            print("For now, indexing and slicing work only with a 2D array.")
            return

        print("\nChoose an operation:")
        print("1. Indexing")
        print("2. Slicing")
        print("3. Go Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            row = int(input("Enter the row index: "))
            col = int(input("Enter the column index: "))
            print("Element:", self.__arr[row][col])

        elif choice == "2":
            row_range = input("Enter the row range (start:end): ")
            col_range = input("Enter the column range (start:end): ")

            row_start, row_end = map(int, row_range.split(":"))
            col_start, col_end = map(int, col_range.split(":"))

            sliced_array = self.__arr[row_start:row_end, col_start:col_end]

            print("\nSliced Array:")
            print(sliced_array)

        elif choice == "3":
            return

        else:
            print("Invalid choice!")

    def mathematical_operations(self):
        if self.__arr is None:
            print("Please create an array first!")
            return

        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Enter your choice: ")

        total_elements = self.__arr.size

        elements = list(map(int, input(
            f"Enter the same-size array elements ({total_elements} elements separated by space): "
        ).split()))

        second_array = np.array(elements).reshape(self.__arr.shape)

        print("\nOriginal Array:")
        print(self.__arr)

        print("\nSecond Array:")
        print(second_array)

        if choice == "1":
            result = self.__arr + second_array
            print("\nResult of Addition:")
            print(result)

        elif choice == "2":
            result = self.__arr - second_array
            print("\nResult of Subtraction:")
            print(result)

        elif choice == "3":
            result = self.__arr * second_array
            print("\nResult of Multiplication:")
            print(result)

        elif choice == "4":
            result = self.__arr / second_array
            print("\nResult of Division:")
            print(result)

        else:
            print("Invalid choice!")

    def combine_split_arrays(self):
        if self.__arr is None:
            print("Please create an array first!")
            return

        if self.__arr.ndim != 2:
            print("For now, combine and split work only with a 2D array.")
            return

        print("\nCombine or Split Arrays:")
        print("1. Combine Arrays")
        print("2. Split Array")
        print("3. Go Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            rows = self.__arr.shape[0]
            cols = self.__arr.shape[1]

            elements = list(map(int, input(
                f"Enter {rows * cols} elements for second array: "
            ).split()))

            second_array = np.array(elements).reshape(rows, cols)

            combined_array = np.concatenate((self.__arr, second_array))

            print("\nFirst Array:")
            print(self.__arr)

            print("\nSecond Array:")
            print(second_array)

            print("\nCombined Array:")
            print(combined_array)

        elif choice == "2":
            parts = int(input("Enter number of parts: "))

            split_arrays = np.array_split(self.__arr, parts)

            print("\nSplit Arrays:")

            for array in split_arrays:
                print(array)

        elif choice == "3":
            return

        else:
            print("Invalid choice!")


analyzer = DataAnalytics()


while True:
    print("\nWelcome to the NumPy Analyzer!")
    print("1. Create a Numpy Array")
    print("2. Index or Slice Array")
    print("3. Mathematical Operations")
    print("4. Combine or Split Arrays")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        analyzer.create_array()

    elif choice == "2":
        analyzer.index_slice()

    elif choice == "3":
        analyzer.mathematical_operations()

    elif choice == "4":
        analyzer.combine_split_arrays()

    elif choice == "6":
        print("Thank you for using the NumPy Analyzer! Goodbye!")
        break

    else:
        print("Invalid choice!")