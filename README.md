# QR Code Scanner with ESP32-CAM & OpenCV

This project demonstrates a wireless QR code scanner built using the ESP32-CAM module and OpenCV. The ESP32-CAM streams live video over Wi-Fi, and a Python script processes the stream to detect and decode QR codes in real time.

## 🚀 Features

- 📷 Real-time video streaming from ESP32-CAM
- 🔍 QR code detection and decoding using OpenCV and pyzbar
- 📡 Wireless and lightweight solution
- 🐍 Easy-to-use Python script for scanning

## 🛠️ Hardware Required

- ESP32-CAM module
- ESP32-CAM MB board
- USB Connector
- Wi-Fi network

## 💻 Software Required

- Arduino IDE (to program ESP32-CAM)
- Python
- OpenCV
- Numpy
- Pyzbar

## 🔧 Setup Instructions

### 1. Flash ESP32-CAM

- Install the ESP32 board manager in Arduino IDE
- Use the `ESP32-CAM` sketch provided in the `esp32-cam-code/` folder
- Set your Wi-Fi credentials in the sketch
- Upload the code

### 2. Stream Video

- After flashing, reset the ESP32-CAM
- Open the Serial Monitor to find the stream URL
- Test the stream in a browser

### 3. Run Python QR Scanner

- Run the `qrscanner.py` script in the `python-opencv/` folder
- It will access the video stream and scan for QR codes in real time
