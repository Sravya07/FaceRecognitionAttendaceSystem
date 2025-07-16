import pickle
import cv2
import os

import face_recognition
import numpy as np

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognitionattendacesystem-default-rtdb.firebaseio.com/",
    'storageBucket' : "facerecognitionattendacesystem.firebasestorage.app"
})

bucket = storage.bucket()

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
# print(userIds)

modeType = 3
counter = 0
id = -1
imgUser = []

while True:
    success, img = capture.read()

    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)



    imgBackground[162:162+480, 55:55+640] = img #Overlay webcam feed onthe background image
    imgBackground[44:44+633, 808:808+414] = imgModeList[modeType]

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

            id = userIds[matchIdx]

            if counter == 0:
                counter = 1
                modeType = 1
        
    if counter != 0:

        if counter == 1:

            #Get data
            userInfo = db.reference(f'Users/{id}').get()
            print(userInfo)

            #Get image from storage
            blob = bucket.get_blob(f'Images/{id}.png')
            array = np.frombuffer(blob.download_as_string(), np.uint8)
            imgUser = cv2.imdecode(array, cv2.COLOR_BGRA2BGR)




        cv2.putText(imgBackground, str(userInfo['total_attendance']), (861,125),
                     cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
        
        (w, h), _ = cv2.getTextSize(userInfo['name'], cv2.FONT_HERSHEY_COMPLEX, 1, 1)
        offset = (414 - w)//2
        cv2.putText(imgBackground, str(userInfo['name']), (808+offset,445),
                     cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 50), 1)
        
        cv2.putText(imgBackground, str(userInfo['dept']), (1006,550),
                     cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
        cv2.putText(imgBackground, str(id), (1006,493),
                     cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
        cv2.putText(imgBackground, str(userInfo['level']), (910,625),
                     cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
        cv2.putText(imgBackground, str(userInfo['start_date']), (1125,625),
                     cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
        
        imgBackground[175:175+216,909:909+216] = cv2.resize(imgUser,(216,216))

        counter += 1

    # Show webcam feed
    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)
