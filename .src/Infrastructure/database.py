from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    date_of_birth = Column(String)
    address = Column(String)
    phone_number = Column(String)
    email = Column(String)

class MedicalRecord(Base):
    __tablename__ = 'medical_records'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    diagnoses = Column(String)
    treatments = Column(String)
    test_results = Column(String)

engine = create_engine('postgresql://user:password@host:port/dbname')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def create_patient(patient_data):
    patient = Patient(**patient_data)
    session.add(patient)
    session.commit()
    return patient

def get_patient(patient_id):
    return session.query(Patient).filter_by(id=patient_id).first()

def update_patient(patient_id, patient_data):
    patient = get_patient(patient_id)
    if patient:
        patient.name = patient_data['name']
        patient.date_of_birth = patient_data['date_of_birth']
        patient.address = patient_data['address']
        patient.phone_number = patient_data['phone_number']
        patient.email = patient_data['email']
        session.commit()
    return patient

def delete_patient(patient_id):
    patient = get_patient(patient_id)
    if patient:
        session.delete(patient)
        session.commit()

def create_medical_record(medical_record_data):
    medical_record = MedicalRecord(**medical_record_data)
    session.add(medical_record)
    session.commit()
    return medical_record

def get_medical_record(medical_record_id):
    return session.query(MedicalRecord).filter_by(id=medical_record_id).first()

def update_medical_record(medical_record_id, medical_record_data):
    medical_record = get_medical_record(medical_record_id)
    if medical_record:
        medical_record.diagnoses = medical_record_data['diagnoses']
        medical_record.treatments = medical_record_data['treatments']
        medical_record.test_results = medical_record_data['test_results']
        session.commit()
    return medical_record

def delete_medical_record(medical_record_id):
    medical_record = get_medical_record(medical_record_id)
    if medical_record:
        session.delete(medical_record)
        session.commit()
