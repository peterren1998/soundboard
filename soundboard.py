from flask import Flask, render_template, request, make_response, redirect, json
app = Flask(__name__)

home = "http://127.0.0.1:5000/"

@app.route("/")
def index():
    return redirect("%stest.html" % home, code=302)

@app.route('/test.html', methods=["GET","POST"])
def main():
    if request.method == "POST":
        return redirect("%stest2.html" % home, code=302)
    #set_board("default")
    return render_template("test.html")

@app.route('/test2.html')
def main2():
    return render_template("test2.html")
"""
@app.route('/test/%s/%s.html' % (board_name, button_name))
def play(button_name):
    for button in buttons:
        if button_name == button.name:
            button.play()
"""

@app.route('/test/<board_name>.html')
def set_board(board_name):
    for board in boards:
        if board_name == board.name:
            buttons = board.buttons
    dump_buttons()

#@app.route('/test/create_board')
#def create_board():


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

boards = [default]
buttons = []

def dump_buttons():
    button_dictionary = {}
    for b in buttons:
        button_dictionary[b.name] = b.audio_file
    return json.dumps(button_dictionary)

if __name__ == "__main__":
    app.run()
