# LifeguardAI

> Simple motion-detection alert script that beeps and sends a WhatsApp alert via Twilio when no movement is detected.

- **File:** mai.py

**Prerequisites**
- Windows (uses `winsound` for beep).
- Python 3.8+
- A webcam connected and accessible.
- A Twilio account with WhatsApp sandbox configured.

**Install**

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install opencv-python twilio
```

**Configuration**
- Open `mai.py` and replace `YOUR_SID` and `YOUR_TOKEN` with your Twilio `account_sid` and `auth_token`.
- Replace the `to` phone number in `send_whatsapp()` with your WhatsApp-enabled number (international format).
- Ensure your Twilio WhatsApp sandbox `from` number is correct (`+14155238886` is the default sandbox).

**Run**

```powershell
python mai.py
```

- Press `Esc` to quit the window.

**Notes**
- `THRESHOLD` in `mai.py` is set to `10` seconds for testing — change to a larger value (e.g., `1200`) for production.
- If WhatsApp messages fail, check your Twilio credentials and sandbox configuration.
