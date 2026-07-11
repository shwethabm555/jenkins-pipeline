# Student Grade Calculator

## Project Description

Student Grade Calculator is a simple C application built using **CMake**.

The application accepts a student's name and marks for three subjects, calculates the total and average, assigns a grade, and displays whether the student has passed or failed.

---

## Features

- Accepts student name
- Accepts marks for 3 subjects
- Calculates total marks
- Calculates average
- Assigns grade (A, B, C, D, F)
- Displays Pass/Fail status

---

## Project Structure

```
StudentGradeCalculator/
│
├── CMakeLists.txt
├── main.c
└── README.md
```

---

## Requirements

- GCC Compiler
- CMake (Version 3.10 or later)

---

## Build Instructions

Create a build directory:

```bash
mkdir build
cd build
```

Generate build files:

```bash
cmake ..
```

Compile the project:

```bash
cmake --build .
```

Run the executable:

```bash
./StudentGradeCalculator
```

---

## Sample Output

```
=========================================
     Student Grade Calculator
=========================================

Enter Student Name : John

Enter Marks for Subject 1 : 90
Enter Marks for Subject 2 : 85
Enter Marks for Subject 3 : 80

=========================================
           Result Summary
=========================================
Student Name : John
Total Marks  : 255
Average      : 85.00
Grade        : B
Result       : PASS
=========================================
```

---

## Author

Your Name
