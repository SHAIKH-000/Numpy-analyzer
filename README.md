# NumPy Analyzer

A menu-driven Python project built using **NumPy** and **Object-Oriented Programming (OOP)** concepts.

This program allows users to create NumPy arrays and perform different array operations such as indexing, slicing, mathematical calculations, combining, splitting, searching, sorting, filtering, and statistical analysis.

---

## Features

### Array Creation

The program can create the following types of NumPy arrays:

- 1D Array
- 2D Array
- 3D Array

Example of a 2D array:

```text
[[10 20 30]
 [40 50 60]]
```

---

### Indexing and Slicing

Users can access a specific element from a 2D array using row and column indexes.

Example:

```text
Array:
[[10 20 30]
 [40 50 60]]

Row index: 0
Column index: 1

Output:
20
```

Users can also slice a part of a 2D array.

---

### Mathematical Operations

The program performs element-wise mathematical operations between two arrays of the same size.

Supported operations:

- Addition
- Subtraction
- Multiplication
- Division

Example:

```text
First Array:
[[10 20]
 [30 40]]

Second Array:
[[1 2]
 [3 4]]

Addition:
[[11 22]
 [33 44]]
```

---

### Combine and Split Arrays

The program supports the following array operations:

- Combine two arrays using `numpy.concatenate()`
- Split an array into multiple parts using `numpy.array_split()`

Example:

```text
Array:
[[10 20]
 [30 40]
 [50 60]]

Number of parts: 2
```

---

### Search, Sort and Filter

Users can perform the following actions:

- Search for an element using `numpy.argwhere()`
- Sort an array using `numpy.sort()`
- Filter elements greater than a selected value

Example:

```text
Array:
[10 50 20 80 30]

Filter value: 25

Output:
[50 80 30]
```

---

### Aggregates and Statistics

The program calculates different aggregate and statistical values from the array.

Supported calculations:

- Sum
- Mean
- Median
- Minimum value
- Maximum value
- Standard Deviation
- Variance
- Percentile
- Correlation Coefficient between two arrays

Example:

```text
Array:
[10 20 30 40 50]

Mean: 30.0
Median: 30.0
Maximum: 50
Minimum: 10
```

---

## OOP Concepts Used

This project uses basic Object-Oriented Programming concepts.

| OOP Concept | Implementation |
|---|---|
| Class | `DataAnalytics` |
| Object | `analyzer = DataAnalytics()` |
| Constructor | `__init__()` |
| Encapsulation | Private variable `self.__arr` |
| Private Method | `__check_array()` |
| Static Method | `message()` |
| Class Method | `show_total_arrays()` |
| Class Variable | `total_arrays` |

---

## Main Menu

```text
Welcome to the NumPy Analyzer!

1. Create a Numpy Array
2. Index or Slice Array
3. Mathematical Operations
4. Combine or Split Arrays
5. Search, Sort, or Filter Arrays
6. Compute Aggregates and Statistics
7. Show Total Arrays Created
8. Exit
```

---

## Requirements

You need Python and NumPy installed on your computer.

### Python Version

Use Python 3 or later.

### Install NumPy

Open terminal or command prompt and run:

```bash
pip install numpy
```

---

## How to Run the Project

1. Download or copy the project files.

2. Open the project folder in Visual Studio Code.

3. Make sure Python is installed.

4. Install NumPy:

```bash
pip install numpy
```

5. Run the Python file:

```bash
python main.py
```

If your Python command does not work, try:

```bash
py main.py
```

---

## Input Instructions

### Creating a 1D Array

```text
Enter elements separated by space: 10 20 30 40 50
```

### Creating a 2D Array

If rows are `2` and columns are `3`, then enter exactly `6` elements.

```text
Enter rows: 2
Enter columns: 3
Enter elements separated by space: 10 20 30 40 50 60
```

Output:

```text
[[10 20 30]
 [40 50 60]]
```

### Creating a 3D Array

If layers are `2`, rows are `2`, and columns are `2`, then enter exactly `8` elements.

```text
Enter layers: 2
Enter rows: 2
Enter columns: 2
Enter elements separated by space: 1 2 3 4 5 6 7 8
```

Output:

```text
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
```

---

## Important Notes

- Enter array elements separated by spaces.
- For 2D and 3D arrays, enter the correct number of elements according to the selected dimensions.
- Mathematical operations require a second array with the same size and shape as the first array.
- Combine operation requires a second array with the same shape as the current array.
- Split operation requires only one number: the number of parts.

Correct example:

```text
Enter number of parts: 2
```

Incorrect example:

```text
Enter number of parts: 10 60
```

- Indexing and slicing are intended for 2D arrays in this project.
- Correlation coefficient requires a second array of the same size.

---

## Technologies Used

- Python
- NumPy
- Object-Oriented Programming
- Visual Studio Code

---

## Project Structure

```text
project-Numpy-Analyzer/
│
├── main.py
└── README.md
```

---

## Author

**Shaikh Ayan**

Student project created for learning:

- Python Programming
- NumPy
- Array Operations
- Object-Oriented Programming
- Basic Data Analysis Concepts

---

## Project Status

Completed basic NumPy Analyzer project with menu-driven interface and OOP concepts.


