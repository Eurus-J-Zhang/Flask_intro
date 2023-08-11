from flask import Flask,render_template,url_for,request, redirect, send_from_directory, session
from flask_migrate import Migrate
from forms import EmotionForm1
from forms import EmotionForm2
from forms import EmotionForm3
from forms import EmotionForm4
from forms import FeedbackForm
from forms import DemographicInfo
import os
import pymysql
from models import db, Data

pymysql.install_as_MySQLdb()

# Here is about configuration


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('JAWSDB_URL') 
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SECRET_KEY'] = "iloveeurus"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app

app = create_app()

def handle_form_submission(form, session_key, next_page):
    if form.validate_on_submit():
        data = form.data
        data.pop('csrf_token', None)
        session[session_key] = data
        return redirect(next_page)
    return None


@app.route('/', methods=['GET', 'POST'])
def index():
    form = DemographicInfo()
    result = handle_form_submission(form, 'index_data', 'emo1')
    if result:
        return result
    return render_template('index.html',form=form)

@app.route('/emo1', methods=['GET', 'POST'])
def emo1():
    form = EmotionForm1()
    result = handle_form_submission(form, 'emo1_data', 'q1')
    if result:
        return result
    return render_template('emo1.html',form=form)


@app.route('/emo2', methods=['GET', 'POST'])
def emo2():
    form = EmotionForm2()
    result = handle_form_submission(form, 'emo2_data', 'q12')
    if result:
        return result
    return render_template('emo2.html',form=form)

@app.route('/emo3', methods=['GET', 'POST'])
def emo3():
    form = EmotionForm3()
    result = handle_form_submission(form, 'emo3_data', 'q23')
    if result:
        return result
    return render_template('emo3.html',form=form)


@app.route('/emo4', methods=['GET', 'POST'])
def emo4():
    form = EmotionForm4()
    result = handle_form_submission(form, 'emo4_data', 'emo_end')
    if result:
        return result
    return render_template('emo4.html',form=form)

@app.route('/emo_end', methods=['GET', 'POST'])
def emo_end():
    form = FeedbackForm()
    result = handle_form_submission(form, 'emo_add_data', 'page_end')
    if result:
        index_data = session.get('index_data')
        emo1_data = session.get('emo1_data')
        emo2_data = session.get('emo2_data')
        emo3_data = session.get('emo3_data')
        emo4_data = session.get('emo4_data')
        emo_add_data = session.get('emo_add_data')
        
        combined_data = {**index_data, **emo1_data, **emo2_data, **emo3_data, **emo4_data, **emo_add_data}
        data = Data(**combined_data)
        db.session.add(data)
        db.session.commit()

        return result
    return render_template('emo_end.html',form=form)

def question_route(question_num, correct_answer, template_name):
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == correct_answer:
            result = 'correct'
        else:
            result = 'wrong'
        return render_template(template_name + 'r.html', result=result, answer=answer)
    return render_template(template_name + '.html')

# Q1
@app.route('/q1', methods=['GET', 'POST'])
def q1():
    return question_route(1, 'A', 'q1')

@app.route('/q1r')
def q1r():
    return render_template('q1r.html')

# Q2
@app.route('/q2', methods=['GET', 'POST'])
def q2():
    return question_route(2, 'A', 'q2')

@app.route('/q2r')
def q2r():
    return render_template('q2r.html')

# Q3
@app.route('/q3', methods=['GET', 'POST'])
def q3():
    return question_route(3, 'B', 'q3')

@app.route('/q3r')
def q3r():
    return render_template('q3r.html')

# Q4
@app.route('/q4', methods=['GET', 'POST'])
def q4():
    return question_route(4, 'A', 'q4')

@app.route('/q4r')
def q4r():
    return render_template('q4r.html')

# Q5
@app.route('/q5', methods=['GET', 'POST'])
def q5():
    return question_route(5, 'B', 'q5')

@app.route('/q5r')
def q5r():
    return render_template('q5r.html')

# Q6
@app.route('/q6', methods=['GET', 'POST'])
def q6():
    return question_route(6, 'B', 'q6')

@app.route('/q6r')
def q6r():
    return render_template('q6r.html')

# Q7
@app.route('/q7', methods=['GET', 'POST'])
def q7():
    return question_route(7, 'A', 'q7')

@app.route('/q7r')
def q7r():
    return render_template('q7r.html')

# Q8
@app.route('/q8', methods=['GET', 'POST'])
def q8():
    return question_route(8, 'B', 'q8')

@app.route('/q8r')
def q8r():
    return render_template('q8r.html')

# Q9
@app.route('/q9', methods=['GET', 'POST'])
def q9():
    return question_route(9, 'A', 'q9')

@app.route('/q9r')
def q9r():
    return render_template('q9r.html')

# Q10
@app.route('/q10', methods=['GET', 'POST'])
def q10():
    return question_route(10, 'B', 'q10')

@app.route('/q10r')
def q10r():
    return render_template('q10r.html')

# Q11
@app.route('/q11', methods=['GET', 'POST'])
def q11():
    return question_route(11, 'A', 'q11')

@app.route('/q11r')
def q11r():
    return render_template('q11r.html')

# Q12
@app.route('/q12', methods=['GET', 'POST'])
def q12():
    return question_route(12, 'A', 'q12')

