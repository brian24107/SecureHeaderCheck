# SecureHeaderCheck

A simple Python-based tool to analyze the presence of critical HTTP security headers on websites. This tool helps identify missing headers that can expose web applications to common vulnerabilities such as XSS, clickjacking, and insecure transport channels.

---

## 📌 Features

- Checks for the following HTTP security headers:
  - `Content-Security-Policy`
  - `Strict-Transport-Security`
  - `X-Frame-Options`
  - `X-Content-Type-Options`
  - `Referrer-Policy`
  - `Permissions-Policy`
  - `Cross-Origin-Resource-Policy`
- Provides human-readable explanations for why each header matters.
- Simple command-line interface for quick checks.
- Lightweight and easy to extend.

---

## 🚀 Usage

1. **Install Dependencies**  
   ```bash
   pip install requests
