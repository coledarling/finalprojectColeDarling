### INF601 - Advanced Programming in Python  
### Cole Darling  
### Final Project  

## Description
This project is a Flask-based web application designed to analyze password strength and check whether a password has been exposed in known data breaches using the **Have I Been Pwned API**.  

The PasswordAnalyzer helps users create **stronger passwords** and provides **warnings** if a password has been previously compromised, ensuring better security practices.  

## Getting Started  

### Dependencies

```
pip install -r requirements.txt
```

### Executing program

```
python PasswordAnalyzer.py
```

### Output
The web interface will:

- Analyze password strength based on length, character diversity, and complexity.
- Check if the password has appeared in known data breaches.
- Warn users if a strong password has been found in a breach.

## Authors

Contributors names and contact info

ex. Cole Darling

## Acknowledgments

API Used: [Have I Been Pwned Password API](https://haveibeenpwned.com/) 
Technologies: Flask, Requests, SHA-1 hashing
