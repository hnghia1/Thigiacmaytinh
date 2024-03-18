import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import subprocess
import os

class ObjectDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Object Detection App")
        self.root.geometry("1280x720")
        self.root.config(bg="#f0f0f0")

        # Tạo Frame chứa nút tải ảnh và nút nhận diện
        self.button_frame = tk.Frame(root, bg="#f0f0f0")
        self.button_frame.pack(side=tk.TOP, fill=tk.X)

        self.upload_button = tk.Button(self.button_frame, text="Tải ảnh lên", font=("Arial", 14, "bold"),
                                       command=self.upload_image, bg="#4CAF50", fg="white")
        self.upload_button.pack(side=tk.LEFT, padx=20, pady=20, expand=True)

        self.process_button = tk.Button(self.button_frame, text="Phát hiện và nhận diện", font=("Arial", 14, "bold"),
                                        command=self.detect_objects, bg="#4CAF50", fg="white")
        self.process_button.pack(side=tk.LEFT, padx=20, pady=20, expand=True)

        self.result_label = tk.Label(root, text="", font=("Arial", 14, "italic"), bg="#f0f0f0")
        self.result_label.pack()

        self.original_image = None
        self.result_image = None
        self.original_label = tk.Label(root, bg="#f0f0f0")
        self.original_label.pack(side=tk.LEFT, padx=20, pady=20)
        self.result_label = tk.Label(root, bg="#f0f0f0")
        self.result_label.pack(side=tk.LEFT, padx=20, pady=20)

    def upload_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
        if self.image_path:
            # Hiển thị ảnh gốc
            original_image = Image.open(self.image_path)
            original_image = original_image.resize((600, 450))
            self.original_image = ImageTk.PhotoImage(original_image)
            self.original_label.config(image=self.original_image)
            self.original_label.image = self.original_image

    def detect_objects(self):
        if self.image_path:
            # Thực hiện nhận diện bằng subprocess
            command = f"python yolov5/detect.py --source {self.image_path} --img 640 --conf 0.25 --weights best.pt"
            subprocess.run(command, shell=True)

            folder_path = "C:/Users/HP/PycharmProjects/NhanDienHoaQua/result"
            items = os.listdir(folder_path)
            folder_count = 0
            for item in items:
                item_path = os.path.join(folder_path, item)
                if os.path.isdir(item_path):
                    folder_count += 1

            base_name = os.path.splitext(os.path.basename(self.image_path))[0]

            # Hiển thị ảnh kết quả
            result_image_path = f"result/detect{folder_count}/{base_name}.jpg"
            result_image = Image.open(result_image_path)
            result_image = result_image.resize((600, 450))
            self.result_image = ImageTk.PhotoImage(result_image)
            self.result_label.config(image=self.result_image)
            self.result_label.image = self.result_image

            self.result_label.config(text="Kết quả nhận diện đã được hiển thị ở trên.", fg="#4CAF50")
        else:
            messagebox.showerror("Lỗi", "Vui lòng tải ảnh lên trước khi thực hiện nhận diện.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ObjectDetectionApp(root)
    root.mainloop()
