import random, smtplib, tkinter as tk
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import messagebox

otp, attempts_left = "", 3

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp():
    global otp, attempts_left
    email = email_entry.get().strip()

    if not email:
        messagebox.showerror("Error", "Please enter your email.")
        return
    
    otp = generate_otp()
    attempts_left = 3
    verify_button.config(state="normal")

    password = "hndm vfxy dfin fqsp"

    message = MIMEMultipart()
    message["From"] = email
    message["To"] = email
    message["Subject"] = "Self-Sent Email from Python"

    body = f"Hey Mayank!\n\nYour OTP is {otp} (3 attempts only)."
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(email, password)
            server.sendmail(email, email, message.as_string())
        messagebox.showinfo("Success", "OTP sent successfully!")

        for w in (email_label, email_entry, send_button):
            w.pack_forget()

        otp_label.pack(pady=5)
        otp_entry.pack()
        verify_button.pack(pady=10)


    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email : {e}")


def verify_otp():
    global attempts_left

    if attempts_left <= 0:
        messagebox.showwarning("Locked", "No attempts left. Please request a new OTP.")
        return
    
    if otp_entry.get().strip() == otp:
        messagebox.showinfo("Success", "OTP Verified !")
        verify_button.config(state="disabled")

    else:
        attempts_left -= 1
        if attempts_left > 0:
            messagebox.showerror("Error", f"Incorrect OTP {attempts_left} attempt(s) left.")
        else:
            messagebox.showerror("Error", "Incorrect OTP. No attempts left.")
            verify_button.config(state="disabled")

root = tk.Tk()
root.title("OTP Verification")
root.geometry("300x150")
root.resizable(False, False)

email_label = tk.Label(root, text="Enter Email :")
email_label.pack(pady=5)

email_entry = tk.Entry(root, width = 30)
email_entry.pack()

send_button = tk.Button(root, text="Send OTP", command=send_otp)
send_button.pack(pady=10)

otp_label = tk.Label(root, text="Enter OTP:")
otp_entry = tk.Entry(root, width = 10)

verify_button = tk.Button(root, text="Verify OTP", command=verify_otp)

root.mainloop()