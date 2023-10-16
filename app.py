from bottle import Bottle, run, request, template

app = Bottle()


data = []


@app.route('/add', method='POST')
def add_item():
    name = request.forms.get('name')
    data.append(name)
    return "Item added: " + name


@app.route('/')
def display_items():
    return template('items', items=data)


@app.route('/edit/<index:int>', method='GET')
def edit_item(index):
    if index < len(data):
        return template('edit_item', index=index, item=data[index])
    else:
        return "Item not found"

@app.route('/edit/<index:int>', method='POST')
def do_edit_item(index):
    if index < len(data):
        new_name = request.forms.get('name')
        data[index] = new_name
        return "Item edited: " + new_name
    else:
        return "Item not found"

@app.route('/delete/<index:int>')
def delete_item(index):
    if index < len(data):
        deleted_item = data.pop(index)
        return "Item deleted: " + deleted_item
    else:
        return "Item not found"

if __name__ == '__main__':
    run(app, host='localhost', port=8000)
