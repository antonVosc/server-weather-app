# How to run server-weather-app

This is a server side. You will also need a client side (https://github.com/antonVosc/client-weather-app)

STEP 1: Download the repo:
```
git clone https://github.com/antonVosc/server-weather-app.git
```

STEP 2: Navigate to server-weather-app directory:
```
cd server-weather-app
```

STEP 3: Create the virtual environment:
```
python3 -m venv venv
```

STEP 4: Activate the virtual environment:
```
. venv/bin/activate
```

STEP 5: Install the required libraries:
```
pip install -r requirements.txt
```

STEP 6: To run the program:
```
python main.py
```

NOTE: If you want to run the app remotely, look into uvicorn