#Royce Daniel, 3/27/2026 "Addition drone"
def sum_numbers_from_file():
    total = 0

    try:
        f = open("numbers.txt", "r")

        for line in f:
            try:
                num = int(line.strip())
                total += num
            except ValueError:
                print("Skipping invalid value:", line.strip())

        f.close()

        print("Total:", total)

    except IOError:
        print("Error: Could not open file.")


if __name__ == '__main__':
    sum_numbers_from_file()