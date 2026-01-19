### 🔹 TASK 3: Conditional Statements & Logical Flow

# This program calculates the grade based on the score provided by the user.

def grade_calculate(score):
    try:
        score = float(score)
        if score < 0.0 or score > 100.0:
            return "Score must be between 0 and 100."
    except ValueError:
        return "Invalid input. Please enter a numeric value."

    if score >= 90.0 and score <= 100.0:
        return f"Grade is {'A'}"
    elif score >= 80.0 and score < 90.0:
        return f"Grade is {'B'}"
    elif score >= 70.0 and score < 80.0:
        return f"Grade is {'C'}"
    elif score >= 60.0 and score < 70.0:
        return f"Grade is {'D'}"
    else:
        return f"Grade is {'F'}"
    
score_input = input("Enter the score (0-100): ")
result = grade_calculate(score_input)

print(result)
    
