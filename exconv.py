def conv(feet,inches):
    inches = inches/12
    feet = feet + inches
    met = feet/3.28
    return met


if __name__ == "__main__":
    print(conv(5,11))
    