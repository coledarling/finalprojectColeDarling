'''
INF601 - Programming in Python
Assignment# Final Project
I, Cole Darling, affirm that the work submitted for this assignment is entirely my own. I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials. I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards. I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.
'''

from flask import Flask, request, render_template
import requests
import hashlib

app = Flask(__name__)


# Check password strength
def analyze_password(password):
    if len(password) < 8:
        return "Weak: Password is too short. Use at least 8 characters."
    elif password.isalpha():
        return "Weak: Password shouldn't be all letters."
    elif password.isnumeric():
        return "Weak: Password shouldn't be all numbers."
    elif all(char in "!@#$%^&*()-_+=<>?/" for char in password):
        return "Weak: Password shouldn't be only special characters."
    elif not any(char in "!@#$%^&*()-_+=<>?/" for char in password):
        return "Weak: Password should include at least one special character (!@#$%^&*()-_+=<>?/)."
    else:
        return "Strong: Your password looks good!"


# Check if password has been found in breaches
def check_breach(password):
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()
    first_five_chars = sha1_password[:5]
    url = f"https://api.pwnedpasswords.com/range/{first_five_chars}"
    response = requests.get(url)

    if response.status_code != 200:
        return "Error checking password breaches."

    if sha1_password[5:] in response.text:
        return "Your password has been found in a data breach!"
    else:
        return "Your password has NOT been found in a breach."


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        password = request.form.get("password")  # Get user input
        if password:
            # Perform both strength and breach analysis
            strength = analyze_password(password)
            breach = check_breach(password)

            # Contingent logic: Strong but breached
            if "Strong" in strength and "found in a data breach" in breach:
                result = "Strong: Your password looks good based on the requirements for a strong password. | However, it has been found in a data breach. WOULD NOT ADVISE USING IT!"
            else:
                result = f"{strength} | {breach}"

            return render_template("index.html", result=result)
    return render_template("index.html", result="")  # Default page


if __name__ == "__main__":
    app.run(debug=True)