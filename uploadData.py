import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognitionattendacesystem-default-rtdb.firebaseio.com/"
})

ref = db.reference('Users')

data = {
    "325788" : {
        "name" : "Adam Sandler",
        "dept" : "Robotics",
        "start_date" : "2017-11-02",
        "total_attendance" : 6,
        "level" : 3,
        "title" : "Junior Engineer",
        "last_attendance_time" : "2021-12-11 00:54:34"
    },
    "547678" : {
        "name" : "Tom Cruise",
        "dept" : "Mechanics",
        "start_date" : "2015-1-22",
        "total_attendance" : 9,
        "level" : 3,
        "title" : "Aircraft mechanic",
        "last_attendance_time" : "2023-02-18 01:45:36"
    },
    "678903" : {
        "name" : "Sravya Somi",
        "dept" : "Tech",
        "start_date" : "2020-11-14",
        "total_attendance" : 13,
        "level" : 4,
        "title" : "Software Dev Engineer",
        "last_attendance_time" : "2024-03-11 10:16:56"
    },
    "890373" : {
        "name" : "Harish S",
        "dept" : "Marketing",
        "start_date" : "2018-09-20",
        "total_attendance" : 8,
        "level" : 5,
        "title" : "Marketing Manager",
        "last_attendance_time" : "2024-06-18 07:28:23"
    },
    "965412" : {
        "name" : "Emilia Clarke",
        "dept" : "Product",
        "start_date" : "2016-08-12",
        "total_attendance" : 9,
        "level" : 5,
        "title" : "Technical Product Manager",
        "last_attendance_time" : "2025-04-11 06:39:23"
    }
}

print("Uploading user data to db..")
for key, value in data.items():
    ref.child(key).set(value)

print("Data uploaded successfully")