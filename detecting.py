import cv2
import dlib

model_detector1 = dlib.simple_object_detector("Detector1.svm") # путь к детектору
model_detector2 = dlib.simple_object_detector("Detector2.svm")
model_detector3 = dlib.simple_object_detector("Detector3.svm")
cam = cv2.VideoCapture(0)

key = 1
ESCAPE = 27
while key != ESCAPE:
    ret, frame = cam.read()
    frame_viz = frame.copy()
    #frame_viz = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    boxes1 = model_detector1(frame)
    boxes2 = model_detector2(frame)
    boxes3 = model_detector3(frame)
    #if not boxes1:
        #print("no")
    for box in boxes1:
        print(box, 1)
        (x, y, xb, yb) = [box.left(), box.top(), box.right(), box.bottom()]
        cv2.rectangle(frame_viz, (x, y), (xb, yb), (0, 0, 255), 2)

    for box in boxes2:
        print(box, 2)
        (x, y, xb, yb) = [box.left(), box.top(), box.right(), box.bottom()]
        cv2.rectangle(frame_viz, (x, y), (xb, yb), (0, 0, 255), 2)

    for box in boxes3:
        print(box, 3)
        (x, y, xb, yb) = [box.left(), box.top(), box.right(), box.bottom()]
        cv2.rectangle(frame_viz, (x, y), (xb, yb), (0, 0, 255), 2)
    cv2.imshow("Frame", frame_viz)
    key = cv2.waitKey(10)
cv2.destroyAllWindows()
cam.release()