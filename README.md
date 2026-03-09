# Drishyamitra – AI-Powered Photo Management System

## Overview

**Drishyamitra** is an AI-powered photo management system designed to intelligently organize, search, and distribute digital photographs.

The platform uses **deep learning–based facial recognition and conversational AI** to automate photo categorization and delivery.

Unlike traditional gallery systems that require manual sorting, Drishyamitra automatically:

* Detects faces in uploaded images
* Recognizes individuals
* Organizes photos into person-specific folders

Users can also interact with their photo collections through a **natural language chatbot** to search and distribute images.

---

# Problem Domain

Managing large photo collections has become increasingly difficult due to the massive number of images captured during:

* Events
* Vacations
* Professional activities

Traditional gallery applications rely heavily on **manual organization**, which is time-consuming and inefficient.

Users often struggle to:

* Locate specific images
* Share them with the right people
* Distribute large photo sets after events

**Drishyamitra solves this using AI-driven automation for photo recognition, categorization, and delivery.**

---

# Technology Stack

## Backend

* Python (Flask)
* SQLAlchemy ORM
* DeepFace AI Models
* NumPy
* OpenCV

## Frontend

* React.js
* TailwindCSS
* Axios
* React Router

## APIs & Services

* Groq API (Chatbot)
* Gmail API (Email delivery)
* WhatsApp Web API (Messaging)

## Deployment

* Docker
* Docker Compose
* Nginx

---

# Key Features

* Automatic face detection and recognition
* Intelligent photo organization into person folders
* Natural language chatbot interaction
* Automated photo delivery via email and WhatsApp
* Secure and scalable full-stack architecture

---

# Target Users

* Individuals managing personal photo collections
* Event photographers
* Media teams and marketing agencies
* Organizations managing digital assets

---

# Use Cases

## Family Photo Organization

A user uploads thousands of photos.

Drishyamitra automatically:

* Detects faces
* Groups images by person

Example query:

```
Show me photos of Grandma from Diwali 2022
```

The system instantly retrieves the images and can send them via email.

---

## Event Photographer Workflow

A wedding photographer uploads thousands of photos.

Drishyamitra:

* Detects bride, groom, and guests
* Groups images automatically

Example query:

```
Show all photos of the bride and groom during the ceremony
```

Photos can be delivered automatically via **email or WhatsApp**.

---

## Corporate Media Management

A marketing team manages event photos.

Example query:

```
Find photos of Rohan and Priya from the product launch
```

The system retrieves images and sends them to the PR team.

---

# System Architecture

### High-Level Flow

```
User
 ↓
React Frontend
 ↓
Flask Backend
 ↓
AI Models
 ↓
Database
 ↓
External APIs
 ↓
Response to User
```

---

# Architecture Components

## Frontend Layer

Built using **React.js and TailwindCSS**.

Features include:

* Photo uploads
* Gallery viewing
* Face labeling
* Chatbot interaction

---

## Backend Layer

Built with **Flask REST APIs** responsible for:

* Photo processing
* Face recognition
* Chatbot queries
* Delivery services

Frontend communicates using **Axios HTTP requests**.

---

## Database Layer

Database: **SQLite**

Managed using **SQLAlchemy ORM**

Stores:

* Users
* Photos
* Faces
* Persons
* Delivery history

Database migrations handled via **Alembic**.

---

## External Services

* Groq API → Chatbot AI
* Gmail API → Email delivery
* WhatsApp Web API → Messaging

---

# System Workflow

1. User uploads photos via frontend
2. Backend receives images through REST API
3. DeepFace performs face detection
4. Face embeddings are generated
5. Faces are matched with stored identities
6. Photos are organized into person folders
7. Users interact with chatbot to search photos
8. Photos can be delivered via email or WhatsApp

---

# Installation

## Prerequisites

* Python 3.8+
* Node.js 16+
* Docker
* Git

Hardware:

* Intel i5 or equivalent
* 8GB RAM
* 10GB free storage

---

# Environment Setup

Create Python virtual environment

```
python -m venv venv
```

Install backend dependencies

```
pip install -r requirements.txt
```

Install frontend dependencies

```
npm install
```

---

# Environment Variables

Create a `.env` file

```
GROQ_API_KEY=xxxx
GMAIL_API_KEY=xxxx
DATABASE_URL=sqlite:///database.db
```

---

# Project Structure

```
project_root/

backend/
frontend/
whatsapp_service/
docker-compose.yml
README.md
.gitignore
```

Main components:

* **backend/** → Flask APIs and AI modules
* **frontend/** → React web application
* **whatsapp_service/** → Node.js WhatsApp messaging service

---

# Backend Structure

```
backend/
 ├── app.py
 ├── config.py
 ├── models/
 ├── routes/
 ├── services/
 ├── migrations/
 ├── tasks.py
 ├── test_ai.py
```

### Models

* user.py
* photo.py
* face.py
* person.py
* delivery.py

### Routes

* auth_routes.py
* photo_routes.py
* face_routes.py
* chat_routes.py
* delivery_routes.py

### Services

* ai_service.py
* recognition_service.py
* chatbot_service.py
* email_service.py
* whatsapp_service.py

---

# Frontend Structure

```
frontend/src/
 ├── components/
 ├── pages/
 ├── hooks/
 ├── Context/
 ├── utils/
```

Main pages:

* Home
* Authentication
* Gallery

Key components:

* ChatAssistant
* PhotoModal
* Layout

---

# WhatsApp Microservice

Node.js service used for sending messages and images through **WhatsApp Web API**.

```
whatsapp_service/
 ├── index.js
 ├── package.json
 ├── .wwebjs_cache/
```

---

# Testing

## Test Cases

| Test | Description       | Result |
| ---- | ----------------- | ------ |
| TC01 | Photo Upload API  | Pass   |
| TC02 | Face Detection    | Pass   |
| TC03 | Face Recognition  | Pass   |
| TC04 | Chat Assistant    | Pass   |
| TC05 | Email Delivery    | Pass   |
| TC06 | WhatsApp Delivery | Pass   |
| TC07 | Authentication    | Pass   |

---

# Performance Metrics

| Operation        | Time        |
| ---------------- | ----------- |
| Face Detection   | 1–2 seconds |
| Face Recognition | 1–3 seconds |
| Chat Query       | < 1 second  |
| Photo Delivery   | 2–5 seconds |

---

# Deployment

Clone repository

```
git clone https://github.com/LightningHat/Drishyamitra
cd Drishyamitra
```

Build containers

```
docker-compose build
```

Start services

```
docker-compose up
```

Access application

Frontend

```
http://localhost:3000
```

Backend

```
http://localhost:5000
```

---

# Advantages

* Automated photo organization
* Natural language search
* Multi-platform delivery
* Scalable architecture

---

# Limitations

* Requires initial face labeling
* High computational requirements for large datasets
* Recognition accuracy depends on image quality

---

# Future Enhancements

* Mobile application
* Cloud storage integration
* Real-time camera recognition
* Multi-language chatbot

---

# Conclusion

Drishyamitra demonstrates how **AI and modern web technologies** can transform photo management systems.

By combining:

* Facial recognition
* Conversational AI
* Automated delivery services

the platform simplifies photo organization and sharing for both individuals and organizations.

---

# Repository

GitHub Repository
https://github.com/LightningHat/Drishyamitra

Live Demo
Clone the Repo and install dependencies to test out Drishyamitra
