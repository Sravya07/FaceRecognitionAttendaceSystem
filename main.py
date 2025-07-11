import pickle
import cv2
import os

import face_recognition
import numpy as np

capture = cv2.VideoCapture(1)
capture.set(3, 640)
capture.set(4, 480)

imgBackground = cv2.imread('Resources/background.png')

folderPath = 'Resources/Modes'
modePathList = os.listdir(folderPath)
imgModeList = []

for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderPath, path)))

# print(len(imgModeList))


#Load encoding file
print("Loading Encoding file.. ")
file = open('encodeFile.p', 'rb')
encodingsKnownWithIds = pickle.load(file)
file.close()
print("Encodings File loaded")

encodingsKnown, userIds = encodingsKnownWithIds
print(userIds)

while True:
    success, img = capture.read()

    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)



    imgBackground[162:162+480, 55:55+640] = img #Overlay webcam feed onthe background image
    imgBackground[44:44+633, 808:808+414] = imgModeList[0]

    for encodedFace, faceLocation in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodingsKnown, encodedFace)
        faceDistance = face_recognition.face_distance(encodingsKnown, encodedFace)

        # print("matches", matches)
        # print("Face Distance", faceDistance)

        matchIdx = np.argmin(faceDistance)
        # print("Match Index", matchIdx)

        if matches[matchIdx]:
            # print("Known Face Detected - userId", userIds[matchIdx])
            y1, x2, y2, x1 = faceLocation
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

            bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1 # Bounding Box

            x, y, w , h = bbox
            start_point = (x, y)
            end_point = (x + w, y + h)
            bbox_color = (0, 0, 255)
            bbox_thickness = 2

            imgBackground = cv2.rectangle(imgBackground, start_point, end_point, bbox_color, bbox_thickness)



    # cv2.imshow("Webcam", img)
    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)
