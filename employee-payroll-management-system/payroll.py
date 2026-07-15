def calculate_salary(basic_salary):
    """
    Calculate employee payroll.

    HRA = 20%
    DA = 10%
    TAX = 8%
    """

    if basic_salary < 0:
        raise ValueError("Basic salary cannot be negative.")

    hra = basic_salary * 0.20
    da = basic_salary * 0.10

    gross_salary = basic_salary + hra + da

    tax = gross_salary * 0.08

    net_salary = gross_salary - tax

    return {
        "Basic Salary": basic_salary,
        "HRA": hra,
        "DA": da,
        "Gross Salary": gross_salary,
        "Tax": tax,
        "Net Salary": net_salary
    }