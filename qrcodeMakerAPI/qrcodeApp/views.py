from django.http import HttpResponse
from django.shortcuts import render
import qrcode



# Create your views here.

# Global variables
path = "/Users/emmanuelkwakyenyantakyi/Desktop/cs/Python_files/Django_Projects/qrcodeMakerAPI/qrcodeApp/static/"

# Function to make qrcode from url
def makeCode(url):
    image = qrcode.make(url)
    name = "m.jpg"
    image.save(path + name)

# Function to send code to user
def get_code (request, URL):
    if request.method == 'GET':
        makeCode(URL)

    return render(request, 'image.html')
      

# this is the youtube url http://youtu.be/xvFZjo5PgG0 we're gonna test our program with