#!/usr/bin/python
from urllib2 import urlopen
from dothat import lcd
from dothat import backlight


#Monitors a VPN connection by checking the public IP and outputs to a Pi HAT display

def main():
	ip = urlopen('http://ip.42.pl/raw').read()
	lcd.clear()
	lcd.set_contrast(50)
	if ip == '#IPADDRESS':
		backlight.rgb(0,255,0)
		lcd.set_cursor_position(0,0); lcd.write("  LINK SECURED")
		lcd.set_cursor_position(0,1); lcd.write(" " + ip)
	else:
		backlight.rgb(255,0,0)
		lcd.set_cursor_position(0,0); lcd.write(" LINK UNSECURED")
		lcd.set_cursor_position(0,1); lcd.write(" " + ip)


if __name__ == "__main__":
	main()
