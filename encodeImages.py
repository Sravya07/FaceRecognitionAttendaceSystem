import cv2
import face_recognition
import os
import pickle

# importing user images
folderPath = "Images"
pathList = os.listdir(folderPath)
# print(pathList)
imgList = []
userIds = []

for path in pathList:
    # imgList.append(cv2.resize(cv2.imread(os.path.join(folderPath, path)), (216, 216)))
    imgList.append(cv2.imread(os.path.join(folderPath, path)))

    userIds.append(os.path.splitext(path)[0])
    # print(os.path.splitext(path)[0])

print(userIds)


def findEncodings(imagesList):
    encodings = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodings.append(encode)

    return encodings


print("Encoding images.. ")
encodingsKnown = findEncodings(imgList)
encodingsKnownWithIds = [encodingsKnown, userIds]
print("Encoding complete")

# cv2.imencode('Images/')

print("Saving encoded images in a pickle file..")
file = open("encodeFile.p", "wb")
pickle.dump(encodingsKnownWithIds, file)
file.close()
print("Encodings saved")
