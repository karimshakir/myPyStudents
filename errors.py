def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")#this goes is'e'

    return dividend / divisor

grades = [1,2,3]

print ('Welcome to the average grade program.')
try:
    average  = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print('There are no grades yet in your list.')
    print(e)
else:    
    print(f"The average grade is {average}.")
finally:
    print("end of average block")