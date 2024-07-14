from app import create_app, db
from app.models import Doctor, Patient, ConditionEnum, SpecializationEnum

def populate_patients_and_doctor():
    app = create_app()
    with app.app_context():
        db.drop_all()  # This will drop all tables. Use with caution.
        db.create_all()

        # Create 20 patients, 5 for each condition
        conditions = [ConditionEnum.FLU, ConditionEnum.FRACTURE, ConditionEnum.TOOTHACHE, ConditionEnum.HEARTDISEASE]
        for i in range(20):
            patient = Patient(
                name=f'Patient {i+1}',
                condition=conditions[i // 5]
            )
            db.session.add(patient)
        doctor = Doctor(
            name='Dr. Oba',
            specialization=SpecializationEnum.GENERAL
        )
        db.session.add(doctor)
        db.session.commit()

        print("Patients and Doctor added successfully.")

if __name__ == "__main__":
    populate_patients_and_doctor()
