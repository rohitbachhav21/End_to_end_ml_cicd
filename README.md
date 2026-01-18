📌 Project Setup and Workflow

This project follows a modular, production-style structure for building, training, and deploying a Machine Learning model with a Flask web interface.

1️⃣ Project Initialization

Create a new project folder and open it in VS Code.

Open the integrated terminal.

Create a virtual environment:

python -m venv venv


Activate the virtual environment:

venv\Scripts\activate


After activation, the terminal will show:

(venv) PS D:\ML Generic


A venv/ folder is created with the required environment structure.

2️⃣ Version Control Setup

While pushing code to GitHub:

The venv/ folder is not pushed

Only README.md and .gitignore are tracked

Ensure venv/ is added to .gitignore.

3️⃣ Project Structure Setup

Create setup.py outside the venv/ folder

Used to build the project as a Python package

Create requirements.txt outside venv/

Contains all required dependencies

Create a src/ directory outside venv/

Entire project development happens inside src/

Inside setup.py, define get_requirements()

Used to read dependencies from requirements.txt

Install dependencies:

pip install -r requirements.txt

4️⃣ Core Utilities

Create:

logging.py → central logging configuration

exception.py → custom exception handling

5️⃣ Notebook Workflow

Create a notebook/ folder outside src/

The notebook folder contains:

Raw dataset

Jupyter notebooks (.ipynb)

Notebook 1:

Data cleaning

Exploratory Data Analysis (EDA)

Notebook 2:

Model creation

Training and testing experiments

6️⃣ Data Ingestion & Artifacts

Create src/components/data_ingestion.py

Running this creates an artifacts/ folder outside src/

Stores:

data.csv

train.csv

test.csv

A logs/ folder (outside src/) tracks:

Execution history

Pipeline progress

Automation logs

7️⃣ Data Transformation

Create src/components/data_transformation.py

Handles preprocessing

Generates preprocessor.pkl inside artifacts/

8️⃣ Pipeline Execution

Run data ingestion as an entry point:

python -m src.components.data_ingestion

9️⃣ Model Training

Create src/components/model_trainer.py

Trains multiple models

Selects the best-performing model

Saves model.pkl inside artifacts/

🔟 Prediction & Deployment

application.py

Flask web application

Serves the HTML interface

src/components/predict_pipeline.py

Handles final predictions from user input

templates/home.html

Web form to collect user input

Sends data to Flask app

Displays predicted Maths score

🚀 Deployment

The project is designed for deployment on AWS Elastic Beanstalk

Tailwind CSS is used inline via CDN

No Node.js or external CSS build steps required

Fully compatible with virtual environments
