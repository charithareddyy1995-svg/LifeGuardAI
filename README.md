# 🛡️ LifeGuardAI

A Python-based computer vision application that monitors a person through a webcam and detects prolonged inactivity. If no movement is detected for a specified duration, the system plays an alarm and automatically sends a WhatsApp alert using the Twilio API.

---

## 📖 About the Project

LifeGuardAI is designed to improve the safety of elderly people and individuals living alone by continuously monitoring movement through a webcam. The application uses OpenCV to detect motion in real time. If inactivity exceeds a predefined threshold, the system immediately triggers an audible alarm and sends an emergency WhatsApp notification to a registered contact.

This project demonstrates the practical use of computer vision and cloud communication APIs for real-world safety applications.

---

## ✨ Features

- 📷 Real-time webcam monitoring
- 🚶 Motion detection using OpenCV
- ⏱️ Inactivity detection based on a configurable time threshold
- 🔔 Audible alarm using Windows Beep
- 📱 Automatic WhatsApp alert using Twilio API
- ⚙️ Easy configuration of alert duration
- 💻 Lightweight and simple Python implementation

---

## 🛠️ Technology Stack

- Python 3.8+
- OpenCV
- Twilio API
- Winsound (Windows)
- Computer Vision

---

## 📂 Project Structure

```
LifeGuardAI/
│── README.md
│── main.py
│── requirements.txt
│── .gitignore
│── LICENSE
│── assets/
│     ├── architecture.png
│     ├── output.png
│     └── demo.gif
```

---

## ⚙️ Prerequisites

Before running the project, ensure you have:

- Windows Operating System
- Python 3.8 or later
- Webcam connected and accessible
- Twilio Account
- Twilio WhatsApp Sandbox configured

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/LifeGuardAI.git
```

Move into the project directory:

```bash
cd LifeGuardAI
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
.\.venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

Open `main.py` and update the following values:

- Twilio Account SID
- Twilio Auth Token
- Recipient WhatsApp Number
- Twilio WhatsApp Sandbox Number (if different)

Example:

```python
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"
```

---

## ▶️ Running the Project

Run the application:

```bash
python main.py
```

The webcam window will open and begin monitoring for movement.

Press **Esc** to close the application.

---

## ⚙️ Configuration Notes

- The inactivity threshold is currently set to **10 seconds** for testing.
- For real-world usage, increase the threshold (for example, 300–1200 seconds).
- Ensure your Twilio WhatsApp Sandbox is activated before testing alerts.

---

## 📸 Screenshots

*Screenshots will be added soon.*

## 🚀 Future Improvements

- Face recognition
- Human pose estimation
- Heart rate estimation
- Breathing rate estimation
- AI-based anomaly detection
- Azure AI integration
- Power BI dashboard
- SMS and Email alerts
- Mobile application
- Cloud deployment

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Nandhagiri Charitha Reddy**

- **GitHub:** [charithareddyy1995-svg](https://github.com/charithareddyy1995-svg)
- **LinkedIn:** [Charitha Reddy Nandhagiri](https://www.linkedin.com/in/charithareddynandhagiri)

⭐ If you found this project useful, consider giving it a star on GitHub!
