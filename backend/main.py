import openai
import docx2txt
import os
from flask import Flask, render_template, request
from PyPDF2 import PdfReader

app = Flask(__name__,template_folder="frontend")

openai.api_key = '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'

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('upload.html')

def extract_text_from_docx(file_path):
    return docx2txt.process(file_path)

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text

@app.route('/upload', methods=['POST'])
def upload():
    if 'resume' not in request.files:
        return 'No file part'

    resume_file = request.files['resume']

    if resume_file.filename == '':
        return 'No selected file'
    resume_path = os.path.join(UPLOAD_FOLDER, resume_file.filename)
    resume_file.save(resume_path)
    try:
        if resume_path.endswith('.docx'):
            resume_text = extract_text_from_docx(resume_path)
        elif resume_path.endswith('.pdf'):
            resume_text = extract_text_from_pdf(resume_path)
        else:
            return 'Unsupported file format'
    except Exception as e:
        return f'Error processing resume file: {str(e)}'

    try:
        prompt_text = f"Feedback on resume:\n{resume_text}\n\nPlease provide constructive feedback on the applicant's resume. Highlight strengths, areas of improvement, and any specific recommendations for enhancing the overall presentation and content.\n###\n"
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt_text,
            max_tokens=300,
        )
        feedback = response.choices[0].text.strip()
    except Exception as e:
        return f'Error generating feedback: {str(e)}'

    return render_template('feedback.html', feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)
