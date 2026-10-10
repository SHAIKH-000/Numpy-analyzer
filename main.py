import numpy as np


class DataAnalytics:

    total_arrays = 0

    def __init__(self):
        self.__arr = None

    # Private method
    def __check_array(self):
        if self.__arr is None:
            print("Please create an array first!")
            return False
        return True

    # Static method
    @staticmethod
    def message():
        print("Welcome to NumPy Analyzer")

    # Class method
    @classmethod
    def show_total_arrays(cls):
        print("Total arrays created:", cls.total_arrays)

    def create_array(self):
        print("\nSelect Array Type")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        choice = input("Enter your choice: ")

        if choice == "1":
            elements = list(map(int, input(
                "Enter elements separated by space: "
            ).split()))

            self.__arr = np.array(elements)

        elif choice == "2":
            rows = int(input("Enter rows: "))
            cols = int(input("Enter columns: "))

            elements = list(map(int, input(
                "Enter elements separated by space: "
            ).split()))

            self.__arr = np.array(elements).reshape(rows, cols)

        elif choice == "3":
            layers = int(input("Enter layers: "))
            rows = int(input("Enter rows: "))
            cols = int(input("Enter columns: "))

            elements = list(map(int, input(
                "Enter elements separated by space: "
            ).split()))

            self.__arr = np.array(elements).reshape(layers, rows, cols)

        else:
            print("Invalid choice!")
            return

        DataAnalytics.total_arrays += 1

        print("\nArray created successfully:")
        print(self.__arr)

    def index_slice(self):
        if not self.__check_array():
            return

        print("\n1. Indexing")
        print("2. Slicing")

        choice = input("Enter your choice: ")

        if choice == "1":
            row = int(input("Enter row index: "))
            col = int(input("Enter column index: "))

            print("Element:", self.__arr[row, col])

        elif choice == "2":
            row_start = int(input("Enter row start: "))
            row_end = int(input("Enter row end: "))
            col_start = int(input("Enter column start: "))
            col_end = int(input("Enter column end: "))

            print("Sliced Array:")
            print(self.__arr[row_start:row_end, col_start:col_end])

        else:
            print("Invalid choice!")

    def mathematical_operations(self):
        if not self.__check_array():
            return

        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Enter your choice: ")

        elements = list(map(int, input(
            f"Enter {self.__arr.size} elements for second array: "
        ).split()))

        second_array = np.array(elements).reshape(self.__arr.shape)

        if choice == "1":
            print("Addition:")
            print(self.__arr + second_array)

        elif choice == "2":
            print("Subtraction:")
            print(self.__arr - second_array)

        elif choice == "3":
            print("Multiplication:")
            print(self.__arr * second_array)

        elif choice == "4":
            print("Division:")
            print(self.__arr / second_array)

        else:
            print("Invalid choice!")

    def combine_split_arrays(self):
        if not self.__check_array():
            return

        print("\n1. Combine Arrays")
        print("2. Split Array")

        choice = input("Enter your choice: ")

        if choice == "1":
            elements = list(map(int, input(
                f"Enter {self.__arr.size} elements for second array: "
            ).split()))

            second_array = np.array(elements).reshape(self.__arr.shape)

            print("Combined Array:")
            print(np.concatenate((self.__arr, second_array)))

        elif choice == "2":
            parts = int(input("Enter number of parts: "))

            print("Split Arrays:")
            print(np.array_split(self.__arr, parts))

        else:
            print("Invalid choice!")

    def search_sort_filter(self):
        if not self.__check_array():
            return

        print("\n1. Search")
        print("2. Sort")
        print("3. Filter")

        choice = input("Enter your choice: ")

        if choice == "1":
            value = int(input("Enter element to search: "))
            print(np.argwhere(self.__arr == value))

        elif choice == "2":
            print("Sorted Array:")
            print(np.sort(self.__arr))

        elif choice == "3":
            value = int(input("Show elements greater than: "))
            print("Filtered Array:")
            print(self.__arr[self.__arr > value])

        else:
            print("Invalid choice!")

    def aggregates_statistics(self):
        if not self.__check_array():
            return

        print("\n1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Minimum")
        print("5. Maximum")
        print("6. Standard Deviation")
        print("7. Variance")
        print("8. Percentile")
        print("9. Correlation Coefficient")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Sum:", np.sum(self.__arr))

        elif choice == "2":
            print("Mean:", np.mean(self.__arr))

        elif choice == "3":
            print("Median:", np.median(self.__arr))

        elif choice == "4":
            print("Minimum:", np.min(self.__arr))

        elif choice == "5":
            print("Maximum:", np.max(self.__arr))

        elif choice == "6":
            print("Standard Deviation:", np.std(self.__arr))

        elif choice == "7":
            print("Variance:", np.var(self.__arr))

        elif choice == "8":
            percentile = int(input("Enter percentile: "))
            print("Percentile:", np.percentile(self.__arr, percentile))

        elif choice == "9":
            elements = list(map(int, input(
                f"Enter {self.__arr.size} elements for second array: "
            ).split()))

            second_array = np.array(elements).reshape(self.__arr.shape)

            print("Correlation Coefficient:")
            print(np.corrcoef(self.__arr.flatten(), second_array.flatten())[0, 1])

        else:
            print("Invalid choice!")


DataAnalytics.message()

analyzer = DataAnalytics()


while True:
    print("\nWelcome to the NumPy Analyzer!")
    print("1. Create a Numpy Array")
    print("2. Index or Slice Array")
    print("3. Mathematical Operations")
    print("4. Combine or Split Arrays")
    print("5. Search, Sort, or Filter Arrays")
    print("6. Compute Aggregates and Statistics")
    print("7. Show Total Arrays Created")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        analyzer.create_array()

    elif choice == "2":
        analyzer.index_slice()

    elif choice == "3":
        analyzer.mathematical_operations()

    elif choice == "4":
        analyzer.combine_split_arrays()

    elif choice == "5":
        analyzer.search_sort_filter()

    elif choice == "6":
        analyzer.aggregates_statistics()

    elif choice == "7":
        DataAnalytics.show_total_arrays()

    elif choice == "8":
        print("Thank you for using the NumPy Analyzer!")
        break

    else:
        print("Invalid choice!")
