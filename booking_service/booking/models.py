from django.db import models

class Doctor(models.Model):
    """
    Represents a doctor with their name, specialty, and availability.

    Attributes:
        name (CharField): Doctor's full name.
        specialty (CharField): Doctor's medical specialty.
        availability (JSONField): Doctor's availability schedule in JSON format. 
                                  Example: {"Monday": "9-5", "Tuesday": "10-4"}
    """
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    availability = models.JSONField()

class Appointment(models.Model):
    """
    Represents a scheduled appointment between a patient and a doctor.

    Attributes:
        patient (ForeignKey): ForeignKey to the Patient model in the `patient_service` app.
        doctor (ForeignKey): ForeignKey to the Doctor model.
        date (DateField): Date of the appointment.
        time (TimeField): Time of the appointment.
        status (CharField): Status of the appointment (e.g., 'Scheduled', 'Completed').
    """
    patient = models.ForeignKey('patient.Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=50, choices=[
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed')
    ])