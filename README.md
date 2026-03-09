1. PROJECT TITLE
Drishyamitra – AI-Powered Photo Management System
________________________________________
2. PROJECT DESCRIPTION
System Overview
Drishyamitra is an AI-powered photo management system designed to intelligently organize, search, and distribute digital photographs. The platform uses deep learning–based facial recognition and conversational AI to automate photo categorization and delivery.
Unlike traditional gallery systems that require manual sorting, Drishyamitra automatically detects faces in uploaded images, recognizes individuals, and organizes photos into person-specific folders. Users can also interact with their photo collections through a chatbot that understands natural language queries.
The system integrates modern web technologies with artificial intelligence to provide an efficient and user-friendly solution for photo management.
________________________________________
Problem Domain
Managing large photo collections has become increasingly difficult due to the massive number of images captured during events, vacations, and professional activities. Traditional gallery applications rely heavily on manual organization, which is time-consuming and inefficient.
Users often struggle to locate specific images or share them with the right people. Event photographers and organizations face similar challenges when distributing thousands of photos to clients or team members.
Drishyamitra addresses these problems by introducing AI-driven automation for photo recognition, categorization, and delivery.
________________________________________


Core Technology Used
• Python (Flask Backend)
• React.js (Frontend Interface)
• DeepFace AI Models
• SQLAlchemy ORM
• Groq API for chatbot
• Gmail API
• WhatsApp Web API
• Docker & Nginx for deployment
________________________________________
Key Capabilities
• Automatic face detection and recognition
• Intelligent photo organization into person folders
• Natural language chatbot interaction
• Automated photo delivery via email and WhatsApp
• Secure and scalable full-stack architecture
________________________________________
Target Users
• Individual users managing personal photo collections
• Event photographers
• Media teams and marketing agencies
• Organizations managing digital assets
________________________________________
Real-World Relevance
Drishyamitra simplifies photo management using artificial intelligence, making it valuable for individuals and organizations that handle large image collections.
________________________________________


3. APPLICATION SCENARIOS / USE CASES
Scenario 1 – Family Photo Organization
Riya has thousands of photos stored across multiple devices. After uploading them to Drishyamitra, the system detects faces and organizes photos into folders like “Mom”, “Dad”, and “Grandma”.
She can search using natural language such as:
“Show me photos of Grandma from Diwali 2022.”
The system instantly retrieves those images and can even send them via email.
________________________________________
Scenario 2 – Event Photographer Workflow
A wedding photographer uploads thousands of photos from an event. Drishyamitra automatically detects the bride, groom, and guests.
The photographer can request:
“Show all photos of the bride and groom during the ceremony.”
The system retrieves the images and can automatically deliver them to clients via email or WhatsApp.
________________________________________
Scenario 3 – Corporate Media Management
A marketing team uses Drishyamitra to manage event and campaign photos. When a manager asks:
“Find photos of Rohan and Priya from the product launch.”
The system retrieves the images and sends them to the PR team.
________________________________________

4. TECHNICAL ARCHITECTURE OVERVIEW
Architecture Diagram
 
________________________________________
Component Interaction Diagram
User → React Frontend → Flask Backend → AI Models → Database → External APIs → Response to User
________________________________________


Architecture Explanation
Frontend Layer
The frontend is built using React.js and TailwindCSS. It provides the user interface for uploading photos, viewing galleries, labeling faces, and interacting with the chatbot.
Backend Layer
The backend is implemented using Flask and exposes RESTful APIs for photo processing, face recognition, chatbot queries, and delivery services. These APIs are consumed by the React frontend using HTTP requests handled through Axios.
Database Layer
The system uses SQLite as the primary database, managed through SQLAlchemy ORM. Database schema changes are managed using Alembic migrations, which maintain version-controlled database structures. The database stores user information, photos, detected faces, recognized persons, and delivery history.
External APIs / Services
• Groq API for chatbot interaction
• Gmail API for email delivery
• WhatsApp Web API for messaging
Deployment Environment
The system is containerized using Docker and orchestrated using Docker Compose. Nginx can be used as a reverse proxy with SSL security in production environments.
________________________________________
5. PREREQUISITES
5.1 Software Requirements
• Python 3.8+
• Node.js 16+
• Flask Framework
• React.js
• Docker
• Nginx
• Git
________________________________________
5.2 Libraries / Frameworks / Dependencies
Backend Libraries
• Flask
• SQLAlchemy
• DeepFace
• NumPy
• OpenCV
• Requests
Frontend Libraries
• React.js
• Axios
• React Router
• TailwindCSS
________________________________________
5.3 Hardware Requirements
Minimum Requirements
• Processor: Intel i5 or equivalent
• RAM: 8GB
• Storage: 10GB free disk space
• Internet connection
________________________________________
6. PRIOR KNOWLEDGE REQUIRED
• Python programming
• JavaScript and React basics
• Database fundamentals
• REST API concepts
• AI/ML basics
• Web development fundamentals
________________________________________


