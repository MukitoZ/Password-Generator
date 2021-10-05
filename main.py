#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for char in range(1, nr_letters + 1):
  password += random.choice(letters)
for char in range(1, nr_numbers + 1):
  password += random.choice(numbers)
for char in range(1, nr_symbols + 1):
  password += random.choice(symbols)

print(f"Your EZ password is: {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

passwords = []
for char in range(1, nr_letters + 1):
  passwords += random.choice(letters)
for char in range(1, nr_numbers + 1):
  passwords += random.choice(numbers)
for char in range(1, nr_symbols + 1):
  passwords += random.choice(symbols)
random.shuffle(passwords)
pwd = ""
for pw in passwords:
  pwd += pw

print(f"Your MID password is: {pwd}")

# untuk ambil letters random sesuai yang diinput
random_letters = random.sample(letters, nr_letters)
# untuk ambil numbers random sesuai yang diinput
random_numbers = random.sample(numbers, nr_numbers)
# untuk ambil symbols random sesuai yang diinput
random_symbols = random.sample(symbols, nr_symbols)

#nyatuin semua variable jadi satu
random_password = random_letters + random_numbers + random_symbols
#disini password diacak lagi biar ga berurutan sesuai dengan jumlah karakter dari password
real_random_password = random.sample(random_password, len(random_password))

#string sebagai akumulator dari perulangan
yes = ""
#perulangan untuk ngubah semua list jadi string
for x in real_random_password:
  yes += x

print(f"Your HARD password is: {yes}")