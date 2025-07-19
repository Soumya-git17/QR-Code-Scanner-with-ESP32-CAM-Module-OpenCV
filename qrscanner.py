import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import requests


url = "your url from esp"


prev = ""
pres = ""

while True:
    img_resp = requests.get(url)
    imgnp = np.array(bytearray(img_resp.content), dtype = np.uint8)
    frame = cv2.imdecode(imgnp, -1)

    if frame is None:
            print("Failed to decode image from ESP32-CAM")
            continue
    
    decodedObjects = pyzbar.decode(frame)

    for obj in decodedObjects:
        pres = obj.data
        if prev == pres:
            pass
        else:
            print("Type:", obj.type)
            print("Data", obj.data)
            prev = pres
        
        cv2.putText(frame, str(obj.data), (50,50), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3)

    cv2.imshow("live transmission", frame)
    
    key = cv2.waitKey(1)
    if key == 27:   # Esc key
        break

cv2.destroyAllWindows()