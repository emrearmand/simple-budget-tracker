print("Budget Tracker is running!")
transactions = [] 

def add_transaction(amount, type):
    transactions.append({"amount": amount, "type": type})

def get_balance():
    income = sum(t["amount"] for t in transactions if t["type"] == "income")
    outcome = sum(t["amount"] for t in transactions if t["type"] == "outcome")
    return income - outcome

while True:
    print("\nBudget Tracker")
    print("1. Tambah Pemasukan")
    print("2. Tambah Pengeluaran")
    print("3. Lihat Saldo")
    print("4. Keluar")

    choice = input("Pilih menu: ")

    if choice == "1":
        amount = float(input("Masukkan jumlah pemasukan: "))
        add_transaction(amount, "income")
    elif choice == "2":
        amount = float(input("Masukkan jumlah pengeluaran: "))
        add_transaction(amount, "outcome")
    elif choice == "3":
        print(f"Total saldo saat ini: {get_balance()}")
    elif choice == "4":
        print("Keluar dari Budget Tracker.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
