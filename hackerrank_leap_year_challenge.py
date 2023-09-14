def is_leap(year):
    leap = False
# Check if the year is evenly divisible by 4
    if year % 4 == 0:
        leap = True
            
        # Check if the year is evenly divisible by 100
        if year % 100 == 0:
            leap = False
                
            # Check if the year is evenly divisible by 400
            if year % 400 == 0:
                leap = True
    return leap

year = int(input())
print(is_leap(year))