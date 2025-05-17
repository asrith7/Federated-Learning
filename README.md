Terminal- 1:
    Run the following comands in one terminal on VS Code.
        1) run python -m venv venv
        2) venv\Scripts\activate
        3) pip install -r requirements.txt

Terminal- 2:
    Run the following comands in second terminal on VS Code.
        1) uvicorn main:app --reload

Terminal- 3:
    Run the following comands in third terminal on VS Code.
        1) python -m http.server 8001

Note run all the terminals in parallel