def insert_patient_date(name, age):
    if age < 0:
        print('Age cannot be negative')
        raise ValueError('Age cannot be negative')
    print(name)
    print(age)
    print('Inserted patient data')


def insert_patient_date_data_type_info(name:str, age:int):
    print(name)
    print(age)
    print('Inserted patient data')

def insert_patient_date_validation(name, age):
    if isinstance(name, str) and isinstance(age, int):
        print(name)
        print(age)
        print('Inserted patient data')
    else:
        print('Invalid data type')


insert_patient_date('Pratap', 25)