# age_validator.py

def validate_age(age):
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120.")
    return True


try:
    age = int(input("Enter your age: "))
    
    validate_age(age)
    print("Age accepted:", age)

except ValueError as e:
    print("Error:", e)