import random

def toss_coin():
    return random.choice(['Heads', 'Tails'])

def main():
    print("Coin Toss Simulator")
    result = toss_coin()
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()
