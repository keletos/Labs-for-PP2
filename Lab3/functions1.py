grams = float(input())

def converter(grams):
    ounces = grams * 28.3495231
    return ounces

print(converter(grams))


F = int(input())

def C_to_F(F):
    C = (5 / 9) * (F - 32)
    return C

print(C_to_F(F))


numheads = 35
numlegs = 94
def solve(numheads, numlegs):
    rabbits = int(((numlegs - (2 * numheads)) / 2))
    print("Number of rabbits: ")
    print(rabbits)
    chikens = int(numheads - rabbits)
    print("Number of chikens: ")
    print(chikens)
    return 0

solve(numheads, numlegs)


def filter_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    return [num for num in numbers if is_prime(num)]

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = filter_prime(numbers_list)
print(prime_numbers)


def print_permutations(input_str, current_permutation=""):
    if len(input_str) == 0:
        print(current_permutation)
    else:
        for i in range(len(input_str)):
            remaining_chars = input_str[:i] + input_str[i+1:]
            print_permutations(remaining_chars, current_permutation + input_str[i])


def reverse_sentence(input_str):
    return ' '.join(input_str.split()[::-1])

user_input = input("Enter a sentence: ")
reversed_sentence = reverse_sentence(user_input)
print("Reversed sentence:", reversed_sentence)


nums = [1, 2, 3, 3]

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            print("True")
    

has_33(nums)


nums = [1,2,4,0,0,7,5]

def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7:
            print("True")

spy_game(nums)


def volume(R):
    vol = 4 * 3.14 * R ** 3 / 3
    return vol 

print(volume(float(input())))


def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

input_list = [1, 2, 3, 4, 2, 3, 5, 6, 4]
print(unique_elements(input_list))


def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]

user_input = input("Enter:")
if is_palindrome(user_input):
    print("Palindrome.")
else:
    print("Not a palindrome.")


def pseudo_random(seed):
    a = 1664525
    c = 1013904223
    m = 2**32
    return (a * seed + c) % m


def histogram(numbers):
    for num in numbers:
        print('*' * num)

histogram([3, 2, 1])


def guess_the_number():
    seed = 123456789

    secret_number = (pseudo_random(seed) % 20) + 1

    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    guesses_taken = 0

    while True:
        print("Take a guess.")
        guess = int(input())

        guesses_taken += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break

guess_the_number()


from my_functions import reverse_sentence, is_palindrome

def main():
    user_input = input("Enter: ")
    reversed_sentence = reverse_sentence(user_input)
    print("Reversed:", reversed_sentence)

    user_input = input("Enter: ")
    if is_palindrome(user_input):
        print("Palindrome.")
    else:
        print("Not a palindrome.")

if __name__ == "__main__":
    main()

