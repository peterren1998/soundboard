from flask import Flask, render_template, request, make_response, redirect, json
app = Flask(__name__)

home = "http://127.0.0.1:5000/"

local_buttons = []

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

@app.route("/")
def index():
    return redirect("%sreal.html" % home, code=302)

@app.route('/real.html', methods=["GET","POST"])
def main():

    default = Board("default")
    default.add_button(Button("d1", "fileName1"))
    default.add_button(Button("d2", "fileName2"))
    cur_board = default
    boards = [default]
    buttons = cur_board.buttons
    if request.method == "POST":
        if request.form['board'] and request.form['board'] in [board.name for board in boards]:
            for board in boards:
                if request.form['board'] == board.name:
                    cur_board = board
                    buttons = cur_board.buttons
                return redirect('%sreal.html' % home, code=302)
    buttons_dictionary = {}
    for button in buttons:
        buttons_dictionary[button.name] = button.audio_file
    return render_template("real.html", title = cur_board.name, d = buttons_dictionary)

#@app.route('/buttons/<button_name>.html')
#def play(button_name):
#    for button in buttons:
#        if button.name == button_name:
#            return render_template("real.html", press=button_name)
"""
@app.route('/real2.html')
def set_board():
    return render_template("real2.html", title="my title")
"""
@app.route('/real2.html', methods = ['GET', 'POST'])
def create_board():
    if request.method == "POST" and request.form['bitstring']: #when stop button is pressed
        local_buttons.append(Button(request.form['name'], request.form['bitstring']))
        return redirect("%sreal2.html" % home, code=302)
    elif request.method == "GET": #when submit is clicked
        boards.append(Board(board_name, local_buttons))
        return redirect("%sreal.html" % home, code=302)
    return render_template("real2.html", title = board_name)


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

"""
    def play(self):
"""

"""
def dump_buttons():
    button_dictionary = {}
    for b in buttons:
        button_dictionary[b.name] = b.audio_file
    return json.dumps(button_dictionary)
"""
if __name__ == "__main__":
    app.run()
