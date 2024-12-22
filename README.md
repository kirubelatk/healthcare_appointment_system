# healthcare_appointment_system


## Overview
The Healthcare Appointment Booking System is a distributed system built using a microservices architecture. It allows patients to book appointments with doctors, manage their profiles, and receive notifications for upcoming appointments.

## Features
- Patient Management: Create, update, and manage patient profiles, including medical history.
- Doctor Availability and Booking: View doctor schedules and book, reschedule, or cancel appointments.
- Notification System: Receive reminders and confirmations for appointments using RabbitMQ and Celery.
- Scalable Design: Built for reliability, fault tolerance, and seamless communication between microservices.

## Core Technologies
- Backend:
  - Django REST Framework for building APIs.
  - RabbitMQ for asynchronous inter-service communication.
  - Celery for task scheduling and background processing.
- Database:
  - PostgreSQL for patient data and medical history.
  - MySQL for managing doctor availability and appointments.
- Version Control:
  - GitHub for source code management and collaboration.

## Architecture
The system consists of three core microservices:
1. Patient Management Service: Handles patient data.
2. Doctor Availability and Booking Service: Manages doctor schedules and appointments.
3. Notification Service: Sends appointment reminders and confirmations.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Cherub21/healthcare_appointment_system.git
   cd healthcare_appointment_system

## Contributions
Collaborators working on this project can list their names here:

Kirubel Dagnachew
Kirubel Ateka
Desalegn Sendek
Natnael Endale
Natnael Mulugeta
Laelay Temesgen 
Mitiku Abebe
