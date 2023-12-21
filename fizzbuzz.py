def main():
    print("\n This program tells the 'FizzBuzz'.")
    number = int(input("\n Enter number: "))
    if (0 == number % 3) and (0 == number % 5):
        print("\n FizzBuzz")
    elif 0 == number % 3:
        print("\n Fizz")
    elif 0 == number % 5:
        print("\n Buzz")
    else:
        print("\n Number is not FizzBuzz.")

main()

