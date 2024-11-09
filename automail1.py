import datetime
import os
import yagmail

try:
    # Get today's date
    date = datetime.date.today().strftime("%B %d, %Y")

    # Define the full path of the 'StudentDetails.csv' file
    filename = r"C:\Users\akshi\OneDrive\Desktop\(IOMP)\PresencePro\PresencePro\StudentDetails\StudentDetails.csv"

    # Check if the file exists
    if not os.path.exists(filename):
        print("StudentDetails.csv file not found in the specified directory.")
    else:
        subject = f"Attendance Report for {date}"

        # Set up Yagmail with credentials
        yag = yagmail.SMTP("saibaba12ajk@gmail.com", "uysy ydmm rngc vhhd")

        # Send the email with the 'StudentDetails.csv' file attached
        yag.send(
            to="akshithshanagonda@gmail.com",
            subject=subject,
            contents="Attached is the students' attendance report.",
            attachments=filename,
        )
        print("Email Sent Successfully!")

except FileNotFoundError as fnf_error:
    print(f"Error: {fnf_error}. Please check the directory path.")
except yagmail.error.YagAddressError:
    print("Invalid email address provided.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
