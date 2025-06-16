import prompt

# import sys
# print(sys.executable)


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")


if __name__ == '__main__':
    main()
