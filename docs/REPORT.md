# DevSecOps Pipeline Implementation Report

<div align="center">
  <h3><strong>School:</strong> Supemir</h3>
  <p><strong>Authors:</strong> Hamza Hssaini & Anouar</p>
  <p><strong>Project:</strong> Securing a CI/CD Pipeline (DevSecOps)</p>
  <p><strong>Date:</strong> May 2026</p>
</div>

---

## 1. Executive Summary
This report details the implementation of a professional **DevSecOps pipeline**. The primary objective of this project is to demonstrate the integration of security tools directly into the CI/CD workflow rather than focusing on application development. We used a simple, minimalistic Python/Flask application as a vessel to showcase how security constraints, vulnerability scanning, and compliance can be enforced automatically before any code reaches production.

By adopting a **"Shift-Left"** approach, we ensure that secrets, vulnerable dependencies, insecure code patterns, and flawed container configurations are caught at the commit stage, maintaining both development velocity and high security standards.

---

## 2. Project Scope & Objectives
We strictly assumed the roles of **DevOps/DevSecOps Engineers**. Our focus was on infrastructure, automation, and security gating.

**Objectives:**
1. Provision an automated pipeline using GitHub Actions.
2. Integrate continuous security checks (Secret Scanning, SAST, SCA, Container Scanning).
3. Enforce a "Fail-Fast" mechanism to block vulnerable code from being deployed.
4. Establish clear visibility of security metrics and scan results.

---

## 3. Architecture & Workflow

*Our pipeline is structured into multiple robust security gates. If any step detects a critical vulnerability, the pipeline breaks, preventing the deployment of insecure artifacts.*

> ?? **[SCREENSHOT 1: GitHub Actions Architecture]**
> *Action to take:* Go to the "Actions" tab in your GitHub repository, click on your most recent successful workflow run, and take a screenshot of the visual graph showing jobs (TruffleHog -> Bandit -> Pip-Audit -> Docker Build -> Trivy).

### Pipeline Stages

1. **Source Code Check-in & Secret Scanning**
2. **Static Application Security Testing (SAST)**
3. **Software Composition Analysis (SCA)**
4. **Containerization & Image Scanning**

---

## 4. Implementation Details & Evidence

### 4.1. Secret Scanning (TruffleHog)
**Concept:** Prevent leaked credentials (API keys, passwords, tokens) from being pushed to the repository.
**Tool Used:** TruffleHog.

> ?? **[SCREENSHOT 2: Secret Scan Step]**
> *Action to take:* Click on the "Secret Scanning" job in GitHub Actions. Expand the logs where it shows "TruffleHog" running. Take a screenshot showing the clean output (or blocked commit if you pushed a fake secret).

### 4.2. Static Application Security Testing - SAST (Bandit)
**Concept:** Analyze the source code for insecure coding practices (e.g., hardcoded passwords, unsafe imports, shell injections) without running the application.
**Tool Used:** Bandit (Python).

> ?? **[SCREENSHOT 3: SAST Execution]**
> *Action to take:* Expand the "Bandit SAST" job logs in GitHub Actions to show the summary of the scan. Highlighting Total lines of code, Issues found: 0, etc.

### 4.3. Software Composition Analysis - SCA (pip-audit)
**Concept:** Audit the application's third-party dependencies (equirements.txt) against known CVE databases.
**Tool Used:** pip-audit / Safety.

> ?? **[SCREENSHOT 4: SCA Dependency Check]**
> *Action to take:* Expand the "SCA" job logs. Take a screenshot showing pip-audit scanning the environment and returning no known vulnerabilities.

### 4.4. Containerization & Infrastructure Security (Trivy)
**Concept:** The simple app is packaged into a Docker container. We scan the Docker image (OS packages and application libraries) for vulnerabilities before pushing it to a registry.
**Tool Used:** Aqua Security Trivy.

> ?? **[SCREENSHOT 5: Dockerfile & Trivy Image Scan]**
> *Action to take:* 
> 1. Take a screenshot of the clean Dockerfile minimizing privileges (e.g., using a non-root user).
> 2. Take a screenshot of the "Trivy Container Scan" job logs in GitHub Actions showing the table of CVEs (if any) or the success message.

---

## 5. Security Enforcements & Best Practices Applied

To truly emphasize the DevSecOps engineering aspect, the following practices were heavily enforced:
- **Minimalistic Codebase:** We stripped the application down to bare essentials. The app does not matter; the pipeline does.
- **Fail-Fast Policy:** Jobs are strictly dependent on one another. If Bandit fails, Docker Build doesn't even start.
- **Least Privilege:** The application runs as a non-root user within the Docker container to mitigate container breakout attacks.

> ?? **[SCREENSHOT 6: A Blocked/Failed Pipeline]**
> *Action to take:* Add a fake vulnerable package (like an ancient version of Django) or push a fake API key temporarily. Take a screenshot of the pipeline **turning RED** and failing. This is the **most impressive** slide for the jury, proving the pipeline actually blocks bad code!

---

## 6. Conclusion
This project successfully demonstrates the transition from DevOps to **DevSecOps**. By introducing automated tooling at every stage of the Software Development Life Cycle (SDLC), we guarantee that security is an enabler of quality, not a bottleneck.

**Prepared for:** Supemir Jury  
**Presented by:** Hamza Hssaini & Anouar
