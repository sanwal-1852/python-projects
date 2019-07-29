def fib(n):
    """
    Recursively return the next term and the current term in the Fibonacci
    sequence.

    """
    if n == 1:
        return [1, 0]
    else:
        terms = fib(n - 1)
        terms = [terms[0] + terms[1], terms[0]]
        return terms


def validate_positive_integer():
    """
    Ask the user for input and only return when a positive integer under
    500 is given.
    """
    while True:
        s = input("Which term in the Fibonacci sequence you want to see? ")
        try:
            n = int(s)
            if n >= 500:
                print("Enter a number smaller than 500.")
            elif n > 0:
                return n
            else:
                print("Enter a positive integer.")
        except ValueError:
            print("Enter a positive integer.")


def main():
    n = validate_positive_integer()
    print(fib(n)[1])


if __name__ == "__main__":
    main()
