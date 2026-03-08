import cv2
import mediapipe as mp
import time
import math

from volume_control import handle_volume_control

hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
cap.set(3, 1280)
cap.set(4, 720)

def main():
    with hands.Hands(max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.7) as hand:

        while True:
            attempt = 0
            success, img = cap.read()

            while not success and attempt < 5:
                time.sleep(0.2)
                success, img = cap.read()
                attempt += 1

            if not success:
                print("Failed to read frame")
                break
        
            img = cv2.flip(img, 1)
            height, width, _ = img.shape
            rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            results = hand.process(rgb)

            if results.multi_hand_landmarks:
                for hand_landmark in results.multi_hand_landmarks:
                    mp_draw.draw_landmarks(img, hand_landmark, hands.HAND_CONNECTIONS, mp_draw.DrawingSpec(color=(0, 255, 0), thickness=5, circle_radius=4))

                    fingerTips = {
                        "thumb": hand_landmark.landmark[4],
                        "index": hand_landmark.landmark[8],
                        "middle": hand_landmark.landmark[12],
                        "ring": hand_landmark.landmark[16],
                        "pinky": hand_landmark.landmark[20]
                    }

                    # for vol control
                    # volume = handle_volume_control(hand_landmark)
                    # cv2.putText(img, f"Volume: {int(volume)}%", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                    for name, landmark in fingerTips.items():
                        x = int(landmark.x * width)
                        y = int(landmark.y * height)
                        cv2.putText(img, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1) # label finger tip
                        cv2.circle(img, (x, y), 5, (255, 0, 0), cv2.FILLED) # filled finger tip 

                volume = handle_volume_control(hand_landmark)
                cv2.putText(img, f"Volume: {int(volume)}%", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            cv2.imshow("Image", img)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
