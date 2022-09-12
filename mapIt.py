# my middle school: 中卫市兴仁中学/@36.938018,105.2579519,17.25z/data=!4m5!3m4!1s0x3643770f7e19b58d:0x49f0024dfdb8e1da!8m2!3d36.936508!4d105.254548
# using address from the command line or clipboard.
import webbrowser,sys,pyperclip
if len(sys.argv)>1:
	# get address from command line
	address = ' '.join(sts.argv[1:])
else:
	# get address from clipboard.
	address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/'+address)
