#include <stdio.h>

int main()
{
    char studentName[50];
    int subject1, subject2, subject3;
    int total;
    float average;
    char grade;

    printf("=========================================\n");
    printf("     Student Grade Calculator\n");
    printf("=========================================\n\n");

    printf("Enter Student Name : ");
    scanf("%49s", studentName);

    printf("Enter Marks for Subject 1 : ");
    scanf("%d", &subject1);

    printf("Enter Marks for Subject 2 : ");
    scanf("%d", &subject2);

    printf("Enter Marks for Subject 3 : ");
    scanf("%d", &subject3);

    total = subject1 + subject2 + subject3;
    average = total / 3.0;

    if (average >= 90)
        grade = 'A';
    else if (average >= 80)
        grade = 'B';
    else if (average >= 70)
        grade = 'C';
    else if (average >= 60)
        grade = 'D';
    else
        grade = 'F';

    printf("\n=========================================\n");
    printf("           Result Summary\n");
    printf("=========================================\n");

    printf("Student Name : %s\n", studentName);
    printf("Total Marks  : %d\n", total);
    printf("Average      : %.2f\n", average);
    printf("Grade        : %c\n", grade);

    if (grade == 'F')
        printf("Result       : FAIL\n");
    else
        printf("Result       : PASS\n");

    printf("=========================================\n");

    return 0;
}
