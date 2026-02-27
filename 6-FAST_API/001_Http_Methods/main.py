from fastapi import FastAPI, Path, Body, HTTPException, Query
import json
        
app = FastAPI()

# load_data() function to read patients.json
def load_data():
    try:
        with open('patients.json', 'r') as f:
            patients = json.load(f)
    except FileNotFoundError:
        patients = {}
    return patients

# read_patients() function to read all patients
# Add a query param to sort the patients by age
@app.get('/patients')
def read_patients(sort_by: str = Query(None, description='Sort the patients by age')):
    # read patients.json
    patients = load_data()
    # sort the patients by age
    if sort_by == 'age':
        patients = dict(sorted(patients.items(), key=lambda item: item[1]['age'], reverse=True))  
    return patients 

# read_patient() function to read a patient by id       
@app.get('/patients/{patient_id}')
def read_patient(patient_id: str = Path(..., description='The ID of the patient to read')):
    # read patients.json
    patients = load_data()
    if patient_id not in patients:
        raise HTTPException(status_code=404, detail='Patient not found')
    return patients[patient_id] 

# update_patient() function to update a patient by id
@app.put('/patients/{patient_id}')
def update_patient(patient_id: str = Path(..., description='The ID of the patient to update'), patient: dict = Body(..., description='The patient data to update')):
    # read patients.json
    patients = load_data()
    # update patient in patients    
    if patient_id not in patients:
        raise HTTPException(status_code=404, detail='Patient not found')            
    patients[patient_id] = patient
    # write patients.json
    with open('patients.json', 'w') as f:
        json.dump(patients, f, indent=4)
    return {'message': 'Patient updated', 'patient_id': patient_id}         

# Create_patient() function to create a patient
@app.post('/patients/{patient_id}')
def create_patient(patient_id: str = Path(..., description='The ID of the patient to create'), patient: dict = Body(..., description='The patient data to create')):
    # read patients.json
    patients = load_data()
    # create patient in patients    
    if patient_id in patients:
        raise HTTPException(status_code=400, detail='Patient already exists')
    patients[patient_id] = patient
    # write patients.json
    with open('patients.json', 'w') as f:
        json.dump(patients, f, indent=4)
    return {'message': 'Patient created', 'patient_id': patient_id}             

# delete_patient() function to delete a patient by id
@app.delete('/patients/{patient_id}')
def delete_patient(patient_id: str = Path(..., description='The ID of the patient to delete')):
    # read patients.json
    patients = load_data()
    # delete patient in patients    
    if patient_id not in patients:
        raise HTTPException(status_code=404, detail='Patient not found')            
    del patients[patient_id]
    # write patients.json
    with open('patients.json', 'w') as f:
        json.dump(patients, f, indent=4)
    return {'message': 'Patient deleted', 'patient_id': patient_id}         