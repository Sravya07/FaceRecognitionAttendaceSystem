# Real-Time Facial Recognition Attendance System

This project implements a **Real-Time Facial Recognition Attendance System** designed to automate student attendance tracking using a live webcam feed and a real-time database.

## Overview

The system captures video input, performs instant face recognition, and automatically updates attendance records in a Firebase database. It provides a robust solution for efficient and accurate attendance management, leveraging machine learning for identification and Firebase for data synchronization.

---

## Features

* **Real-Time Tracking:** Instantaneous update of attendance records upon successful face recognition.
* **Facial Recognition Pipeline:** Utilizes the `face_recognition` library to detect faces, generate encodings, and match known individuals.
* **Firebase Integration:** Seamless connection to Firebase Realtime Database for storing student information and attendance logs, and Firebase Storage for managing student images.
* **Time Constraint Logic:** Implements logic to prevent redundant attendance marks within a set period, ensuring data integrity.
* **Dynamic GUI:** A custom graphical interface displays real-time student information and attendance status upon detection.

---

## Technologies Used

* **Python:** Core programming language.
* **`face_recognition`:** For face detection and encoding.
* **Firebase:** Realtime Database and Storage.
* **Webcam Integration:** For live video capture.
* **GUI Framework:** (Specify framework if known, e.g., Tkinter, PyQt).

---

## Prerequisites

Ensure you have the following installed before proceeding:

* Python 3.x
* A configured **Firebase project** with access to Realtime Database and Storage. You will need your Firebase service account key.

## Installation and Setup

1.  **Clone the repository:**
    ```bash
    git clone [Insert GitHub URL]
    cd [repository-name]
    ```

2.  **Install dependencies:**
    ```bash
    pip install [List required Python libraries, e.g., face_recognition, firebase-admin, etc.]
    ```

3.  **Configure Firebase:**
    * Place your Firebase service account key file (e.g., `firebase-adminsdk.json`) in the project root.
    * Update any necessary configuration parameters in the project code (e.g., database URL, storage bucket).

4.  **Prepare Face Encodings:**
    * Ensure student data and corresponding images are uploaded to Firebase.
    * Run the encoding script (if available in the repo) to generate the `.pickle` file containing face encodings.

---

## Usage

1.  **Run the main application script:**
    ```bash
    python main.py  # (or the name of the main executable file)
    ```

2.  **System Operation:**
    * The GUI will launch and the webcam will activate.
    * The system will automatically recognize students in the camera feed.
    * Attendance records in the Firebase database will be updated instantly upon recognition.
