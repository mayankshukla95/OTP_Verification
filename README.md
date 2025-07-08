# OTP Verification GUI (Python/Tkinter)

## Overview

A simple desktop app to send a 6-digit OTP to your Gmail and verify it using a graphical interface.

## Features

* Email OTP to yourself using Gmail SMTP
* 6-digit random OTP generation
* 3 verification attempts
* Built with Tkinter (no external libraries)

## Usage

1. Run the script: `python otp_gui.py`
2. Enter your Gmail address and click **Send OTP**
3. Check your email and enter the OTP in the app
4. You have up to 3 attempts to verify it

## Requirements

* Python 3.8+
* Gmail account with either:

  * App Password (recommended)
  * Or temporarily enabled "Less secure apps" (for quick tests)

## Screenshots

![Email Entry](docs/demo_email.png)
![OTP Entry](docs/demo_otp.png)

## Notes

* Keep your email password secure – never hard-code it
* The same Gmail is used as both sender and recipient

## Author

**Mayank Shukla**
[LinkedIn](https://www.linkedin.com/in/mayank-shukla)

---

*Project created for learning and demonstration purposes.*
