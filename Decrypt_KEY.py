import tkinter as tk
from tkinter import filedialog
from cryptography.fernet import Fernet


# โหลดกุญแจจากไฟล์
def load_key():
    with open("encryption_key.key", "rb") as key_file:
        return key_file.read()


# ถอดรหัสไฟล์
def decrypt_file(file_path, key):
    fernet = Fernet(key)

    # อ่านข้อมูลจากไฟล์ที่เข้ารหัส
    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    # ถอดรหัสข้อมูล
    decrypted_data = fernet.decrypt(encrypted_data)

    # สร้างไฟล์ใหม่สำหรับข้อมูลที่ถอดรหัส
    decrypted_file_path = file_path.replace(".encrypted", ".decrypted")
    with open(decrypted_file_path, "wb") as file:
        file.write(decrypted_data)

    # แสดงผลลัพธ์
    result_label.config(text=f"ไฟล์ {file_path} ถูกถอดรหัสแล้ว\nบันทึกเป็น {decrypted_file_path}")


# เปิดไฟล์ที่เลือก
def open_file():
    # เปิดหน้าต่างเลือกไฟล์
    file_path = filedialog.askopenfilename(filetypes=[("Encrypted Files", "*.encrypted")])

    if file_path:
        key = load_key()  # โหลดกุญแจจากไฟล์
        decrypt_file(file_path, key)


# สร้างหน้าต่าง GUI
root = tk.Tk()
root.title("โปรแกรมถอดรหัสไฟล์")

# สร้างปุ่มเลือกไฟล์
select_button = tk.Button(root, text="เลือกไฟล์ที่ต้องการถอดรหัส", command=open_file)
select_button.pack(pady=20)

# สร้าง label แสดงผลลัพธ์
result_label = tk.Label(root, text="", wraplength=400)
result_label.pack(pady=10)

# เริ่มต้นหน้าต่าง
root.mainloop()
