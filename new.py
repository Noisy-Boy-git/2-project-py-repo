import random
import string
letters=string.ascii_letters
number = ['1','2','3','4','5','6','7','8','9']
punctuation=string.punctuation
print("\n\n***** welcom to password generator *****\n\n")
total=int(input("enter the number of character in th password:"))
total_letters=int(input("enter the number of letters in the password:"))
total_numbers=int(input("enter the number of numbers in the password:"))
total_symbols=int(input("enter the number of symbols in the password:"))
if total_letters+total_numbers+total_symbols==total:
    password=(
        random.choices(number, k=total_numbers)+
        random.choices(letters, k=total_letters)+
        random.choices(punctuation, k=total_symbols)
    )
    random.shuffle(password)
    passkey=''.join(password)
    print(f"{passkey}")
else:
    print("invalid input. the sum of letters or numbers or symbols doesn't match the password")