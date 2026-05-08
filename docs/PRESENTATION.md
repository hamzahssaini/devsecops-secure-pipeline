# DevSecOps Pipeline Showcase - Presentation

## Slide 1: Title Screen
**Title:** Shifting Security Left: An Enterprise DevSecOps Implementation
**Speaker:** Hamza
**Goal:** Demonstrate an automated CI/CD pipeline featuring Secret Scanning, SAST, SCA, and Container Vulnerability Scanning.

---

## Slide 2: Why DevSecOps?
- **The Problem:** Traditional security happens at the *end* of the pipeline. Finding a flaw late means costly delays.
- **The Solution:** "Shift-Left" - Move security checks directly into developer workflows (Code Push).
- **The Workflow:** GitHub Actions tests the code simultaneously for bugs **and** vulnerabilities.

---

## Slide 3: Project Architecture
*(Show the Mermaid Architecture Diagram here)*
- Developer pushes code to GitHub.
- 4 Parallel/Sequential Gates perform security triage.
- Only a 100% clean build generates a secure Docker image limit.

---

## Slide 4: Scenario 1 - Secret Scanning (TruffleHog)
- **Concept:** Developers accidentally commit cloud API keys or passwords.
- **Red Demo:** Show `demos/fake_keys.py` containing a Stripe API Key. Show TruffleHog failing the build.
- **The Fix:** Remove the hardcoded keyword. Show TruffleHog passing. 

---

## Slide 5: Scenario 2 - SAST (Bandit)
- **Concept:** Static Code Analysis. Finding structural logic flaws in Python.
- **Red Demo:** Show `eval(user_input)` or `SECRET_API_KEY` assignments. Show Bandit aborting the build for `CWE-94 / CWE-259`.
- **The Fix:** Explain how `# nosec` is used to allow intentional exceptions (like Docker `0.0.0.0`), while enforcing secure coding practices.

---

## Slide 6: Scenario 3 - SCA (pip-audit)
- **Concept:** Checking 3rd party Open-Source vulnerabilities.
- **Red Demo:** Change `requirements.txt` to use Flask 3.0.0. Show pip-audit alerting that CVEs exist.
- **The Fix:** Upgrade to Flask `3.1.3` and Werkzeug `3.1.6`. Prove the vulnerabilities disappear.

---

## Slide 7: Scenario 4 - Container Scans (Trivy)
- **Concept:** The OS layer inside our Docker Container must be patched.
- **Red Demo:** Downgrade the Docker base image to `python:3.9.0-slim` (a 2020 image). Show Trivy identifying critical debian OS CVEs.
- **The Fix:** Move to a modern, patched image `python:3.11-slim`. Shows Trivy returning **0 Vulnerabilities**.

---

## Slide 8: Conclusion
- **Result:** Complete defensive automation.
- **Impact:** Decreased risk of deployment vulnerabilities, automated enforcement of coding standards.
- **Q&A**