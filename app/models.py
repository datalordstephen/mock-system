from datetime import datetime
from . import db
from enum import Enum


class SpecializationEnum(Enum):
    GENERAL = 'General'
    ORTHOPEDICS = 'Orthopedics'
    DENTISTRY = 'Dentistry' 
    CARDIOLOGY = 'Cardiology'

class ConditionEnum(Enum):
    FLU = 'Flu'
    FRACTURE = 'Fracture'
    TOOTHACHE = 'Toothache'
    HEARTDISEASE = 'Heart Disease'
    
class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    specialization = db.Column(db.Enum(SpecializationEnum))

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    condition = db.Column(db.Enum(ConditionEnum))

class AccessLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    suspicious = db.Column(db.Boolean)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
