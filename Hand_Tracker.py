import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
tip_ids = [4, 8, 12, 16, 20]  # 4 , 8 , 12 , 16 , 20 for all the finger tips

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    lmList = []

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
                if id == 8:
                    cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)

                if len(lmList) == 21:
                    fingers = []
                    if lmList[tip_ids[0]][1] < lmList[tip_ids[0] - 2][1]:
                        fingers.append(1)

                    else:
                        fingers.append(0)

                    for tip in range(1, 5):
                        if lmList[tip_ids[tip]] [2] < lmList[tip_ids[tip] - 2] [2]:
                            fingers.append(1)

                        else:
                            fingers.append(0)

                    print(fingers.count(1))
                    cv2.putText(img, str(fingers.count(1)), (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

    cv2.imshow("Hand Tracker", img)
    if cv2.waitKey(5) & 0xFF == 27:
        break