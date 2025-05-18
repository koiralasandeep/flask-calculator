# 🧮 Web Calculator with Flask

A user-friendly web calculator built using **Flask** and **Bootstrap**, offering both **basic arithmetic operations** and **advanced math functions** like trigonometry and square root.

## 🔍 Overview

This project showcases how to build a full-featured web application using Flask. It includes:
- A homepage with navigation
- A simple calculator for basic math
- An advanced calculator with trigonometric and square root functions
- Clean UI using Bootstrap 5

## ✨ Features

### ✅ Simple Calculator
- Addition
- Subtraction
- Multiplication
- Division

### 🔬 Advanced Calculator
- `sin(x)`
- `cos(x)`
- `tan(x)`
- `√x` (square root)

### 📱 Responsive UI
- Built with [Bootstrap 5](https://getbootstrap.com/)
- Mobile-friendly layout
- Inline alerts for success and errors

## 🛠 Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, Bootstrap
- **Templating**: Jinja2

## 🚀 How to Run Locally

### Prerequisites
- Python 3.6+
- `pip` installed

### Installation & Execution
# Step 1: Install Flask
pip install flask

# Step 2: Run the application
python index.py
Visit http://127.0.0.1:5000 in your browser.

🗂 Project Structure
bash
Copy
Edit
├── index.py              # Main Flask app
├── templates/
│   ├── index.html        # Base layout
│   ├── simple.html       # Simple calculator UI
│   └── advanced.html     # Advanced calculator UI
📌 Routes
Route	Description
/	Homepage
/simple	Simple calculator
/advanced	Advanced calculator
/calculate	POST route for simple calc logic
/calculate_advanced	POST route for advanced calc logic

📸 Screenshots
<img width="1920" alt="Screenshot 2025-05-18 at 11 54 44 AM" src="https://github.com/user-attachments/assets/506236e3-8080-4be0-8114-6a046bbff4f6" />


