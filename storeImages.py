import os
import cv2
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'storageBucket' : "facerecognitionattendacesystem.firebasestorage.app"
})

folderPath = 'Images'
pathList = os.listdir(folderPath)
imgList = []

print("Uploading Images to Storage..")
for path in pathList:
    
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    fileName = os.path.join(folderPath, path)
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

print("User Images uploaded successfully")