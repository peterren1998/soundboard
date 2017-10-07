from flask import Flask, render_template, request, make_response, redirect
import api
app = Flask(__name__)

home = "http://127.0.0.1:5000/"

@app.route("/")
def index():
    return redirect("%smainpage.html" % home, code=302)

default = Package("default")
default.addButton(Button("d1", fileName1)
default.addButton(Button("d2"), fileName2)

packages = [default]
buttons =

@app.route('/url.html')
def main():
    setPackage("default")

def setPackage(packageName):
    for package in packages:
        if packageName == package.name:


class Package:

    def __init__(self, name):
        self.name = name
        self.buttons = []
        self.button_dictionary =

    def setName(self, name):
        self.name = name

    def addButton(self, button):
        self.buttons.add(button)

    def changeButton(self, name, newButton):
        for button in self.buttons:
            if button.name == name:
                button = newButton

class Button:

    def __init__(self, name, audioFile):
        self.name = name
        self.audioFile = audioFile

    def play(self):
        #play self.audioFile

@app.route('/url/<button_name>.html')
def play(button_name):
