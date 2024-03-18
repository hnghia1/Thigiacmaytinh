import cv2
import torch

# Đường dẫn đến mô hình đã train (best.pt)
model_path = 'C:/Users/HP/PycharmProjects/NhanDienHoaQua/best.pt'

# Load mô hình YOLOv5
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)

# Tên của các loại quả
classes = [
    "dua chuot", "tao", "kiwi", "chuoi", "cam",
    "dua`", "dao", "cherry", "le", "luu", "dua'",
    "dua hau", "dua vang", "nho", "dau tay"
]

# Danh sách màu sắc tương ứng với mỗi loại quả
colors = [
    (255, 255, 0),
    (255, 165, 0),
    (255, 192, 203),
    (255, 255, 0),
    (255, 0, 0),
    (0, 255, 0),
    (128, 0, 128),
    (255, 0, 0),
    (0, 128, 0),
    (139, 69, 19),
    (128, 0, 128),
    (255, 0, 0),
    (255, 0, 0),
    (255, 255, 0),
    (0, 255, 255)
]

# Kết nối đến camera (0: camera mặc định)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Chuyển đổi hình ảnh sang định dạng RGB và nhận dạng bằng mô hình YOLOv5
    results = model(frame)

    # Hiển thị kết quả trên hình ảnh
    for *boxes, conf, class_idx in results.xyxy[0].numpy():
        if conf > 0.5:  # Chỉ hiển thị kết quả với độ tin cậy > 0.5
            class_name = classes[int(class_idx)]
            if int(class_idx) < len(colors):  # Áp dụng màu chỉ cho số quả tương ứng với số màu có sẵn
                color = colors[int(class_idx)]  # Lấy màu sắc tương ứng
                cv2.rectangle(frame, (int(boxes[0]), int(boxes[1])), (int(boxes[2]), int(boxes[3])), color, 2)
                cv2.putText(frame, f'{class_name} {conf:.2f}', (int(boxes[0]), int(boxes[1] - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    # Hiển thị hình ảnh
    cv2.imshow('YOLOv5 Fruit Detection', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
