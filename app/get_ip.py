import smtplib
import socket 
import io
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


MY_ADDRESS = 'framboisepi01@gmail.com'
PASSWORD = ''


def get_ip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	ip = s.getsockname()[0]
	print("My IP address is: " + ip)
	s.close()
	return ip


def send_mail(message):
	# Open connection
	s = smtplib.SMTP(host='smtp.gmail.com', port=587)
	s.starttls()
	s.login(MY_ADDRESS, PASSWORD)
	# create a message
	msg = MIMEMultipart()
	# Get the message template
	message_template = read_template('/home/pi/webapp/app/infos/message.txt')
	# add in the ip address to the message template
	message = message_template.substitute(IP=message)
	# setup the parameters of the message
	msg['From']=MY_ADDRESS
	msg['To']=MY_ADDRESS
	msg['Subject']="IP Address"
	# add in the message body
	msg.attach(MIMEText(message, 'plain'))
	# send the message via the server set up earlier.
	s.send_message(msg)
	del msg
	# Terminate the SMTP session and close the connection
	s.quit()


def get_password(path_to_file):
	global PASSWORD
	with io.open(path_to_file, 'r', encoding='utf-8') as password_txt:
		PASSWORD = password_txt.read()


# Open the template for the mail content
def read_template(filename):
	with io.open(filename, 'r', encoding='utf-8') as template_file:
		template_file_content = template_file.read()
	return Template(template_file_content)


def main():
	print("Sending IP Address ")
	get_password("/home/pi/Documents/App/password.txt")
	ip = get_ip()
	send_mail(ip)


if __name__ == "__main__":
	# execute only if run as a script
	main()
