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

        # Tạo Frame chứa nút tải video và nút nhận diện
        self.button_frame = tk.Frame(root, bg="#f0f0f0")
        self.button_frame.pack(side=tk.TOP, fill=tk.X)

        self.upload_button = tk.Button(self.button_frame, text="Tải video lên", font=("Arial", 14, "bold"), command=self.upload_video, bg="#4CAF50", fg="white")
        self.upload_button.pack(side=tk.LEFT, padx=20, pady=20, expand=True)

        self.process_button = tk.Button(self.button_frame, text="Phát hiện và nhận diện", font=("Arial", 14, "bold"), command=self.detect_objects, bg="#4CAF50", fg="white")
        self.process_button.pack(side=tk.LEFT, padx=20, pady=20, expand=True)

        self.result_label = tk.Label(root, text="", font=("Arial", 14, "italic"), bg="#f0f0f0")
        self.result_label.pack()

        self.original_label = tk.Label(root, bg="#f0f0f0")
        self.original_label.pack(side=tk.LEFT, padx=20, pady=20)
        self.result_label = tk.Label(root, bg="#f0f0f0")
        self.result_label.pack(side=tk.LEFT, padx=20, pady=20)

    def upload_video(self):
        self.video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi *.mkv")])
        if self.video_path:
            messagebox.showinfo("Thông báo", f"Đã chọn video: {self.video_path}")

    def detect_objects(self):
        if self.video_path:
            # Thực hiện nhận diện bằng subprocess
            command = f"python yolov5/detect.py --source {self.video_path} --img 640 --conf 0.25 --weights best.pt"
            subprocess.run(command, shell=True)

            folder_path = "C:/Users/HP/PycharmProjects/NhanDienHoaQua/result"
            items = os.listdir(folder_path)
            folder_count = 0
            for item in items:
                item_path = os.path.join(folder_path, item)
                if os.path.isdir(item_path):
                    folder_count += 1

            base_name = os.path.splitext(os.path.basename(self.video_path))[0]

            # Hiển thị video kết quả
            result_video_path = f"result/detect{folder_count}/{base_name}.mp4"

            # Tạo widget video từ thư viện PIL
            self.result_video = ImageTk.PhotoImage(file=result_video_path)
            self.result_label.config(image=self.result_video)
            self.result_label.image = self.result_video

            self.result_label.config(text="Kết quả nhận diện đã được hiển thị ở trên.", fg="#4CAF50")
        else:
            messagebox.showerror("Lỗi", "Vui lòng tải video lên trước khi thực hiện nhận diện.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ObjectDetectionApp(root)
    root.mainloop()
