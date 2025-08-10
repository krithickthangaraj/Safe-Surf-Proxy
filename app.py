from flask import Flask, request, render_template, redirect, jsonify, make_response
import requests
from urllib.parse import urlparse
import threading

app = Flask(__name__)

blocked_sites = {"www.instagram.com", "www.facebook.com"}
logs = []
unblock_requests = []
approved_domains = set()
admin_password = "admin123"
latest_request = {"domain": None, "reason": None}

@app.route('/')
def home():
    return "Proxy server is running. Go to /proxy?url=https://www.instagram.com"

@app.route('/proxy')
def proxy():
    url = request.args.get('url')
    if not url:
        return "URL is required", 400

    parsed = urlparse(url)
    domain = parsed.netloc

    # If blocked
    if domain in blocked_sites:
        requested = any(req[0] == domain for req in unblock_requests)
        return render_template("blocked.html", domain=domain, requested=requested)

    try:
        resp = requests.get(url)
        return resp.text
    except Exception as e:
        return f"Error fetching URL: {e}"

@app.route('/request-unblock', methods=['POST'])
def request_unblock():
    domain = request.form.get('domain')
    reason = request.form.get('reason')
    if domain and reason:
        unblock_requests.append((domain, reason))
        logs.append(f"📝 Unblock request for {domain}: {reason}")
        latest_request['domain'] = domain
        latest_request['reason'] = reason
    return redirect(f"/proxy?url=https://{domain}")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html", blocked_sites=blocked_sites, logs=logs, unblock_requests=unblock_requests)

@app.route('/new_logs')
def new_logs():
    if latest_request['domain']:
        return jsonify({"new_domain": latest_request['domain']})
    return jsonify({})

@app.route('/allow', methods=['POST'])
def allow():
    domain = request.form.get('domain')
    password = request.form.get('password')

    if password == admin_password and domain in blocked_sites:
        blocked_sites.remove(domain)
        logs.append(f"✅ Admin allowed access to {domain}")
        approved_domains.add(domain)

        # Remove request from list
        global unblock_requests
        unblock_requests = [req for req in unblock_requests if req[0] != domain]

        # Clear latest request
        if latest_request['domain'] == domain:
            latest_request['domain'] = None
            latest_request['reason'] = None

        return '', 204  # Don't redirect admin
    else:
        logs.append(f"❌ Wrong password attempt for {domain}")
        return "Unauthorized or wrong password", 403

@app.route('/check-unblocked')
def check_unblocked():
    domain = request.args.get('domain')
    if domain in approved_domains:
        approved_domains.remove(domain)
        return jsonify({"unblocked": True})
    return jsonify({"unblocked": False})

if __name__ == "__main__":
    app.run(debug=True)
