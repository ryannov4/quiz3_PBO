# fungsi penjumlahane1
def add(x,y):
    return x + y
# fungsi pengurangan
def add(x,y):
    return x - y
# fungsi perkalian
def add(x,y):
    return x * y
# fungsi pembagian
def add(x,y):
    return x / y
# menu operasi
print("pilih operasi.")
print("1.penjumlahan.")
print("2.pengurangan.")
print("3.perkalian.")
print("4.pembagian.")
# meminta input dari user
choice = input("Masukan Pilihan")
num1 = int(input("Masukan Bilangan Pertama:"))
num2 = int(input("Masukan Bilangan Kedua:"))
if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))
else:
    print("input salah")