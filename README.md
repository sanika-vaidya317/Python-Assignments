# Python Assignments

A collection of my Python programming lab assignments from college. Each assignment has its own folder containing the code, any input data files, and output screenshots where relevant.

## Assignments

| # | Folder | Topic |
|---|--------|-------|
| 1 | `Python Assignment 1` | Lists: managing tech fest participants (indexing, append, remove, sort, copy, combine) |
| 2 | `Python Assignment 2` | Conditionals: greatest of three numbers, and grade calculator from marks |
| 3 | `Python Assignment 3` | Functions: checking whether three sides form a right-angled triangle |
| 4 | `Python Assignment 4` | NumPy: adding two matrices entered by the user |
| 5 | `Python Assignment 5` | Strings: checking whether a string contains only ASCII characters |
| 6 | `Python Assignment 6` | Pandas: data preprocessing (missing values, duplicates) on CSV/Excel files |
| 7 | `Python Assignment 7` | Data visualization with Matplotlib: line, bar, scatter and heatmap plots, plus histogram, box plot and pie chart |

## Requirements

- Python 3.8 or above
- Libraries used across the assignments:

```
pip install numpy pandas matplotlib seaborn openpyxl
```

`openpyxl` is only needed to read `.xlsx` files in Assignment 6.

## How to run

1. Download or clone this repository.
2. Open a terminal in the assignment's folder.
3. Run the program:

```
python "python assignment 1.py"
```

Use the actual file name from the folder. Wrap it in quotes if it contains spaces.

Assignments 6 and 7 read data files, so keep the CSV/Excel file in the same folder as the script and type its name when the program asks (for example `messy_data.csv` or `sample_data_assignment_07.csv`).

## Outputs

- **Assignment 6** writes the cleaned data to `preprocessed_data.csv`.
- **Assignment 7** produces plots, saved as PNG screenshots in its folder.
