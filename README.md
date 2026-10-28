# Python Assignments

My Python programming lab assignments from college, covering lists, conditionals, functions, NumPy, strings, Pandas and Matplotlib. Each assignment has its own folder with the code, any data files it needs, and sample output shown below.

## Contents

- [Assignment overview](#assignment-overview)
- [Repository structure](#repository-structure)
- [Requirements](#requirements)
- [How to run](#how-to-run)
- [Sample outputs](#sample-outputs)

## Assignment overview

| # | Topic | What the program does | Concepts used |
|---|-------|-----------------------|---------------|
| 1 | Lists | Manages a list of tech fest participants: edit, add, remove, sort, back up and combine lists | list methods, slicing, `in` operator |
| 2 | Conditionals | Part 1 finds the greatest of three numbers. Part 2 converts marks into a grade | `if / elif / else` |
| 3 | Functions | Checks whether three sides form a right-angled triangle | functions, `sorted()` |
| 4 | NumPy | Reads two matrices from the user and adds them | nested loops, `numpy` arrays |
| 5 | Strings | Checks whether a string contains only ASCII characters | string handling, `all()` |
| 6 | Pandas | Cleans a dataset: fills missing values, removes duplicates, saves the result | `pandas`, data preprocessing |
| 7 | Matplotlib | Plots student data: histogram, box plot and pie chart, and prints averages | `matplotlib`, `pandas` |

## Repository structure

```
Python-Assignments/
├── README.md
├── Python Assignment 1/
├── Python Assignment 2/
├── Python Assignment 3/
├── Python Assignment 4/
├── Python Assignment 5/
├── Python Assignment 6/
│   ├── messy_data.csv
│   ├── messy_data.xlsx
│   └── python assignment 6.py
└── Python Assignment 7/
    ├── sample_data_assignment_07.csv
    ├── python assignment 7.py
    └── plot images (.png)
```

## Requirements

- Python 3.8 or above
- Libraries:

```
pip install numpy pandas matplotlib seaborn openpyxl
```

`openpyxl` is only needed to read `.xlsx` files in Assignment 6.

## How to run

1. Download or clone this repository.
2. Open a terminal inside the assignment's folder.
3. Run the program (use the real file name, in quotes because it contains spaces):

```
python "python assignment 1.py"
```

Assignments 6 and 7 read data files. Keep the CSV or Excel file in the same folder as the script and type its name when asked (for example `messy_data.csv`).

## Sample outputs

Click an assignment to expand it. In the runs below, the values after each prompt are the example inputs that were typed.

---

<details>
<summary><b>Assignment 1:</b> Lists (tech fest participants)</summary>

<br>

**Task:** manage a participant list, then combine it with a second list.

**Output:**

```
third student: Rohan
Updated list 1: ['Aarav', 'Isha', 'Rohan Patil', 'Sneha', 'Kabir']
updated list 2: ['Aarav', 'Isha', 'Rohan Patil', 'Sneha', 'Kabir', 'Ananya', 'Vihaan']
updated list 3: ['Aarav', 'Isha', 'Rohan Patil', 'Sneha', 'Ananya', 'Vihaan']
total no of registered students: 6
Is Isha registered? True
alphabetical order: ['Aarav', 'Ananya', 'Isha', 'Rohan Patil', 'Sneha', 'Vihaan']
backup list: ['Aarav', 'Ananya', 'Isha', 'Rohan Patil', 'Sneha', 'Vihaan']
AI hackathon participants: ['Meera', 'Arjun', 'Isha']
all participants: ['Aarav', 'Ananya', 'Isha', 'Rohan Patil', 'Sneha', 'Vihaan', 'Meera', 'Arjun', 'Isha']
Final list of participants: ['Aarav', 'Ananya', 'Isha', 'Rohan Patil', 'Sneha', 'Vihaan', 'Meera', 'Arjun', 'Isha']
backup list of participants: ['Aarav', 'Ananya', 'Isha', 'Rohan Patil', 'Sneha', 'Vihaan']
combined participants list: ['Aarav', 'Ananya', 'Isha', 'Rohan Patil', 'Sneha', 'Vihaan', 'Meera', 'Arjun', 'Isha']
```

</details>

<details>
<summary><b>Assignment 2:</b> Conditionals</summary>

<br>

### Part 1: Greatest of three numbers

**Test 1: one number is clearly the greatest**

```
First no:12
Second no:45
Third no:30
b is greatest
```

**Test 2: all numbers equal**

```
First no:5
Second no:5
Third no:5
All numbers are equal
```

### Part 2: Grade calculator

**Test: marks in the 80 to 89 range**

```
enter maths marks85
Grade A+
```

</details>

<details>
<summary><b>Assignment 3:</b> Right-angled triangle</summary>

<br>

**Test 1: valid right-angled triangle (3, 4, 5)**

```
side 1:3
side 2:4
side 3:5
It is a right angled triangle
```

**Test 2: not a right-angled triangle (2, 3, 4)**

```
side 1:2
side 2:3
side 3:4
It is not a right angled triangle
```

</details>

<details>
<summary><b>Assignment 4:</b> Matrix addition (NumPy)</summary>

<br>

**Test: adding two 2x2 matrices**

```
Enter the number of rows: 2
Enter the number of columns: 2
Enter the elements of the first matrix:
Enter A[1][1]: 1
Enter A[1][2]: 2
Enter A[2][1]: 3
Enter A[2][2]: 4
Enter the elements of the second matrix:
Enter B[1][1]: 5
Enter B[1][2]: 6
Enter B[2][1]: 7
Enter B[2][2]: 8

Matrix A:
[[1 2]
 [3 4]]

Matrix B:
[[5 6]
 [7 8]]

Addition of A and B:
[[ 6  8]
 [10 12]]
```

</details>

<details>
<summary><b>Assignment 5:</b> ASCII check</summary>

<br>

**Test 1: ordinary text and digits**

```
Enter a string: Hello123
The string contains only ASCII characters.
```

**Test 2: contains an accented character**

```
Enter a string: héllo
The string contains non-ASCII characters.
```

</details>

<details>
<summary><b>Assignment 6:</b> Data preprocessing (Pandas)</summary>

<br>

**Input file:** `messy_data.csv`, 10 rows with missing values and duplicate rows.

**Step 1: original data (NaN marks missing values)**

```
  Student   Age  Marks  Attendance    City
0    Amit  20.0   75.0        85.0    Pune
1  Bhavna  21.0   82.0         NaN  Mumbai
2  Chetan   NaN   68.0        78.0    Pune
3    Diya  20.0   90.0        95.0     NaN
4    Esha  22.0    NaN        80.0  Mumbai
5  Farhan  21.0   85.0        92.0    Pune
6    Amit  20.0   75.0        85.0    Pune
7   Gauri  20.0   78.0         NaN  Nashik
8   Harsh   NaN   70.0        88.0    Pune
9  Bhavna  21.0   82.0         NaN  Mumbai
```

**Step 2: count of missing values per column**

```
Student       0
Age           2
Marks         1
Attendance    3
City          1
dtype: int64
```

**Step 3: after cleaning** (numbers filled with the column mean, text filled with the most common value, duplicates removed)

```
  Student     Age      Marks  Attendance    City
0    Amit  20.000  75.000000   85.000000    Pune
1  Bhavna  21.000  82.000000   86.142857  Mumbai
2  Chetan  20.625  68.000000   78.000000    Pune
3    Diya  20.000  90.000000   95.000000    Pune
4    Esha  22.000  78.333333   80.000000  Mumbai
5  Farhan  21.000  85.000000   92.000000    Pune
6   Gauri  20.000  78.000000   86.142857  Nashik
7   Harsh  20.625  70.000000   88.000000    Pune
```

**Result:** the cleaned data is saved as `preprocessed_data.csv`.

</details>

<details>
<summary><b>Assignment 7:</b> Data visualization (Matplotlib)</summary>

<br>

**Input file:** `sample_data_assignment_07.csv`, six students with Maths, Python, Attendance and City.

**Averages printed by the program**

```
Average Maths score: 78.67
Average Python score: 80.50
Average Attendance: 86.67
```

**Histogram of Python scores** (dashed line marks the average)

![Histogram of Python scores](Python%20Assignment%207/assignment_07_python_histogram.png)

**Box plot of Maths and Python scores**

![Box plot of Maths and Python scores](Python%20Assignment%207/assignment_07_score_box_plot.png)

**Number of students from each city**

![Pie chart of students by city](Python%20Assignment%207/assignment_07_city_pie_chart.png)

</details>
