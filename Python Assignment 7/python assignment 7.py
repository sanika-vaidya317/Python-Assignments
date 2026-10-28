import os

import matplotlib.pyplot as plt
import pandas as pd


filename = input("Enter csv file name: ").strip()

if not os.path.exists(filename):
    print(f"Error: file '{filename}' was not found")
    raise SystemExit(1)

df = pd.read_csv(filename)

required = ["Student", "Maths", "Python", "Attendance", "City"]
missing = [column for column in required if column not in df.columns]
if missing:
    print("Error: csv is missing columns", ",".join(missing))
    raise SystemExit(1)

print("\nDataset:")
print(df)

average_maths = df["Maths"].mean()
average_python = df["Python"].mean()
average_attendance = df["Attendance"].mean()

print(f"\nAverage Maths score: {average_maths:.2f}")
print(f"Average Python score: {average_python:.2f}")
print(f"Average Attendance: {average_attendance:.2f}")

plt.figure(figsize=(7, 4.5))
plt.hist(
    df["Python"],
    bins=5,
    color="blue",
    edgecolor="black",
    label="Python scores",
)
plt.axvline(
    average_python,
    color="red",
    linestyle="dashed",
    label=f"Average Python score: {average_python:.2f}",
)
plt.title("Histogram of Python Scores")
plt.xlabel("Python Score")
plt.ylabel("Number of Students")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

plt.figure(figsize=(7, 4.5))
box = plt.boxplot([df["Maths"], df["Python"]], patch_artist=True)
plt.xticks([1, 2], ["Maths", "Python"])
for patch, color in zip(box["boxes"], ["lightgreen", "lightblue"]):
    patch.set_facecolor(color)
plt.title("Box Plot of Maths and Python Scores")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.legend(box["boxes"], ["Maths", "Python"], loc="lower right")
plt.grid(True, axis="y", alpha=0.3)
plt.show()

city_counts = df["City"].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(
    city_counts,
    labels=city_counts.index,
    autopct="%1.1f%%",
    startangle=90,
    wedgeprops={"edgecolor": "white"},
)
plt.title("Distribution of Students by City")
plt.legend(city_counts.index, title="City", loc="best")
plt.show()
