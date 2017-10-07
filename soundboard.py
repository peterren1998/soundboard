from flask import Flask, render_template, request, make_response, redirect
app = Flask(__name__, static_folder='templates')

home = "http://127.0.0.1:5000/"

@app.route("/")
def index():
    return redirect("%stest.html" % home, code=302)

@app.route('/test')
def main():
    setPackage("default")
    return render_template("test.html")

@app.route('/test/%s/%s' % (package_name, button_name))
def play(button_name):
    for button in buttons:
        if button_name == button.name:
            button.play()

@app.route('/test/<package_name>')
def setPackage(package_name):
    for package in packages:
        if packageName == package.name:
            buttons = package.buttons

class Package:

    def __init__(self, name):
        self.name = name
        self.buttons = []

    def setName(self, name):
        self.name = name

    def addButton(self, button):
        self.buttons.append(button)

    def changeButton(self, name, newButton):
        for button in self.buttons:
            if button.name == name:
                button = newButton

class Button:

    def __init__(self, name, audioFile):
        self.name = name
        self.audioFile = audioFile

    #def play(self):
        #play self.audioFile

default = Package("default")
default.addButton(Button("d1", "fileName1"))
default.addButton(Button("d2", "fileName2"))

packages = [default]
buttons = []

if __name__ == "__main__":
    app.run()
