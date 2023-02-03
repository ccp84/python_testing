def even_number_of_evens(numbers):
    if isinstance(numbers, list):
        return True
    else:
        raise TypeError("Value should be a list")


if __name__ == "__main__":
    print(even_number_of_evens(5))
