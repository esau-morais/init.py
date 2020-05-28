import pyqrcode

input_url = input('Enter the URL: ')
url = pyqrcode.create (input_url)
input_name = input('Enter file name: ')
url.png(input_name, scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
