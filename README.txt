Cloud Service Access Management System
Team members
Chanho Kim

Project Overview
This project is a backend system that controls access to cloud services based on user subscriptions. Each user subscribes to a plan, and based on the plan's permissions, they can access certain APIs. If they reach the limit defined in the plan, their access to that specific service is blocked temporarily. The purpose of this project is to learn about API access management, role-based controls, and basic usage tracking.
The system is built using FastAPI and SQLite with asynchronous support.

Tech Stack Used
- FastAPI (Python web framework)
- Uvicorn (ASGI server for running FastAPI)
- SQLAlchemy (ORM for database operations, async version)
- SQLite (file-based database, easy to set up and use)
- Python 3.12

Project Structure
cloud-access-system/
── app/
   ── main.py            # FastAPI application entry point
   ── database.py        # Database connection and session management
   ── models.py          # SQLAlchemy models (Plan, Subscription)
   ── routers/           # API routes separated by feature
        ─ plans.py
        ─ subscriptions.py
        ─ access.py
        ─ services.py
── requirements.txt       # Project dependencies

How to Run the Project
Make sure Python 3.12 or later is installed.
1. Install required packages:
   pip install -r requirements.txt

2. Start the FastAPI server:
   python -m uvicorn app.main:app --reload --port 8080

3. Open Swagger UI for testing:
   http://127.0.0.1:8080/docs
4. Basic API Usage Flow
   - Create a subscription plan
   - Subscribe a user to a plan
   - Check API access
   - Track usage
   - Re-check access after exceeding usage limit

Main Features
- Admin can create, modify, and delete subscription plans.
- Users can subscribe to a plan and view usage.
- The system checks if a user's API request is allowed based on their plan and usage.
- Usage is tracked per user and access is restricted if the limit is exceeded.
- Dummy cloud services (service1 ~ service6) are provided for testing.


Notes
- SQLite database (`cloud_access.db`) is created automatically when the server runs.
- All APIs can be tested directly through Swagger UI.
- This project is mainly for educational purposes, and the APIs are simulated.

GitHub Repository
https://github.com/1Hearts/cloud-access-management
