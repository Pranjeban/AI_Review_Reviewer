# Resume Feedback Web Application

Welcome to our Resume Feedback Web Application! This project empowers users to upload their resumes and receive insightful feedback generated by OpenAI's ChatGPT model. The application integrates FlaskAPI for the backend, HTML/CSS/JavaScript for the frontend, and OpenAI's API for natural language processing.

## Key Features

- Seamless upload of resumes in PDF, DOC, or DOCX formats.
- Actionable feedback on uploaded resumes through ChatGPT.
- Intuitive and user-friendly interface for a smooth experience.

## Project Structure

The project is meticulously organized into the following directories:

- **backend/**: Houses the backend code written in Python using FlaskAPI.
  - `main.py`: Core backend application logic resides here.
  - `requirements.txt`: Lists all the essential Python dependencies required for backend operation.
- **frontend/**: Contains the frontend code crafted in HTML, CSS, and JavaScript.
  - `upload.html`: Primary HTML file defines the structure of the frontend.
  - `feedback.html` : Secondary HTML file that will give feedform
  - `styles.css`: CSS file defines styles and layout for the frontend.
  - `script.js`: JavaScript file adds functionality to the frontend.

## Backend (`main.py`)

The backend is implemented using FlaskAPI, a lightweight Python web framework.

### Endpoints

- **POST /upload/**: Endpoint for uploading resume files and generating ChatGPT-powered feedback.

## Frontend (`upload.html`, `feddback.html`, `styles.css`, `script.js`)

The frontend provides a user-friendly interface for seamless interaction with the application.

### HTML (`upload.html`)

Defines the webpage's structure, including buttons and file input fields.

### HTML (`feedback.html`)

Defines the feedback page structure, incluing the feedback generated by the ChatGPT / OpenAI api

### CSS (`styles.css`)

Defines styles and layout for the frontend, enhancing visual appeal and responsiveness.

### JavaScript (`script.js`)

Injects functionality into the frontend, handling user interaction, making AJAX requests to the backend, and updating the user interface dynamically.

## Configuration

### OpenAI API Key

To integrate with OpenAI's ChatGPT model, replace `'your_openai_api_key'` in `main.py` with your actual OpenAI API key.

## Usage

### Starting the Backend Server

1. Navigate to the backend directory:
   ```bash
   cd backend
2. Initiate the python program
    ```python
    python main.py
3. Then follow open the link

## How to Use:

1. Run python main.py in the backend folder.
2. Open upload.html in your web browser.
3. Click "Upload Resume" and choose your file.
4. See feedback generated by ChatGPT!

## Opening the Frontend

### Launch your web browser.
Navigate to the index.html file within the project directory.
Uploading a Resume File
### Click the "Upload Resume" button.
Select the desired resume file from your system.
### Viewing Feedback
Once the upload process is complete, the application will display the insightful feedback generated by ChatGPT based on your uploaded resume.

