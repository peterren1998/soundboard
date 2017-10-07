from flask import Flask, render_template, request, make_response, redirect, json
app = Flask(__name__, static_folder='templates')

home = "http://127.0.0.1:5000/"

@app.route("/")
def index():
    return redirect("%stest.html" % home, code=302)

@app.route('/test.html')
def main():
    set_package("default")
    return render_template("test.html")
"""
@app.route('/test/%s/%s.html' % (package_name, button_name))
def play(button_name):
    for button in buttons:
        if button_name == button.name:
            button.play()
"""
@app.route('/test/<package_name>.html')
def set_package(package_name):
    for package in packages:
        if package_name == package.name:
            buttons = package.buttons
    dump_buttons()

#@app.route('/test/create_package')
#def create_package():


class Package:

    def __init__(self, name):
        self.name = name
        self.buttons = []

    def set_name(self, name):
        self.name = name

    def add_button(self, button):
        self.buttons.append(button)

    def change_button(self, name, new_button):
        for button in self.buttons:
            if button.name == name:
                button = new_button

class Button:

    def __init__(self, name, audio_file):
        self.name = name
        self.audio_file = audio_file

    #def play(self):
        #play self.audioFile

default = Package("default")
default.add_button(Button("d1", "fileName1"))
default.add_button(Button("d2", "fileName2"))

packages = [default]
buttons = []

def dump_buttons():
    button_dictionary = {}
    for b in buttons:
        button_dictionary[b.name] = b.audio_file
    return json.dumps(button_dictionary)

if __name__ == "__main__":
    app.run()
