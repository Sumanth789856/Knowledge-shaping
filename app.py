from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    last_result = session.get('last_result', {})
    return render_template('dashboard.html', result=last_result)

@app.route('/alphabet', methods=['GET', 'POST'])
def alphabet_test():
    if request.method == 'POST':
        marks = int(request.form['marks'])
        questions = []
        for _ in range(marks):
            r = random.randint(65, 90)
            questions.append({'char': chr(r), 'code': r})
        session['alphabet'] = questions
        return render_template('alphabet.html', questions=questions)
    return render_template('alphabet_start.html')

@app.route('/alphabet/submit', methods=['POST'])
def alphabet_submit():
    questions = session.get('alphabet', [])
    correct = 0
    wrong = 0
    missed = {}

    for i, q in enumerate(questions):
        user_input = int(request.form.get(f'ans{i}', 0))
        correct_number = ord(q['char']) - 64  # A=1, B=2, ..., Z=26

        if user_input == correct_number:
            correct += 1
        else:
            wrong += 1
            missed[q['char']] = correct_number
                
            

    percent = int((correct / len(questions)) * 100)

    return render_template('result.html', correct=correct, wrong=wrong, percent=percent, missed=missed, test="Alphabet Numbering Test")

@app.route('/squares', methods=['GET', 'POST'])
def squares_test():
    if request.method == 'POST':
        ks = int(request.form['ks'])
        marks = int(request.form['marks'])
        questions = [{'num': r, 'ans': r*r} for r in [random.randint(1, ks) for _ in range(marks)]]
        session['squares'] = questions
        return render_template('squares.html', questions=questions)
    return render_template('squares_start.html')

@app.route('/squares/submit', methods=['POST'])
def squares_submit():
    questions = session.get('squares', [])
    correct, wrong, missed = 0, 0, {}
    for i, q in enumerate(questions):
        user = int(request.form.get(f'ans{i}', 0))
        if user == q['ans']:
            correct += 1
        else:
            wrong += 1
            missed[q['num']] = q['ans']
    percent = int((correct / len(questions)) * 100)
    session['last_result'] = {
        'test': "Squares Test",
        'correct': correct,
        'wrong': wrong,
        'percent': percent,
        'missed': missed
    }
    return render_template('result.html', correct=correct, wrong=wrong, percent=percent, missed=missed, test="Squares Test")

@app.route('/cubes', methods=['GET', 'POST'])
def cubes_test():
    if request.method == 'POST':
        ks = int(request.form['ks'])
        marks = int(request.form['marks'])
        questions = [{'num': r, 'ans': r*r*r} for r in [random.randint(1, ks) for _ in range(marks)]]
        session['cubes'] = questions
        return render_template('cubes.html', questions=questions)
    return render_template('cubes_start.html')

@app.route('/cubes/submit', methods=['POST'])
def cubes_submit():
    questions = session.get('cubes', [])
    correct, wrong, missed = 0, 0, {}
    for i, q in enumerate(questions):
        user = int(request.form.get(f'ans{i}', 0))
        if user == q['ans']:
            correct += 1
        else:
            wrong += 1
            missed[q['num']] = q['ans']
    percent = int((correct / len(questions)) * 100)
    session['last_result'] = {
        'test': "Cubes Test",
        'correct': correct,
        'wrong': wrong,
        'percent': percent,
        'missed': missed
    }
    return render_template('result.html', correct=correct, wrong=wrong, percent=percent, missed=missed, test="Cubes Test")

if __name__ == '__main__':
    app.run(debug=True)
