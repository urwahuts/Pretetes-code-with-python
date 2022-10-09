# Membuat kalkulator sederhana dengan Python

# fungsi ini menambah dua angka
def add(x, y):
    return x + y

# fungsi ini mengurangi dua angka
def subtract(x, y):
    return x - y

# fungsi ini mengkalikan dua angka
def multiply(x, y):
    return x * y

# fungsi ini membagi dua angka
def divide(x, y):
    return x / y


print("Pilih Operasi.")
print("1.Tambah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")

while True:
    # Mengambil input dari pengguna
    choice = input("Masukkan Pilihan(1/2/3/4): ")

    # cek jika pilihannya satu dari empat pilihan
    if choice in ('1', '2', '3', '4', ):
        num1 = float(input("Masukkan nomor pertama: "))
        num2 = float(input("Masukkan nomor kedua: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
	
	        
        # cek jika pengguna ingin melakukan penghitungan lain
        # menyudahi pengulangannya jika pengguna menjawab 'tidak'
        next_calculation = input("Lakukan pengitungan lain? (Ya/Tidak): ")
        if next_calculation == "Tidak":
          break
    
    else:
        print(" Perintah tidak dikenali")