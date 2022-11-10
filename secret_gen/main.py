import argparse
import random
import string


def main():
    parser = argparse.ArgumentParser(description="Generate a random secret")
    parser.add_argument(
        "length", type=int, help="How many characters should the secret be?"
    )
    args = parser.parse_args()

    chars = string.ascii_letters
    nums = string.digits
    specs = "!#$%&()*+,-.:;<=>?@[]_"
    secret = []
    for i in range(1, args.length):
        secret.append(chars[random.randint(0, len(chars) - 1)])

    print(secret)


if __name__ == "__main__":
    main()
