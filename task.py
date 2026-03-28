from tasks import load_tasks, save_tasks, add_task, view_tasks, delete_task

def main():
    tasks = load_tasks()
    
    while True:
        print("\n=== TO-DO LIST ===")
        print("1. Lihat tugas")
        print("2. Tambah tugas")
        print("3. Hapus tugas")
        print("4. Keluar")
        
        choice = input("Pilih menu: ")
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            task = input("Masukkan tugas baru: ")
            add_task(tasks, task)
            save_tasks(tasks)
        elif choice == "3":
            index = int(input("Masukkan nomor tugas yang ingin dihapus: "))
            delete_task(tasks, index)
            save_tasks(tasks)
        elif choice == "4":
            print("Keluar dari aplikasi...")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