7. PROJECT OBJECTIVES
Technical Objectives
Develop a scalable AI-based photo management system capable of automatic recognition and organization.
Performance Objectives
Provide fast face recognition and quick photo retrieval.
Deployment Objectives
Deploy the system using containerized infrastructure for reliability.
Learning Outcomes
Gain experience in full-stack development, AI integration, and system deployment.
________________________________________
8. SYSTEM WORKFLOW
1.	User uploads photos via frontend.
2.	Backend receives images through REST API.
3.	Face detection is performed using DeepFace models.
4.	Face embeddings are generated and matched with stored identities.
5.	Photos are organized into person-specific folders.
6.	Users interact with the chatbot to search or deliver photos.
7.	Photos are delivered via Gmail or WhatsApp.
________________________________________
9. MILESTONE 1: REQUIREMENT ANALYSIS & SYSTEM DESIGN
9.1 Problem Definition
Manual photo organization is inefficient and time-consuming. Users require an automated solution to detect, categorize, and share images intelligently.
________________________________________
9.2 Functional Requirements
• Upload photos
• Detect faces
• Recognize individuals
• Organize photos automatically
• Search photos using chatbot
• Deliver photos via email or WhatsApp
________________________________________
9.3 Non-Functional Requirements
• High accuracy face recognition
• Secure data storage
• Fast system response time
• Scalable architecture
________________________________________
9.4 System Design Decisions
The system uses a client-server architecture separating frontend, backend, and AI processing.
________________________________________
9.5 Technology Stack Selection Justification
Flask provides lightweight backend development while React ensures dynamic user interfaces. DeepFace provides reliable facial recognition models.
________________________________________
10. MILESTONE 2: ENVIRONMENT SETUP & INITIAL CONFIGURATION
10.1 Development Environment Setup
Create Python virtual environment and install Node.js.
python -m venv venv
________________________________________
10.2 Dependency Installation
Backend
pip install -r requirements.txt
Frontend
npm install
________________________________________
10.3 Project Structure Creation
project_root/

