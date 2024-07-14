# Mock Anomal Detection System
This code contains code for a mock anomaly detection system in a hostpital setting. I wrote this code during my IT at RAIN for my 200lvl SIWES program.

This code was written to mimic an ideal anomaly detection system in a hospital system. The goal was to use this web app to present the idea of an anomaly system to other staff and explain the workings.

An ideal anomaly detection system would follow a machine learning approach, Clustering to be specific.

# Background
In a hostpital, there is a system that allows doctors to view files of patients, prescribe medications and all of that from their computers. Doctors have different specializations, and these specializations are useful in different scenarios, depending on the patient's condition. 

It would be weird if a doctor specializing in *dentistry* was to try to access the files of a patient suffering from *asthma* right? An anomaly detection system would be able to flag such an interaction, and record it in a database, to either refer back to in the future, or to use as proof to back up a suspiscion.

# Usage
To run this code, `python` has to be installed.

* Install requirements
```
pip install -r requirements.txt
```

* Generate an .env file with a random secret key and database URI
```
py create_env.py
```

* Create a mock database with 20 patients and 1 doctor
```
py populate_db.py
```

* Run the app
```
py run.py
```

After running the app, 20 patients would appear on the screen, and clicking on any patient other that FLU patients would trigger a popup on the screen saying **Suspiscious activity detected**. The interaction would also be logged to the database, indicating the doctor, patient, and that the interaction is suspiscious.

