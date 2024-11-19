import tkinter as tk
from tkinter import filedialog
from cryptography.fernet import Fernet


# โหลดกุญแจจากไฟล์
def load_key():
    with open("encryption_key.key", "rb") as key_file:
        return key_file.read()


# เข้ารหัสไฟล์
def encrypt_file(file_path, key):
    fernet = Fernet(key)

    # อ่านข้อมูลจากไฟล์
    with open(file_path, "rb") as file:
        file_data = file.read()

    # เข้ารหัสข้อมูล
    encrypted_data = fernet.encrypt(file_data)

    # สร้างไฟล์ใหม่สำหรับข้อมูลที่เข้ารหัส
    encrypted_file_path = file_path + ".encrypted"
    with open(encrypted_file_path, "wb") as file:
        file.write(encrypted_data)

    # แสดงผลลัพธ์
    result_label.config(text=f"ไฟล์ {file_path} ได้รับการเข้ารหัสแล้ว\nบันทึกเป็น {encrypted_file_path}")


# เปิดไฟล์ที่เลือก
def open_file():
    # เปิดหน้าต่างเลือกไฟล์
    file_path = filedialog.askopenfilename()

    if file_path:
        key = load_key()  # โหลดกุญแจจากไฟล์
        encrypt_file(file_path, key)


# สร้างหน้าต่าง GUI
root = tk.Tk()
root.title("โปรแกรมเข้ารหัสไฟล์")

# สร้างปุ่มเลือกไฟล์
select_button = tk.Button(root, text="เลือกไฟล์ที่ต้องการเข้ารหัส", command=open_file)
select_button.pack(pady=20)

# สร้าง label แสดงผลลัพธ์
result_label = tk.Label(root, text="", wraplength=400)
result_label.pack(pady=10)

# เริ่มต้นหน้าต่าง
root.mainloop()
