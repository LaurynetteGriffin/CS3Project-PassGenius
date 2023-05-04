from passwordss import password_strength
import sys

def main():
    password = input("Enter a password: ")
    result = password_strength(password)
    print(result)

if __name__ == '__main__':
    main()
