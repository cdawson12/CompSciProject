import requests
import cv2
import os
filePath_1 = "satSim1.png"
filePath_2 = "satSim2.png"

def check_file_size(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
    size = os.path.getsize(file_path)
    if size > 1000000:
        print("This file is too big")
    else:
        print(f"File size of {file_path} is {size} bytes")


check_file_size(filePath_1)

img = cv2.imread(filePath_1)


_, img_encoded = cv2.imencode('.jpg', img)

# Send image to OCRSpace API
url = "https://api.ocr.space/parse/image"
payload = {"apikey": "K84392402688957", "isOverlayRequired": "True"}
files = {"image": (filePath_1, img_encoded.tobytes(), "image/jpeg")}
response = requests.post(url, data=payload, files=files)


if response.status_code != 200:
    print("Error occurred while getting response from API: ",response.status_code)

response_text = response.json()["ParsedResults"][0]["ParsedText"]

if filePath_2 != "":
    img_2 = cv2.imread(filePath_2)
    _, img_encoded_2 = cv2.imencode('.jpg', img_2)
    files_2 = {"image": (filePath_1, img_encoded_2.tobytes(), "image/jpeg")}
    response_2 = requests.post(url, data=payload, files=files_2)
    response_text = response_text + response_2.json()["ParsedResults"][0]["ParsedText"]

print(response_text)

if 'ErrorMessage' in response_text:
    print(f" The error is {response_text['ErrorMessage']}")
