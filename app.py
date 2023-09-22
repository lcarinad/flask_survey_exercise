from flask import Flask, request, render_template
from surveys import satisfaction_survey
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "shh-its-a-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']= True

debug = DebugToolbarExtension(app)

response = []


@app.route('/')
def home():
    survey_title = satisfaction_survey.title
    survey_instructions = satisfaction_survey.instructions
    
    return render_template("home.html", survey_title=survey_title, survey_instructions=survey_instructions)


@app.route('/<survey_questions>/<int:idx>')
def display_questions(survey_questions, idx):
    
    survey_questions=satisfaction_survey.questions[idx].question
    survey_choices=satisfaction_survey.questions[idx].choices

        
    return render_template("questions.html", survey_questions=survey_questions, survey_choices=survey_choices)

@app.route('/answer', methods=["POST"])
def handle_answer():

    usr_response = request.form['response']
    response.append(usr_response)
    return "<h1>Thank you for answerin</h1>"