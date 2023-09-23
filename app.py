from flask import Flask, request, render_template, redirect, flash
from surveys import satisfaction_survey
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "shh-its-a-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']= False

debug = DebugToolbarExtension(app)

responses = []




@app.route('/')
def home():

    survey_title = satisfaction_survey.title
    survey_instructions = satisfaction_survey.instructions
    
    return render_template("home.html", survey_title=survey_title, survey_instructions=survey_instructions)


@app.route('/<survey_questions>/<int:idx>')
def display_questions(survey_questions, idx):
    try:
        survey_questions=satisfaction_survey.questions[idx].question
        survey_choices=satisfaction_survey.questions[idx].choices
        return render_template("questions.html",survey_questions=survey_questions, survey_choices=survey_choices)
    except IndexError:
        return redirect(f"/")
    

@app.route('/answer', methods=["POST"])
def handle_answer():

    survey_questions=satisfaction_survey.questions
    usr_responses = request.form['response']
    responses.append(usr_responses)
    next_question_idx=len(responses)   

    if len(responses) == len(satisfaction_survey.questions):
        return render_template("confirmation.html")
    elif len(responses) < len(satisfaction_survey.questions):
        return redirect(f"/questions/{next_question_idx}")
