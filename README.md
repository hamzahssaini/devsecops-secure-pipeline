# 🛡️ Enterprise DevSecOps Platform Demo

Welcome to the DevSecOps Pipeline Showcase! This project acts as an interactive, educational demonstration of a modern CI/CD platform integrating crucial security checks directly into the Software Development Life Cycle (SDLC).

It features a responsive Bootstrap 5 Dashboard representing continuous security asset monitoring, backed by a Flask API and an end-to-end GitHub Actions pipeline.

---

## 🏗️ Architecture Explanation

1. **Flask REST API**: Serves as the Backend. Manages notes (assets) and serves the `GET /metrics` route to dynamically calculate vulnerability statuses in live code.
2. **Modern Security Dashboard**: An enterprise-style SaaS dashboard built securely on vanilla JS and Bootstrap. Polls for live code health metrics.
3. **Docker**: A production-ready, rootless container implementation running slim Python.
4. **GitHub Actions CI/CD**: A fully automated pipeline implementing multiple DevSecOps gates.

---

## 🚦 DevSecOps Workflow Explanation

The CI/CD pipeline implements a "Shift Left" mentality, discovering issues as soon as code is pushed to GitHub:

1. **TruffleHog (Secret Scanning)**: Scans every commit for active leaked credentials (API keys, Tokens) preventing cloud compromises.
2. **Bandit (SAST - Static Application Security Testing)**: Reads raw Python code without executing it. Searches for dangerous functions (like `exec()` or `eval()`) to prevent Code Injections (CWE-94).
3. **pip-audit (SCA - Software Composition Analysis)**: Reviews `requirements.txt` against vulnerability databases to block CVEs hiding in third-party libraries.
4. **Trivy (Container Image Scanning)**: Analyzes the built Docker image OS layers to ensure you aren't shipping unpatched Debian/Alpine vulnerabilities to the cluster.

---

## 🎭 Educational Scenarios

### The "Red Pipeline" Scenario (Failed)
The project includes a `demos/` folder designed intentionally to trigger security alarms for presentations:
- **Fake API Leaks**: `demos/fake_keys.py` contains fake AWS/Stripe tokens. TruffleHog will catch these.
- **Dangerous Eval**: `demos/vulnerable_code.py` uses python's `eval()`. Bandit will throw a `CWE-94` critical finding.
- **Insecure Container**: `Dockerfile.insecure` runs as root and utilizes old python versions.
By pushing these, you will demonstrate the pipeline turning **RED**, blocking the deployment.

### The "Green Pipeline" Scenario (Clean)
1. Delete or fully comment out files in the `demos/` directory.
2. Make sure `requirements.txt` does *not* have `requests==2.20.0` active.
3. Push to GitHub.
Watch the GitHub actions gracefully clear every gate, resulting in a **GREEN**, successful deployment.

---

## 🚀 Running Locally

```bash
# 1. Create Environment
python -m venv venv
# Windows: .\venv\Scripts\activate | Mac/Linux: source venv/bin/activate

# 2. Install Packages
pip install -r requirements.txt

# 3. Spin up Server
python app/main.py
```
Open `http://localhost:5000` to view the Enterprise Dashboard.
