from flask import Flask, render_template, request, make_response, redirect, json
app = Flask(__name__)

home = "http://127.0.0.1:5000/"

local_buttons = []

@app.route("/")
def index():
    return redirect("%sreal.html" % home, code=302)

@app.route('/real.html', methods=["GET","POST"])
def main():
    if request.method == "POST" and request.form["change"] == "submit":
        return redirect("%stest2.html" % home, code=302)

    return render_template("real.html", title="title_board", data=[{"name": "1"},{"name": "2"},{"name": "3"},{"name": "4"},{"name": "5"},{"name": "6"},{"name": "7"},{"name": "8"}])

@app.route('/test2.html')
def main2():
    return render_template("test2.html")

@app.route('/test3.html')
def main3():
    return render_template("test3.html")

def play(button_name):
    for button in buttons:
        if button_name == button.name:
            json.dumps(button.audio_file)
            return make_response(data, 200)

@app.route('/test/<board_name>.html')
def set_board(board_name):
    for board in boards:
        if board_name == board.name:
            buttons = board.buttons
    return dump_buttons()

@app.route('/create_board.html', methods = ['GET', 'POST'])
def create_board():
    if request.method == "POST" and request.name == "Stop":
        local_buttons.append(Button(request.form['name'], request.form['bitstring']))
    elif request.method == "POST" and request.name == "Submit":
        boards.append(Board(request.form['board_name'], local_buttons))


"""
@app.route('/create_board', methods = ['GET', 'POST'])
def save_audio():
    if request.method == 'POST':
        local_buttons.append(Button(request.form['name'], request.form['bitstring']))
"""
"""
@app.route('/create_board/save_package', methods = ['GET', 'POST'])
def save_board():
    if request.method == 'POST':
        boards.append(Board(request.form['name'], local_buttons))
"""
class Board:

    def __init__(self, name):
        self.name = name
        self.buttons = []

    def __init__(self, name, buttons):
        self.name = name
        self.buttons = local_buttons
        local_buttons = []

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
"""
    def play(self):

default = Package("default")
default.add_button(Button("d1", "fileName1"))
default.add_button(Button("d2", "fileName2"))
boards = [default]
buttons = []
"""
def dump_buttons():
    button_dictionary = {}
    for b in buttons:
        button_dictionary[b.name] = b.audio_file
    return json.dumps(button_dictionary)

if __name__ == "__main__":
    app.run()
