def calculate_score(input_data):
    score = 0
    company_size = input_data.get('company_size', '')
    if company_size == '1-50 employees':
        score += 5
    elif company_size == '51-200 employees':
        score += 10
    elif company_size == '201-1000 employees':
        score += 15
    else:
        score += 20

    budget = input_data.get('budget', '')
    if budget == 'Less than $10,000':
        score += 5
    elif budget == '$10,000 - $50,000':
        score += 10
    elif budget == '$50,001 - $100,000':
        score += 15
    else:
        score += 20

    industry = input_data.get('industry', '')
    if industry == 'Technology':
        score += 10
    elif industry == 'Finance':
        score += 8
    elif industry == 'Healthcare':
        score += 6
    elif industry == 'Retail':
        score += 4
    else:
        score += 2

    urgency = input_data.get('urgency', '')
    if urgency == 'Immediate (within 1 month)':
        score += 20
    elif urgency == 'Short-term (1-3 months)':
        score += 15
    elif urgency == 'Medium-term (3-6 months)':
        score += 10
    else:
        score += 5

    return score

output = [{'score': calculate_score(input)}]
