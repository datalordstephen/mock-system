from flask import render_template, request, jsonify
from . import db
from .models import Doctor, Patient, AccessLog
from . import create_app

app = create_app()

@app.route('/home')
def index():
    patients = Patient.query.all()
    return render_template('index.html', patients=patients)

@app.route('/access', methods=['POST'])
def access_patient():
    if request.method == "GET":
        return jsonify({"error": "Method not allowed"})
    
    data = request.json
    doctor_id = data.get('doctor_id')
    patient_id = data.get('patient_id')

    # Check for suspicious activity by seeing if the doctor is accessing a patient that isn't related to their specialization
    doctor = Doctor.query.get(doctor_id)
    patient = Patient.query.get(patient_id)
    suspicious = False
        
    doctor_to_patient = {
        "General": "Flu",
        "Dentist": "Toothache",
        "Cardiologist": "Heart Disease",
        "Orthopedic": "Fracture"
    }
    
    specialization = doctor.specialization.value
    condition = patient.condition.value
    if doctor_to_patient[specialization] != condition:
        suspicious = True
        
    print(f"{specialization} Doctor {doctor.name} accessed {condition} patient {patient.name} - Suspicious: {suspicious}")
    
    
    # Record the access attempt
    log = AccessLog(doctor_id=doctor_id, patient_id=patient_id, suspicious=suspicious)
    db.session.add(log)
    db.session.commit()
    
    return jsonify({'suspicious': suspicious})

