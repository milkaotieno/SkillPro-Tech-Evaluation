# SkillPro-Tech-Evaluation
 SkillPro Tech Evaluation is a structured assessment designed to test problem-solving, software engineering, API development, and deployment skills. It includes coding challenges, API implementation, testing, and system deployment to validate technical expertise.

##Overview

 SkillPro Tech Evaluation is a FastAPI-based application designed for technical evaluations and API testing.

##Features

    -FastAPI backend

    -RESTful API endpoints

    -Automated testing with pytest

    -Docker support (optional)

##Prerequisites

 Ensure you have the following installed:

    -Python 3.10+

    -Git

    -Virtual environment (venv or equivalent)

    -FastAPI, Uvicorn, and dependencies (from requirements.txt)

##Setup

 1. Clone the Repository

     git clone https://github.com/milkaotieno/SkillPro-Tech-Evaluation.git
     cd SkillPro-Tech-Evaluation

 2. Create and Activate a Virtual Environment

    python -m venv venv  # Create virtual environment
    venv\Scripts\activate  # Windows
 3. Install Dependencies
    pip install -r requirements.txt

##Running the Application

 1. Start the FastAPI Server

    uvicorn main:app --reload

 2. Access the API Documentation

    Swagger UI: http://127.0.0.1:8000/docs

    ReDoc: http://127.0.0.1:8000/redoc

##Running Tests

To run unit tests using pytest, execute:

    python pytest

##Git Configuration & Authentication

If you need to switch GitHub users or reauthenticate:

 1. Remove Stored Credentials (Windows Credential Manager)

    Open Control Panel → User Accounts → Credential Manager

    Remove any stored GitHub credentials

 2. Update Git User Info

    git config --global user.name "milkaotieno"
    git config --global user.email "your-email@example.com"

 3. Change Remote URL to Authenticate as Correct User

   Using HTTPS:

    git remote set-url origin https://milkaotieno@github.com/milkaotieno/SkillPro-Tech-Evaluation.git

   Using SSH (Recommended):

    git remote set-url origin git@github.com:milkaotieno/SkillPro-Tech-Evaluation.git

 4. Push Changes to GitHub

    git push -u origin main

##Contributing

 1. Fork the repository

 2. Create a new feature branch (git checkout -b feature-name)

 3. Commit your changes (git commit -m "Description of changes")

 4. Push to your branch (git push origin feature-name)

 5. Open a pull request

##License

 This project is licensed under the MIT License.
