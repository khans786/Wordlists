import cv2 
#Here i am importing the cv2 module

"""Here is a code created which will launch a webcam if detected and start recording in color untill the user presses the letter 'q' on their keyboard,
which then would save the recording to the location of this code."""

cap = cv2.VideoCapture(0)
#Here im assigning the video output to the word cap.

fourcc = cv2.VideoWriter_fourcc(*'XVID')
#This will be the codec used for the video output.

foutput = cv2.VideoWriter('Recording.avi', fourcc, 24.0, (640,480))
#Here is the settings of the webcam that will be outputted, e.g. the recording that will be saved will be called 'Recording' and will have the 'avi' video format.

while True:
    ret, color_recording = cap.read()
    foutput.write(color_recording)
    
#    grey = cv2.cvtColor(color_recording, cv2.COLOR_BGR2GRAY)
    
    ('Color recording',color_recording)
#    ('Grey recording',grey)

#To get in greyscale remove comment starting with "grey =" + "('Grey recording',grey)"
#To make the webcam appear simply type, "cv2.imshow" before any of the code in brackets located 1 comment above this comment.

    if cv2.waitKey(1) & 0xFF == ord('q'):
      cap.release()
      break
#This while loop will output the recoding in a colour format and will display the window as 'Recording'.
#It will also keep the webcam recording going untill the user presses the letter 'q' on their keyboard which then would stop the recording and release the webcam if another application wants to use it.

foutput.release()
cv2.destroyAllWindows()
#These commands will stop the entire recording and will close any open windows asscociated with this recording.
