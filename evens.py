def even_number_of_evens(numbers):
    if isinstance(numbers, list):
            evens = 0
            for number in numbers:
                if number %2 == 0:
                    evens += 1
            if evens %2 == 0:
                if evens == 0:
                    return False
                else:
                    return True
            else:
                return False
    else:
        raise TypeError("Value should be a list")


if __name__ == "__main__":
    print(even_number_of_evens(5))
