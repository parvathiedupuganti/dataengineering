"""try:
    num1=int(input("Enter the number 1: "))
    num2=int(input("Enter the number 2: "))
    result = num1/num2
    print(num1,"/",num2,"=",result)
   
    x = [7,13,17,19,41]
    x[len(x)] = 23
    print(x)
    
    num = int(input("Enter the even number: "))
    assert num%2==0
except ZeroDivisionError:
    print("Error: Denominator cannot be zero")
except IndexError:
    print("Error: Index you are using is not present in the list, use insert method or check the index position")
except AssertionError:
    print("Error:  You have entered odd number");
else:
    print(num)
finally:
    num = 0
    print("The program is end")
    
"""
"""
yob = int(input("Enter your year of birth: "))
age = 2024-yob
if age < 18:
    raise Exception(f'Entry age for the PG Program is greater than 18 and your age is {age}')
"""

def divide(x,y):
    try:
        if y==0:
            raise ZeroDivisionError("Cannot divide by Zero")
        result = x/y
        return result
    except (ZeroDivisionError,AssertionError) as e:
        print("Error:",e)
    except TypeError as e:
        print("Error: There is string value instead of integer in denominator")

print(divide(10,"2"))


