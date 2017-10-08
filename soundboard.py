from flask import Flask, render_template, request, make_response, redirect, json
app = Flask(__name__)

home = "http://127.0.0.1:5000/"

local_buttons = []

@app.route("/")
def index():
    return redirect("%stest.html" % home, code=302)

@app.route('/test.html', methods=["GET","POST"])
def main():
    if request.method == "POST":
        if request.form['change'] and request.form['change'] in boards.keys():
            return redirect("%s"+request.form['change'] % home)
        else:
            return redirect("%screate_board.html" % home, code=302)
    return set_board("default")

@app.route('/test2.html')
def main2():
    return render_template("test2.html")

@app.route('/buttons/<button_name>.html')
def play(button_name):
    for button in buttons:
        if button.name == button_name:
            return render_template("real.html", press=button_name)

@app.route('/test/<board_name>.html')
def set_board(board_name):
    for board in boards:
        if board_name == board.name:
            buttons = board.buttons
    return render_template("test.html", json = dump_buttons(), title = board_name, data = [{board.name : board} for board in boards])

@app.route('/create_board.html', methods = ['GET', 'POST'])
def create_board():
    if request.method == "POST" and request.name == "Stop":
        local_buttons.append(Button(request.form['name'], request.form['bitstring']))
        return redirect("%screate_board.html" % home, code=302)
    elif request.method == "POST" and request.name == "Submit":
        boards.append(Board(request.form['board_name'], local_buttons))
        return redirect("%stest.html" % home, code=302)


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

    def __init__(self, name, buttons = local_buttons):
        self.name = name
        self.buttons = buttons
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
"""


default = Board("default")
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
