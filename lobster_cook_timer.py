#This script is specific to boiling lobster(s). If using an alternate cooking method, cook times will vary.

def calculate_cooking_time(weight_in_pounds):
    if weight_in_pounds <= 0:
        return 0  # No cooking time for zero or negative weight
    elif weight_in_pounds == 1:
        return 10  # 10 minutes for the first pound
    else:
        return 10 + (weight_in_pounds - 1) * 3  # 10 minutes for the first pound + 3 minutes for each additional pound

def main():
    calculate_cooking_time

# Input weight in pounds
weight_in_pounds = float(input("Enter the weight in pounds: "))

# Calculate cooking time
cooking_time = calculate_cooking_time(weight_in_pounds)

# Display the cooking time
print(f"The cooking time for boiling a lobster of {weight_in_pounds} pounds is {cooking_time} minutes.\nNOTE: Do not start the timer until the water has returned to a roaring boil")


if __name__ == "__main__":
    main()