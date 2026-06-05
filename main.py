import cv2
import time
import winsound
from twilio.rest import Client

# ================== TWILIO SETUP ==================
account_sid = "YOUR_SID"
auth_token = "YOUR_TOKEN"

client = Client(account_sid, auth_token)

def send_whatsapp():
    client.messages.create(
        body="⚠️ LifeguardAI Alert: No movement detected!",
        from_='whatsapp:+14155238886',   # Twilio sandbox
        to='whatsapp:+91XXXXXXXXXX'      # Your number
    )

# ================== CAMERA ==================
cap = cv2.VideoCapture(0)

ret, frame1 = cap.read()
ret, frame2 = cap.read()

last_movement_time = time.time()
THRESHOLD = 10   # keep 10 for testing (later change to 1200)

alert_sent = False

# ================== MAIN LOOP ==================
while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)

    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    movement_detected = False

    for contour in contours:
        if cv2.contourArea(contour) > 1000:
            movement_detected = True
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Reset timer if movement
    if movement_detected:
        last_movement_time = time.time()
        alert_sent = False

    # ALERT CONDITION
    if time.time() - last_movement_time > THRESHOLD and not alert_sent:
        print("⚠️ ALERT TRIGGERED!")

        # Beep sound
        for _ in range(5):
            winsound.Beep(1000, 500)

        # WhatsApp message
        try:
            send_whatsapp()
        except Exception as e:
            print(f"Failed to send WhatsApp message: {e}")

        alert_sent = True

    # Show alert on screen
    if alert_sent:
        cv2.putText(frame1, "ALERT: No Movement!", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    cv2.imshow("LifeguardAI", frame1)

    frame1 = frame2
    ret, frame2 = cap.read()
    if not ret:
        break

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
