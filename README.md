# Enterprise DevSecOps Pipeline Architecture 🛡️

![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge&logo=githubactions)
![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Security](https://img.shields.io/badge/Security-A+-success?style=for-the-badge&logo=security)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker)

## Executive Summary
This repository serves as a comprehensive demonstration of a modern **Enterprise DevSecOps Pipeline**. It showcases the practical implementation of the "Shift-Left" security philosophy by integrating rigorous automated security checks directly into the Continuous Integration and Continuous Deployment (CI/CD) workflow. 

By enforcing strict quality and security gates, this pipeline ensures that no secrets, vulnerable code, or insecure dependencies reach production.

---

## 🏗️ Pipeline Architecture

The pipeline is orchestrated via **GitHub Actions** and enforces mandatory verification across four critical security domains:

\\mermaid
graph LR
    A[Developer Commits] --> B{Push Protection}
    B -->|Blocked| Z[Secret Detected]
    B -->|Passed| C(GitHub Actions CI)
    
    subalign CI Pipeline
    C --> D[1. Secret Scanning<br>TruffleHog]
    D --> E[2. SAST<br>Bandit]
    E --> F[3. SCA<br>pip-audit]
    F --> G[4. Container Scan<br>Trivy]
    end
    
    G --> H((Secure Deploy))
\
---

## ⚙️ Security Integration Matrix

| Stage | Security Tool | Purpose | Threat Mitigated (CWE/OWASP) |
|---|---|---|---|
| **Pre-Commit** | *GitHub Push Protection* | Blocks active tokens from remote history | Sensitive Data Exposure |
| **1. Secret Scan** | **TruffleHog** | Deep repository scan for hardcoded credentials | CWE-798: Hardcoded Credentials |
| **2. SAST** | **Bandit** | Static analysis of Python AST | CWE-605, CWE-94 (Insecure Coding) |
| **3. SCA** | **pip-audit** | Software Composition Analysis | OWASP A06: Vulnerable Components |
| **4. Image Scan** | **Trivy** | Evaluates Docker image OS layers | Zero-day Infrastructure Vulnerabilities |

---

## 🚀 Demonstration Guide

This repository contains intentional flaws commented out to demonstrate the efficacy of the pipeline. To experience the security gates in action:

1. **Test Secret Scanning (TruffleHog):** 
   Uncomment the \DATABASE_URL\ string containing a credential in \pp/routes.py\.
2. **Test SAST (Bandit):** 
   Remove the \# nosec B104\ directive from the Flask \pp.run\ command in \pp/main.py\.
3. **Test SCA (pip-audit):** 
   Add equests==2.19.0\ to equirements.txt\.

---

## 📊 Comprehensive Documentation
For a deep dive into the business value, ROI, and technical specifics of this DevSecOps implementation, please refer to our internal documentation:
* [📖 High-Level Technical Report](docs/REPORT.md)
* [📊 Executive Presentation Deck](docs/PRESENTATION.md)
