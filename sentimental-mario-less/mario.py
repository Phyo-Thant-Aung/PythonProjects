def main():
    height = get_height()
    for i in range(1, height + 1):
        k = i
        j = height - i
        print(" " * j, end ="")
        print("#" * k)

def get_height():
    while True:
        try:
            n = int(input("Height: "))
            if 0 < n < 9:
                break
        except ValueError:
            print("Please key in an integer from 1 to 8 inclusive")
    return n

main()

