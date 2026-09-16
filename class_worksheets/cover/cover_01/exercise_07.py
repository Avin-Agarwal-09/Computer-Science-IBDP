def check_loan_eligibility(salary, years_of_service):
    if salary < 30000:
        return "Ineligible - Low Salary"
    elif years_of_service < 2:
        return "Ineligible - Not Enough Years of Service"
    else:
        return "Eligible"
