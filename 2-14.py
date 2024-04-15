def calculate_tax_and_show_calculation(income):
    thresholds = [0, 12000000, 46000000, 88000000, 150000000]
    rates = [0.06, 0.15, 0.24, 0.35, 0.38]
    tax = 0

    for i in range(len(rates)):
        max_income_this_rate = thresholds[i + 1] if i < len(thresholds) - 1 else income

        taxable_income = min(income, max_income_this_rate) - thresholds[i]

        tax_part = taxable_income * rates[i]
        tax += tax_part

        if income <= max_income_this_rate:
            break

    return tax


income = int(input("연 소득을 입력하세요: "))

tax = calculate_tax_and_show_calculation(income)

income_after_tax = income - tax

print(f"총 세금: {tax:,.0f}원")
print(f"세후 소득: {income_after_tax:,.0f}원")
