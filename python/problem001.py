from timer import Timer


def main():
    Timer()

    total = 0
    for i in range(3, 1000, 3):
        total = total + i

    for i in range(5, 1000, 5):
        total = total + i

    for i in range(15, 1000, 15):
        total = total - i

    print(total)


if __name__ == "__main__":
    main()
