def safe_divide(a,b):
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        print('Error: Cannot divide by zero')
        return None
    
n = int(input('What is the numerator: ?'))
d = int(input('What is the denominator: ?'))
print(safe_divide(n,d))