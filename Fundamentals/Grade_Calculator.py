def calcualte_grade(score):
    if score <= 0:
        return "Invalid Score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
user_input = int(input("Enter your score:"))
grade = calcualte_grade(user_input)
print("Your grade is:", grade)