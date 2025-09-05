from parser_repr import calc


def main():
    while True:
        try:
            s = input("> ")
        except EOFError:
            break
        print(calc(s))


if __name__ == "__main__":
    main()
