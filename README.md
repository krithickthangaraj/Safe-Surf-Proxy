# Flask Web Proxy with Site Blocking & Admin Approval

This project is a **Flask-based web proxy application** that allows users to browse websites through a proxy while enabling an **admin to block/unblock specific sites** dynamically.  
It includes a dashboard for real-time monitoring, unblock requests, and password-protected admin approval.

---

## 🚀 Features
- **Site Blocking** – Prevents access to specified domains.
- **Unblock Requests** – Users can submit a request with a reason when a site is blocked.
- **Admin Dashboard** – Displays unblock requests in real-time with approval popups.
- **Password-Protected Approval** – Only admins can approve unblock requests.
- **Real-Time Updates** – Once approved, the user gets a success message and auto-redirect.
- **Request Logging** – All access attempts and unblock requests are logged in the dashboard.

---

## 🖼 Dashboard Preview
<img width="1439" height="781" alt="Screenshot 2025-08-10 at 10 05 46 AM" src="https://github.com/user-attachments/assets/9a3b2543-d46c-40fe-97b2-4731309627bd" />


---

## 🛠 Installation

### 1. Clone the repository and setup environment

```bash
git clone https://github.com/yourusername/flask-proxy-app.git
cd flask-proxy-app
python3 -m venv venv
source venv/bin/activate      # For macOS/Linux
# OR
venv\Scripts\activate         # For Windows
pip install -r requirements.txt
python app.py


2. Access the app
Proxy: http://127.0.0.1:5000

Dashboard: http://127.0.0.1:5000/dashboard
```
