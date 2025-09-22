#!/usr/bin/env python3
import re

# 1. Email addresses
email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b')

# 2. URLs
url_pattern = re.compile(r'https?://[^\s<>"]+')

# 3. Phone numbers
phone_pattern = re.compile(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}')

# 4. Credit card numbers
credit_pattern = re.compile(r'\b(?:\d{4}[-\s]?){3}\d{4}\b')

# 5. Time (12h & 24h)
time_pattern = re.compile(r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][.]?[Mm][.]?)?\b')

# 6. HTML tags
html_pattern = re.compile(r'<[^>]+>')

# 7. Hashtags
hashtag_pattern = re.compile(r'#\w+')

# 8. Currency amounts ($19.99, $1,234.56)
currency_pattern = re.compile(r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?')

patterns = {
    "Emails": email_pattern,
    "URLs": url_pattern,
    "Phone Numbers": phone_pattern,
    "Credit Cards": credit_pattern,
    "Times": time_pattern,
    "HTML Tags": html_pattern,
    "Hashtags": hashtag_pattern,
    "Currency Amounts": currency_pattern
}

# --- Multi-line input ---
print("Enter text (type END on a new line to finish):")

lines = []
while True:
    line = input()
    if line.strip().upper() == "END":
        break
    lines.append(line)

user_input = "\n".join(lines)

# --- Extract patterns ---
for name, pattern in patterns.items():
    matches = pattern.findall(user_input)
    print(f"{name}: {matches if matches else 'No matches found'}")
