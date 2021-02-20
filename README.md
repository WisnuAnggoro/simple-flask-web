# simple-flask-web
Simple Python Flask Web App

## Running on Local Machine
These're the steps to run this repo on your local machine:
### Clone the repo
Clone this repo to local machine

```bash
git clone https://github.com/WisnuAnggoro/simple-flask-web.git
cd simple-flask-web
```
### Setup environment
Setup virtual environment with Python version is `3.8.2` and environment folder name is `venv`:

```bash
python -m virtualenv venv --python=python3.8.2 
```

**NOTE:** If `virtualenv` is not installed yet, then install it by running the following command:
```bash
python -m pip install virtualenv
```

After environment is set up successfully, `activate` the environment by running this command:

```bash
source venv/bin/activate
```

### Install all dependencies
Run the following command to install dependencies stated in file `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

### Run the web app server
Running the following command to run the web app:

```bash
FLASK_APP=app.py FLASK_ENV=development python -m flask run
```
If the web server is successfully running, we will see a response like this:

```bash
* Serving Flask app "app.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 294-880-215
```
