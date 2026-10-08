# NumPy Analyzer

A beginner-friendly Python project to create and perform operations on NumPy arrays through a simple menu-driven program.

This project allows users to create 1D, 2D, and 3D arrays and perform common array operations such as indexing, slicing, mathematical calculations, combining arrays, and splitting arrays.

## Features

- Create 1D NumPy arrays
- Create 2D NumPy arrays
- Create 3D NumPy arrays
- Perform indexing on a 2D array
- Perform slicing on a 2D array
- Add two arrays
- Subtract two arrays
- Multiply two arrays
- Divide two arrays
- Combine two arrays
- Split an array into smaller parts
- Simple menu-driven interface

## Technologies Used

- Python
- NumPy

## Project Structure

```text
numpy-analyzer/
│
├── numpy_analyzer.py
└── README.md
```

> Rename `numpy_analyzer.py` above if your Python file has a different name.

## Installation

First, make sure Python is installed on your computer.

Install NumPy using the following command:

```bash
pip install numpy
```

## How to Run

1. Download or clone this repository.

2. Open the project folder in VS Code or any code editor.

3. Run the Python file:

```bash
python numpy_analyzer.py
```

## Main Menu

When you run the program, you will see the following menu:

```text
Welcome to the NumPy Analyzer!
1. Create a Numpy Array
2. Index or Slice Array
3. Mathematical Operations
4. Combine or Split Arrays
6. Exit
```

## Example: Create a 2D Array

```text
Enter your choice: 1

Select the type of array to create:
1. 1D Array
2. 2D Array
3. 3D Array

Enter your choice: 2
Enter the number of rows: 2
Enter the number of columns: 3
Enter 6 elements separated by space: 10 20 30 40 50 60
```

Output:

```text
Array created successfully:
[[10 20 30]
 [40 50 60]]
```

## Example: Array Addition

```text
Choose a mathematical operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division

Enter your choice: 1
Enter the same-size array elements (6 elements separated by space): 5 5 5 5 5 5
```

Output:

```text
Original Array:
[[10 20 30]
 [40 50 60]]

Second Array:
[[5 5 5]
 [5 5 5]]

Result of Addition:
[[15 25 35]
 [45 55 65]]
```

## Concepts Used

- Classes and Objects
- Constructor: `__init__()`
- Private Variable: `self.__arr`
- Conditional Statements: `if`, `elif`, `else`
- Loops: `while` and `for`
- User Input
- NumPy Arrays
- Array Indexing
- Array Slicing
- Array Reshaping
- Array Mathematical Operations
- Array Concatenation
- Array Splitting

## Important NumPy Functions

| Function | Purpose |
|---|---|
| `np.array()` | Creates a NumPy array |
| `reshape()` | Changes a 1D list of values into rows and columns |
| `np.concatenate()` | Combines two arrays |
| `np.array_split()` | Splits one array into multiple parts |
| `self.__arr.size` | Counts total elements in the array |
| `self.__arr.shape` | Gives the size/structure of the array |
| `self.__arr.ndim` | Gives the number of dimensions of the array |

## Requirements

```text
Python 3.x
NumPy
```

## Author

**Your Name**

Student | Python & NumPy Learner

---

⭐ If you found this project useful, consider giving it a star!
