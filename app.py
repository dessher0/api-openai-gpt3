from flask import Flask, render_template, request
import gpt_3
import config


def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found)


@app.route('/', methods=["GET", "POST"])
def index():

    if request.method == 'POST':
        if 'form_1' in request.form:
            input_text = request.form['TextResult']
            response = gpt_3.main(input_text)
            Result = response.replace('\n', '<br>')

    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)