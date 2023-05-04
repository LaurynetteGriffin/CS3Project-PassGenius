from passwordss import password_strengthener
import sys

def main():
    password = input("Enter a password: ")
    result = password_strengthener(password)
    print(result)

if __name__ == '__main__':
    main()
