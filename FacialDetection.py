import cv2


xml_haar_cascade = 'haarcascade_frontalface_alt23.xml'

# Carregando classificador
faceClassifier = cv2.CascadeClassifier(xml_haar_cascade)

camera = cv2.VideoCapture(0)

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while not cv2.waitKey(1) & 0xFF == ord("q"):
    ret, frame_colorido = camera.read()

    frame_cinza = cv2.cvtColor(frame_colorido, cv2.COLOR_BGR2GRAY)

    faces =  faceClassifier.detectMultiScale(frame_cinza)

    for x, y, w, h in faces:
        cv2.rectangle(frame_colorido, (x, y), (x+w, y +h), (0,0,255), 3)

    cv2.imshow('Facial detection - PS IMAGEM', frame_colorido)
    #cv2.imshow('gray', frame_cinza)