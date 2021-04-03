import cv2
import numpy as np
import mediapipe as mp
from pathlib import Path


class CheckPoints():
    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.picturePath = Path.cwd() / 'dataset' / 'NativeImg'
        self.file_list = self.picturePath.iterdir()
        self.annotation_folder = Path.cwd() / 'dataset' / 'Annotations'
        self.process_folder = Path.cwd() / 'dataset' / 'ProcessImg'

    def getCheckPoints(self):
        for _iter in self.file_list:
            fileName = _iter.name
            imgPath_list = _iter.iterdir()

            with self.mp_hands.Hands(
                static_image_mode=True,
                max_num_hands=2,
                min_detection_confidence=0.5) as hands:
                landmarks = []
                for idx, imgPath in enumerate(imgPath_list):
                    landmarks_list = []
                    # Read an image, flip it around y-axis for correct handedness output (see
                    # above).
                    image = cv2.flip(cv2.imread(str(imgPath)), 1)
                    # Convert the BGR image to RGB before processing.
                    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

                    # Print handedness and draw hand landmarks on the image.
                    # print('Handedness:', results.multi_handedness)
                    if not results.multi_hand_landmarks:
                        list_0 = [[0] * 3] * 21
                        landmarks.append(list_0)
                        continue
                    image_height, image_width, _ = image.shape
                    annotated_image = image.copy()

                    for i in range(21):
                        landmark_list = []
                        # print('hand_landmarks:', hand_landmarks)
                        # print('hand_landmarks:',hand_landmarks.landmark[0].x)
                        landmark_list.append(results.multi_hand_landmarks[0].landmark[i].x)
                        landmark_list.append(results.multi_hand_landmarks[0].landmark[i].y)
                        landmark_list.append(results.multi_hand_landmarks[0].landmark[i].z)
                        print(
                        f'Index finger tip coordinates: (',
                        f'{results.multi_hand_landmarks[0].landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width}, '
                        f'{results.multi_hand_landmarks[0].landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height})'
                        )
                        self.mp_drawing.draw_landmarks(
                            annotated_image, results.multi_hand_landmarks[0], self.mp_hands.HAND_CONNECTIONS)
                        landmarks_list.append(landmark_list)
                    landmarks.append(landmarks_list)
                    cv2.imwrite(
                        str(self.process_folder / fileName / Path(str(idx) + '.jpg')), cv2.flip(annotated_image, 1))
                landmarks_array = np.array(landmarks)
                landmarks_array = landmarks_array.reshape((-1, 3*21))
                np.savetxt(str(self.annotation_folder / fileName / Path(fileName + '.csv')), landmarks_array, delimiter=',')

