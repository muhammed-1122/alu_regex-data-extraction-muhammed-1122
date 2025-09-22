# Regex Data Extraction Project

This project demonstrates the use of **Regular Expressions (Regex)** in Python to extract structured data from unstructured text. It can dynamically recognize patterns from **user input** or pasted text.

---

## Features

This script can extract the following **8 types of data**:

1. **Email addresses**  
   Example: `user@example.com`, `firstname.lastname@company.co.uk`

2. **URLs**  
   Example: `https://www.example.com`, `https://subdomain.example.org/page`

3. **Phone numbers**  
   Formats: `(123) 456-7890`, `123-456-7890`, `123.456.7890`

4. **Credit card numbers**  
   Formats: `1234 5678 9012 3456`, `1234-5678-9012-3456`

5. **Times** (12-hour and 24-hour formats)  
   Examples: `14:30`, `2:30 PM`

6. **HTML tags**  
   Examples: `<p>`, `<div class="example">`, `<img src="image.jpg" alt="description">`

7. **Hashtags**  
   Examples: `#example`, `#ThisIsAHashtag`

8. **Currency amounts**  
   Examples: `$19.99`, `$1,234.56`

---

## Setup Instructions

### 1. Clone the repository:
git clone https://github.com/muhammed-1122/alu_regex-data-extraction-muhammed-1122.git
cd alu_regex-data-extraction-muhammed-1122

###2. Run the python program:
python3 app.py
Make sure Python 3 is installed. No additional libraries are required.

**How to Use the Program**
Paste or type text into the terminal.

Multi-line input is supported.

The program reads until you type the sentinel word END on a new line.

Finish your input by typing:
`END` in a new line, make sure it is in uppercase

###3. Use the sample text on sample.txt to test the program

