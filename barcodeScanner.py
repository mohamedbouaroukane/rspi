import cv2
import zxing
from playsound import playsound
from PyQt5.QtMultimedia import QSound
from config import assetsURL
from signature.signature import decrypt_and_verify

# Initialize ZXing barcode reader
reader = zxing.BarCodeReader()

# Set to store already read codes
detected_codes = set()

def read_codes(frame, http_requester):
    global detected_codes
    click_sound = QSound(assetsURL+"/clickSound.wav")
    temp_file = 'temp_frame.png'
    cv2.imwrite(temp_file, frame)
    barcode = reader.decode(temp_file)

    if barcode is not None:
        code_data = barcode.parsed
        if code_data in detected_codes:
            return frame  

        detected_codes.add(code_data)

        x, y, w, h = 0, 0, frame.shape[1], frame.shape[0]  
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        code_type = barcode.format
        text = f'{code_type}: {code_data}'
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        playsound(assetsURL+"/clickSound.wav", block=True)
        print(f'Code: {code_data}, Type: {code_type}')
        data,valid = decrypt_and_verify(code_data)
        print(valid)
        if(valid):
            http_requester.send_request(data)

    return frame

def qr_scanner(http_requester):
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Could not open video device.")
        return

    while True:
        ret, frame = camera.read()
        if not ret:
            break

        frame = read_codes(frame, http_requester)
        cv2.imshow('Barcode/QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()