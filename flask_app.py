from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    name = request.form.get('input_name', '')
    dropdown = request.form.get('input_dropdown', '')
    select = request.form.get('input_select', '')
    freeform = request.form.get('input_freeform', '')
    return render_template("main_page.html", input_data=dropdown,
                            output="You're a wizard %s." % name,
                            animals=dedupe(animals))


def dedupe(x): # (x is the list)
    y = []
    for animal in x:
        if animal not in y:
            y+=animal
        # add it
    return y

    # make a new list called deduped_list
    # search for a duplicate
    # for each element in x
    # add item if it is no on a new list

animals = ['cats', 'cats', 'cats', 'dogs', 'pandas']
print(dedupe(animals)) # prints ['cats', 'dogs', 'pandas']

