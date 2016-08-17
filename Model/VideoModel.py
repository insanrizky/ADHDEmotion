import cv2
class VideoModel():
    def readVideo(self, filename):
        cap = cv2.VideoCapture(filename)

        while cap.isOpened():
            print cap.isOpened()
            ret, frame = cap.read()


            if frame is not None:
                # convert to gray scale
                gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                #detect face
                face_cascade = cv2.CascadeClassifier("data/xml/haarcascade_frontalface_default.xml")
                #detect eye
                eye_cascade = cv2.CascadeClassifier("data/xml/haarcascade_eye.xml")

                #detect faces
                faces = face_cascade.detectMultiScale(gray_img, 1.3, 5)

                for(x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                    roi_gray = gray_img[y:y+(h/2), x:x+w]
                    roi_color = frame[y:y+(h/2), x:x+w]
                    #detect eyes
                    eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
                    for (xe, ye, we, he) in eyes:
                        cv2.rectangle(roi_color, (xe, ye), (xe+we, ye+he), (0, 255, 0), 2)


            else:
                break

            cv2.imshow("Video", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


