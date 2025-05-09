import requests

SECURITY_HEADERS = {
    "Content-Security-Policy": "Helps stop script attacks.",
    "Strict-Transport-Security": "Makes sure the website uses HTTPS.",
    "X-Frame-Options": "Stops clickjacking tricks.",
    "X-Content-Type-Options": "Prevents dangerous file guessing.",
    "Referrer-Policy": "Keeps browsing history safe.",
    "Permissions-Policy": "Blocks sneaky browser features.",
    "Cross-Origin-Resource-Policy": "Keeps resources safe from outsiders."
}

def check_headers(url):
    try:
        response = requests.get(url, timeout=10)
        headers = response.headers

        print(f"\nSecurity Header Check for: {url}\n{'-'*50}")
        for header, description in SECURITY_HEADERS.items():
            if header in headers:
                print(f"[+] {header}: ✅ Found")
            else:
                print(f"[-] {header}: ❌ Missing - {description}")
    except requests.exceptions.RequestException as e:
        print(f"Oops! Couldn’t reach {url}. Error: {e}")

if __name__ == "__main__":
    target_url = input("Type a website URL (include https://): ").strip()
    check_headers(target_url)
