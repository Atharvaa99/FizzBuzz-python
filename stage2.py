def fizzBuzz(val):
    if val % 3 == 0 and val % 7 == 0:
        return "FizzBuzz"
    elif val % 7 == 0:
        return "Buzz"
    elif  val % 3 == 0:
        return "Fizz"
    else:
        return str(val)

num = int(input())
greeting = "Welcome to FizzBuzz!"
print(greeting)
result = fizzBuzz(num)
print(result)