├── backend/
├── frontend/
├── whatsapp_service/
├── docker-compose.yml
├── README.md
├── .gitignore
________________________________________
10.4 Configuration Setup
Create .env files containing:
GROQ_API_KEY=xxxx
GMAIL_API_KEY=xxxx
DATABASE_URL=sqlite:///database.db
________________________________________
11. MILESTONE 3: CORE SYSTEM DEVELOPMENT
11.1 Feature 1 – Face Recognition System
Uses DeepFace models such as Facenet512, RetinaFace, and MTCNN for detecting and recognizing faces in uploaded images.
________________________________________
11.2 Feature 2 – Smart Photo Organization
Photos are automatically categorized into folders based on recognized individuals.
________________________________________
11.3 Feature 3 – Chatbot Assistant
The chatbot uses the Groq API to process natural language queries and perform actions such as searching or delivering photos.
________________________________________
12. MILESTONE 4: INTEGRATION & OPTIMIZATION
12.1 Component Integration
Frontend, backend, AI modules, and external APIs are integrated using REST APIs.
________________________________________
12.2 Performance Optimization
Face embeddings are cached to reduce processing time for repeated recognitions.
________________________________________
12.3 Security Enhancements
• Secure authentication using bcrypt-based password hashing
• Encrypted face embeddings
• Secure API endpoints
________________________________________
12.4 Error Handling & Validation
The system validates inputs, handles missing files, and logs errors for debugging.
________________________________________
13. MILESTONE 5: TESTING & VALIDATION
Testing and validation were conducted to ensure that the Drishyamitra system functions correctly across its backend services, AI modules, and frontend interface. Both unit testing and integration testing were performed to validate the performance and reliability of the system.
________________________________________
13.1 Test Cases
TC01 – Photo Upload API – Upload image – Image stored and processed – Pass
TC02 – Face Detection – Upload photo with faces – Faces detected – Pass
TC03 – Face Recognition – Upload labeled person – Correct identification – Pass
TC04 – Chat Assistant – Query photos – Relevant photos retrieved – Pass
TC05 – Email Delivery – Send selected photos – Email sent – Pass
TC06 – WhatsApp Delivery – Send photos – Message delivered – Pass
TC07 – Authentication – Login credentials – Secure login generated – Pass
________________________________________
13.2 Unit Testing
Backend modules were tested using Python scripts including:
• test_ai.py
• check_tf.py
Frontend testing used:
• App.test.js
• setupTests.js
________________________________________
13.3 Integration Testing
Integration testing verified communication between:
• Frontend and Backend APIs
• AI recognition services and database
• Chat assistant and AI services
• Photo delivery services and messaging APIs
________________________________________
13.4 User Acceptance Testing
Full workflow testing confirmed:
• Photo upload and processing
• Face labeling
• Chat-based search
• Email and WhatsApp delivery
• Gallery viewing
________________________________________
13.5 Performance Metrics
Face Detection: 1–2 seconds
Face Recognition: 1–3 seconds
Chat Query Processing: <1 second
Photo Delivery: 2–5 seconds
________________________________________
14. DEPLOYMENT
Deployment refers to making the Drishyamitra system operational in a development or production environment using containerized infrastructure.
________________________________________
14.1 Deployment Architecture
Frontend → React application
Backend → Flask API services
Database → SQLite with SQLAlchemy
Messaging → Node.js WhatsApp Web microservice
Docker containers isolate each service and are orchestrated using Docker Compose.
________________________________________
14.2 Hosting Platform
Possible hosting environments include:
• AWS
• Google Cloud
• Microsoft Azure
• DigitalOcean
• On-premise servers
________________________________________
14.3 Deployment Steps
Clone repository
git clone https://github.com/LightningHat/Drishyamitra
cd Drishyamitra
Build containers
docker-compose build
Start services
docker-compose up
Access application
Frontend
http://localhost:3000
Backend
http://localhost:5000
________________________________________
15. PROJECT STRUCTURE
├── .gitignore
├── .vscode
|     ├── settings.json
├── README.md
├── backend
|     ├── Dockerfile
|     ├── app.py
|     ├── check_tf.py
|     ├── config.py
|     ├── download_models.py
|     ├── migrations
|     |     ├── README
|     |     ├── alembic.ini
|     |     ├── env.py
|     |     ├── script.py.mako
|     |     ├── versions
|     |     |     ├── 01738e19f15b_added_roles_and_bcrypt_hashing.py
|     |     |     ├── 2ca7ea87a329_initial_schema_creation.py
|     ├── models
|     |     ├── db.py
|     |     ├── delivery.py
|     |     ├── face.py
|     |     ├── person.py
|     |     ├── photo.py
|     |     ├── user.py
|     ├── requirements.txt
|     ├── routes
|     |     ├── auth_routes.py
|     |     ├── chat_routes.py
|     |     ├── delivery_routes.py
|     |     ├── face_routes.py
|     |     ├── main_routes.py
|     |     ├── photo_routes.py
|     ├── services
|     |     ├── ai_service.py
|     |     ├── chatbot_service.py
|     |     ├── delivery_tracker.py
|     |     ├── email_service.py
|     |     ├── recognition_service.py
|     |     ├── whatsapp_service.py
|     ├── tasks.py
|     ├── test.jpg
|     ├── test_ai.py
|     ├── utils
|     |     ├── decorators.py
├── docker-compose.yml
├── frontend
|     ├── .gitignore
|     ├── Dockerfile
|     ├── README.md
|     ├── package-lock.json
|     ├── package.json
|     ├── postcss.config.js
|     ├── public
|     |     ├── favicon.ico
|     |     ├── index.html
|     |     ├── logo192.png
|     |     ├── logo512.png
|     |     ├── manifest.json
|     |     ├── robots.txt
|     ├── src
|     |     ├── App.css
|     |     ├── App.js
|     |     ├── App.test.js
|     |     ├── Context
|     |     |     ├── AppContext.js
|     |     ├── components
|     |     |     ├── ChatAssistant.js
|     |     |     ├── Layout.js
|     |     |     ├── PhotoModal.js
|     |     ├── hooks
|     |     |     ├── useVoiceInput.js
|     |     ├── index.css
|     |     ├── index.js
|     |     ├── logo.svg
|     |     ├── pages
|     |     |     ├── Auth.js
|     |     |     ├── Gallery.js
|     |     |     ├── Home.js
|     |     ├── reportWebVitals.js
|     |     ├── setupTests.js
|     |     ├── utils
|     |     |     ├── config.js
|     ├── tailwind.config.js
├── whatsapp_service
|     ├── .wwebjs_cache
|     |     ├── 2.3000.1034402126.html
|     ├── index.js
|     ├── package-lock.json
|     ├── package.json
Root Directory
The root directory contains configuration files and the main folders that make up the system.
.gitignore
Specifies files and folders that should not be tracked by Git, such as temporary files, environment variables, and build artifacts.
.vscode/
Contains Visual Studio Code workspace configuration.
•	settings.json – Editor-specific settings for development.
README.md
Provides an overview of the project, installation instructions, and usage guidelines for developers.
docker-compose.yml
Defines the multi-container deployment configuration for the application. It specifies how the backend, frontend, and messaging services are built and executed together.
________________________________________
Backend Directory (backend/)
The backend folder contains the Flask-based server, AI modules, API routes, database models, and business logic for the system.
________________________________________
Core Backend Files
Dockerfile
Defines the container configuration for the backend service. It installs Python dependencies and sets up the runtime environment.
app.py
The main entry point of the Flask application. It initializes the server, registers routes, and connects system components.
config.py
Stores configuration settings such as database connections, environment variables, and application settings.
check_tf.py
A utility script used to verify that the TensorFlow environment and AI dependencies are correctly installed.
download_models.py
Downloads required AI models used by the DeepFace recognition system.
tasks.py
Handles asynchronous or background tasks such as processing images or managing delivery operations.
test_ai.py
Contains testing scripts for validating the AI recognition functionality.
test.jpg
A sample image used for testing the face recognition system.
________________________________________
Database Migration Directory (backend/migrations/)
This folder contains Alembic migration scripts used to manage database schema updates.
alembic.ini
Configuration file for Alembic migrations.
env.py
Defines the migration environment and database connection configuration.
script.py.mako
Template used by Alembic to generate migration scripts.
versions/
Contains versioned migration files that track database schema changes.
Example migrations include:
•	initial_schema_creation.py – Creates initial database tables.
•	added_roles_and_bcrypt_hashing.py – Adds role management and password hashing support.
________________________________________
Database Models (backend/models/)
This directory contains SQLAlchemy ORM models that define the database structure.
db.py
Initializes the database connection and SQLAlchemy instance.
user.py
Defines the user model, including authentication-related fields.
photo.py
Stores metadata for uploaded photos.
face.py
Represents detected faces within images and associated embeddings.
person.py
Stores information about recognized individuals in the system.
delivery.py
Tracks photo delivery history via email or messaging platforms.
________________________________________
API Routes (backend/routes/)
This directory defines REST API endpoints used by the frontend.
auth_routes.py
Handles user authentication such as login and registration.
photo_routes.py
Manages image uploads, retrieval, and gallery operations.
face_routes.py
Handles face detection and labeling operations.
chat_routes.py
Processes chatbot queries and commands.
delivery_routes.py
Manages photo delivery through email or messaging services.
main_routes.py
Contains general API endpoints such as health checks or root routes.
________________________________________
Service Layer (backend/services/)
The services directory contains the core business logic and AI processing modules.
ai_service.py
Handles AI model initialization and interaction with DeepFace models.
recognition_service.py
Performs face recognition and matching using stored embeddings.
chatbot_service.py
Processes chatbot queries using the Groq API.
email_service.py
Handles sending photos via email using the Gmail API.
whatsapp_service.py
Acts as the backend integration layer that communicates with the WhatsApp messaging service.
delivery_tracker.py
Tracks delivery status and records messaging or email operations.
________________________________________
Utility Functions (backend/utils/)
decorators.py
Contains custom Python decorators used for authentication, authorization, or request validation.
________________________________________
Frontend Directory (frontend/)
The frontend folder contains the React-based web application that provides the user interface.
________________________________________
Frontend Configuration Files
Dockerfile
Defines the container configuration for building and running the React application.
package.json
Lists all frontend dependencies and project scripts.
package-lock.json
Locks the exact versions of installed dependencies.
postcss.config.js
Configuration for PostCSS used with TailwindCSS.
tailwind.config.js
Configuration file for the TailwindCSS styling framework.
________________________________________
Public Assets (frontend/public/)
Contains static files that are served directly by the web application.
index.html
Main HTML file used by the React application.
favicon.ico
Website favicon displayed in browser tabs.
logo192.png and logo512.png
Application logo images.
manifest.json
Provides metadata for progressive web app support.
robots.txt
Defines crawler access rules for search engines.
________________________________________
React Source Code (frontend/src/)
Contains the main frontend application logic.
index.js
Entry point for the React application.
App.js
Main application component that manages routing and layout.
App.css
Main stylesheet for the application.
setupTests.js
Configures the testing environment for React components.
App.test.js
Contains unit tests for the main React application.
________________________________________
React Context (frontend/src/Context/)
AppContext.js
Implements global state management using React Context.
________________________________________
React Components (frontend/src/components/)
Reusable UI components used throughout the application.
ChatAssistant.js
Chat interface that allows users to interact with the AI assistant.
Layout.js
Defines the main layout structure for the application pages.
PhotoModal.js
Displays enlarged photo previews and additional image information.
________________________________________
Custom Hooks (frontend/src/hooks/)
useVoiceInput.js
Provides voice input functionality for chatbot queries.
________________________________________
Application Pages (frontend/src/pages/)
Defines the main pages of the application.
Home.js
Landing page of the application.
Auth.js
Handles user login and authentication.
Gallery.js
Displays uploaded photos and organized image collections.
________________________________________
Frontend Utilities (frontend/src/utils/)
config.js
Stores frontend configuration such as API endpoints.
________________________________________
WhatsApp Service (whatsapp_service/)
This directory contains the Node.js microservice responsible for WhatsApp messaging integration.
index.js
Main entry point for the WhatsApp messaging service. It connects to WhatsApp Web and handles sending messages and images.
package.json
Lists dependencies required for the messaging service.
package-lock.json
Locks dependency versions.
.wwebjs_cache/
Stores cached session data for the WhatsApp Web client to maintain authentication between runs.
________________________________________
16. RESULTS
The system successfully detects and recognizes faces and organizes photos into person-specific folders.Users can retrieve images using chatbot queries and send them via email or WhatsApp.
Screenshots
 
 

________________________________________


17. ADVANTAGES & LIMITATIONS
Advantages
• Automated photo organization
• Natural language search
• Multi-platform delivery
• Scalable architecture
Limitations
• Requires initial face labeling
• High computational requirements for large datasets
• Recognition accuracy depends on image quality
________________________________________
18. FUTURE ENHANCEMENTS
• Mobile application support
• Cloud storage integration
• Real-time camera recognition
• Multi-language chatbot
________________________________________
19. CONCLUSION
Drishyamitra demonstrates how artificial intelligence and modern web technologies can transform photo management systems. By combining facial recognition, conversational AI, and automated delivery services, the platform simplifies photo organization and sharing.
________________________________________
20. APPENDIX
Source Code
Configuration files:
API documentation:
GitHub Repository: https://github.com/LightningHat/Drishyamitra
Live Demo Link
( deployed link)

