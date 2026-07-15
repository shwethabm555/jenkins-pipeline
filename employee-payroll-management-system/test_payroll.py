import pytest
from payroll import calculate_salary


def test_salary_calculation():
    result = calculate_salary(50000)

    assert result["HRA"] == 10000
    assert result["DA"] == 5000
    assert result["Gross Salary"] == 65000
    assert result["Tax"] == 5200
    assert result["Net Salary"] == 59800


def test_zero_salary():
    result = calculate_salary(0)

    assert result["Net Salary"] == 0


def test_negative_salary():
    with pytest.raises(ValueError):
        calculate_salary(-1000)