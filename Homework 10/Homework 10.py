import cv2
import os

video_path = "video.mp4"
output_dir = "tracking_results"
os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    raise Exception("Can't open video")

# Read first frame
ret, frame = cap.read()
if not ret:
    raise Exception("Can't read the first frame")

bbox = cv2.selectROI("Select zone for tracking", frame, fromCenter=False, showCrosshair=True)
cv2.destroyAllWindows()

# Создаем два трекера: CSRT и KCF
tracker_csrt = cv2.TrackerCSRT_create()
tracker_kcf = cv2.TrackerKCF_create()
tracker = cv2.TrackerMIL_create()

# Инициализируем их одинаковым ROI
tracker_csrt.init(frame, bbox)
tracker_kcf.init(frame, bbox)
tracker.init(frame, bbox)

# Флаг для сохранения кадра
saved = False
frameIndex = 0

def trackImage(tracker, name, color):
    success, bbox = tracker.update(frame)
    if success:
        x, y, w, h = [int(v) for v in bbox]
        cv2.rectangle(result_frame, (x, y), (x + w, y + h), color, 2)
        cv2.putText(result_frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, color, 2)

while True:
    ok, frame = cap.read()
    if not ok:
        break

    # Копия кадра для рисования
    result_frame = frame.copy()


    trackImage(tracker_csrt, "CSRT", (0,255,0))   
    trackImage(tracker_kcf, "KCF", (255,0,0)) 
    trackImage(tracker, "MIL", (0,0,255)) 

    cv2.imshow("Compairing", result_frame)

    if(frameIndex % 15 == 0):
        out_path = os.path.join(output_dir, f"frame_{frameIndex:02d}.jpg")
        cv2.imwrite(out_path, result_frame)
    
    frameIndex+=1

    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
