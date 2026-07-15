from payroll import calculate_salary


def main():
    print("=" * 45)
    print("     Employee Payroll Management System")
    print("=" * 45)

    employee_name = input("Enter Employee Name : ")

    basic_salary = float(input("Enter Basic Salary : "))

    payroll = calculate_salary(basic_salary)

    print("\n")
    print("=" * 45)
    print("Payroll Summary")
    print("=" * 45)

    print(f"Employee Name : {employee_name}")
    print(f"Basic Salary  : ₹{payroll['Basic Salary']:.2f}")
    print(f"HRA (20%)     : ₹{payroll['HRA']:.2f}")
    print(f"DA (10%)      : ₹{payroll['DA']:.2f}")
    print(f"Gross Salary  : ₹{payroll['Gross Salary']:.2f}")
    print(f"Tax (8%)      : ₹{payroll['Tax']:.2f}")
    print("-" * 45)
    print(f"Net Salary    : ₹{payroll['Net Salary']:.2f}")
    print("=" * 45)


if __name__ == "__main__":
    main()