@app.route('/q12r')
def q12r():
    return render_template('q12r.html')

# Q13
@app.route('/q13', methods=['GET', 'POST'])
def q13():
    return question_route(13, 'B', 'q13')

@app.route('/q13r')
def q13r():
    return render_template('q13r.html')

# Q14
@app.route('/q14', methods=['GET', 'POST'])
def q14():
    return question_route(14, 'A', 'q14')

@app.route('/q14r')
def q14r():
    return render_template('q14r.html')

# Q15
@app.route('/q15', methods=['GET', 'POST'])
def q15():
    return question_route(15, 'B', 'q15')

@app.route('/q15r')
def q15r():
    return render_template('q15r.html')

# Q16
@app.route('/q16', methods=['GET', 'POST'])
def q16():
    return question_route(16, 'B', 'q16')

@app.route('/q16r')
def q16r():
    return render_template('q16r.html')

# Q17
@app.route('/q17', methods=['GET', 'POST'])
def q17():
    return question_route(17, 'B', 'q17')

@app.route('/q17r')
def q17r():
    return render_template('q17r.html')

# Q18
@app.route('/q18', methods=['GET', 'POST'])
def q18():
    return question_route(18, 'B', 'q18')

@app.route('/q18r')
def q18r():
    return render_template('q18r.html')

# Q19
@app.route('/q19', methods=['GET', 'POST'])
def q19():
    return question_route(19, 'A', 'q19')

@app.route('/q19r')
def q19r():
    return render_template('q19r.html')

# Q20
@app.route('/q20', methods=['GET', 'POST'])
def q20():
    return question_route(20, 'B', 'q20')

@app.route('/q20r')
def q20r():
    return render_template('q20r.html')

# Q21
@app.route('/q21', methods=['GET', 'POST'])
def q21():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'B':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q21r.html', result=result, answer=answer)
    return render_template('q21.html')

@app.route('/q21r')
def q21r():
    return render_template('q21r.html')

# Q22
@app.route('/q22', methods=['GET', 'POST'])
def q22():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'A':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q22r.html', result=result, answer=answer)
    return render_template('q22.html')

@app.route('/q22r')
def q22r():
    return render_template('q22r.html')

# Q23
@app.route('/q23', methods=['GET', 'POST'])
def q23():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'A':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q23r.html', result=result, answer=answer)
    return render_template('q23.html')

@app.route('/q23r')
def q23r():
    return render_template('q23r.html')

# Q24
@app.route('/q24', methods=['GET', 'POST'])
def q24():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'A':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q24r.html', result=result, answer=answer)
    return render_template('q24.html')

@app.route('/q24r')
def q24r():
    return render_template('q24r.html')

# Q25
@app.route('/q25', methods=['GET', 'POST'])
def q25():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'A':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q25r.html', result=result, answer=answer)
    return render_template('q25.html')

@app.route('/q25r')
def q25r():
    return render_template('q25r.html')

# Q26
@app.route('/q26', methods=['GET', 'POST'])
def q26():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'A':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q26r.html', result=result, answer=answer)
    return render_template('q26.html')

@app.route('/q26r')
def q26r():
    return render_template('q26r.html')

# Q27
@app.route('/q27', methods=['GET', 'POST'])
def q27():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'A':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q27r.html', result=result, answer=answer)
    return render_template('q27.html')

@app.route('/q27r')
def q27r():
    return render_template('q27r.html')

# Q28
@app.route('/q28', methods=['GET', 'POST'])
def q28():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'B':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q28r.html', result=result, answer=answer)
    return render_template('q28.html')

@app.route('/q28r')
def q28r():
    return render_template('q28r.html')

# Q29
@app.route('/q29', methods=['GET', 'POST'])
def q29():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'B':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q29r.html', result=result, answer=answer)
    return render_template('q29.html')

@app.route('/q29r')
def q29r():
    return render_template('q29r.html')

# Q30
@app.route('/q30', methods=['GET', 'POST'])
def q30():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'A':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q30r.html', result=result, answer=answer)
    return render_template('q30.html')

@app.route('/q30r')
def q30r():
    return render_template('q30r.html')

# Q31
@app.route('/q31', methods=['GET', 'POST'])
def q31():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'B':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q31r.html', result=result, answer=answer)
    return render_template('q31.html')

@app.route('/q31r')
def q31r():
    return render_template('q31r.html')

# Q32
@app.route('/q32', methods=['GET', 'POST'])
def q32():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'A':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q32r.html', result=result, answer=answer)
    return render_template('q32.html')

@app.route('/q32r')
def q32r():
    return render_template('q32r.html')

# Q33
@app.route('/q33', methods=['GET', 'POST'])
def q33():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'B':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q33r.html', result=result, answer=answer)
    return render_template('q33.html')

@app.route('/q33r')
def q33r():
    return render_template('q33r.html')

# Q34
@app.route('/q34', methods=['GET', 'POST'])
def q34():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'B':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q34r.html', result=result, answer=answer)
    return render_template('q34.html')

@app.route('/q34r')
def q34r():
    return render_template('q34r.html')


@app.route('/page_end')
def page_end():
    return render_template('page_end.html')


if __name__ == "__main__":
    app.run(debug=True)
    