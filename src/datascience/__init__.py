# os module import kar rahe hain taake files aur directories ke sath kaam kar saken
import os

# sys module import karte hain taake system-level streams (jaise stdout) use kar saken
import sys

# logging module import kar rahe hain taake project ke andar proper log messages likh saken
import logging


# ---------------------------------------------
# 1️⃣ Ye format define karta hai ke log ka message kaisa dikhai dega
# "%(asctime)s" -> ye current time show karega jab log likha gaya
# "%(levelname)s" -> ye batayega ke log kis level ka hai (INFO, WARNING, ERROR)
# "%(module)s" -> ye batayega ke kis Python module (file) se log aaya hai
# "%(message)s" -> ye actual message hai jo hum print karte hain
# ---------------------------------------------
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"


# ---------------------------------------------
# 2️⃣ "log_dir" variable me folder ka naam define kar rahe hain jahan logs store honge
# "logs" naam ka folder banaya jayega agar pehle nahi bana
# ---------------------------------------------
log_dir = "logs"

# log file ka poora path bana rahe hain (logs/logging.log)
log_filepath = os.path.join(log_dir, "logging.log")

# agar logs folder exist nahi karta to bana do
os.makedirs(log_dir, exist_ok=True)


# ---------------------------------------------
# 3️⃣ Logging configuration setup kar rahe hain
# ---------------------------------------------
logging.basicConfig(
    # Logging level INFO rakha gaya hai (matlab normal information, warnings, errors sab log honge)
    level=logging.INFO,

    # Format humne upar define kiya (timestamp, level, module, message)
    format=logging_str,

    # Handlers batate hain ke logs kahan likhe jayenge
    handlers=[
        # FileHandler -> logs ko ek file me save karega (logging.log)
        logging.FileHandler(log_filepath),

        # StreamHandler -> logs ko terminal (console) par bhi show karega
        logging.StreamHandler(sys.stdout)
    ]
)


# ---------------------------------------------
# 4️⃣ Ab ek logger object bana rahe hain jiska naam "datasciencelogger" rakha gaya hai
# Ye object poore project me import karke use kiya jayega logs likhne ke liye
# ---------------------------------------------
logger = logging.getLogger("datasciencelogger")
