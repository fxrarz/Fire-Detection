
import cv2
import numpy as np
import os
# import smtplib
# import playsound
# import threading

# Alarm_Status = False
# Email_Status = False
# Fire_Reported = 0

# def play_alarm_sound_function():
# 	while True:
# 		playsound.playsound('alarm-sound.mp3',True)

# def send_mail_function():

#     recipientEmail = "Enter_Recipient_Email"
#     recipientEmail = recipientEmail.lower()

#     try:
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.ehlo()
#         server.starttls()
#         server.login("Enter_Your_Email (System Email)", 'Enter_Your_Email_Password (System Email')
#         server.sendmail('Enter_Your_Email (System Email)', recipientEmail, "Warning A Fire Accident has been reported on ABC Company")
#         print("sent to {}".format(recipientEmail))
#         server.close()
#     except Exception as e:
#     	print(e)


# video = cv2.VideoCapture(0) # If you want to use webcam use Index like 0,1.
file_path = "images/burning-wood-ignites-vibrant-campfire-nature-generated-by-ai_24640-87948.jpg"

img_files = []
for im in os.listdir('images/'):
    img_files.append(os.path.join('images/', im))

print(img_files)
img = enumerate(img_files)
def get_image():
    im = cv2.imread(next(img)[1])
    # print(im)
    return im

for i in img_files:
    frame = get_image()

    frame = cv2.resize(frame, (960, 540))

    blur = cv2.GaussianBlur(frame, (21, 21), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    lower = [18, 50, 50]
    upper = [35, 255, 255]
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    mask = cv2.inRange(hsv, lower, upper)

    output = cv2.bitwise_and(frame, hsv, mask=mask)

    no_red = cv2.countNonZero(mask)

    if int(no_red) > 1500:
        print('fire')
    else:
        print('no fire')
        # Fire_Reported = Fire_Reported + 1

    cv2.imshow("output", output)
    cv2.waitKey(0)

    # if Fire_Reported >= 1:

    	# if Alarm_Status == False:
    		# threading.Thread(target=play_alarm_sound_function).start()
    		# Alarm_Status = True

    	# if Email_Status == False:
    		# threading.Thread(target=send_mail_function).start()
    		# Email_Status = True


    # if cv2.waitKey(0) & 0xFF == ord('q'):
    #     break

cv2.destroyAllWindows()
