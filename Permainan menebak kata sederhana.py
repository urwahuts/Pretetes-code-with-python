import random
# library yang kami gunakan untuk memilih
# pada kata kata yang acak dari daftar yang telah disediakan

name = input("Siapa nama anda? ")
# disini pengguna diminta untuk memasukkan nama pengguna

print("Selamat Bermain ! ", name)

words = ['septi', 'bayu', 'budi', 'anto',
		'tono', 'dika', 'danu', 'elga', 'safi']

# Function akan memilih 1 kata
# dari list kata diatas

word = random.choice(words)


print("Tebak Karakter")

guesses = ''

# angka berapapun dapat ditentukan disini
turns = 3


while turns > 0:

	# menghitung berapa kali pengguna gagal
	failed = 0

	# semua karakter dalam kata
	# diambil satu persatu.
	for char in word:

		# membandingkan karakter itu 
		# dengan karakter yang ditebak
		if char in guesses:
			print(char, end=" ")

		else:
			print("_")
			print(char, end=" ")

			# setiap kesalahan 1 akan
			# ditambahkan di failed
			failed += 1

	if failed == 0:
		# pengguna akan memenangkan permainan jika failure = 0
		# dan 'selamat...' akan diberikan
		print("selamat….")
		
		# ini mencetak kata yang benar
		print("Karakternya Adalah: ", word)
		break

	# jika pengguna telah memasukkan alfabet yang salah maka
	# itu akan meminta pengguna untuk memasukkan alfabet lain
	print()
	guess = input("Tebak Karakter:")

	# setiap karakter input akan disimpan dalam 'guesses'
	guesses += guess

	if guess not in word:
		turns -= 1
		print("Coba Lagi")
		print("Kamu Memiliki", + turns, 'Kesempatan')

		if turns == 0:
			print("Anda Kalah")