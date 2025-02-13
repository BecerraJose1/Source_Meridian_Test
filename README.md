# 📖 Source Meridian Technical Test

## 🚀 Project Overview
This is a simple **Book Management System** built using **Flask (Python) for the backend**, **MySQL as the database**, and **Angular for the frontend**. The project allows users to manage a collection of books, including adding, editing, deleting, and marking books as read.

## 📌 Technologies Used
- **Frontend:** Angular 19
- **Backend:** Flask (Python 3.12.3)
- **Database:** MySQL 8
- **Containerization:** Docker & Docker Compose

## ⚙️ Prerequisites
Before you start, ensure you have the following installed:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## 📥 Clone the Repository
```bash
git clone https://github.com/BecerraJose1/Source_Meridian_Test.git
cd source_meridian_test
```

## 🏗️ Build and Start the Containers
Run the following command to build and start the project:
```bash
docker-compose up -d --build
```
This will:
- Build and start the **MySQL database** container.
- Build and start the **Flask backend** container.
- Build and start the **Angular frontend** container.

## 🔍 Verify Running Containers
Check if all services are running correctly:
```bash
docker ps
```

## 📂 Project Structure
```
book-management/
│── backend/            # Flask API
│   ├── app.py          # Main application
│   ├── routes.py       # API routes
│   ├── models.py       # Database models
│   ├── schemas.py      # Marshmallow schemas
│   ├── config.py       # Configuration file
│   ├── db/             # Database scripts
│   ├── requirements.txt # Python dependencies
│
│── frontend/           # Angular Application
│   ├── src/            # Source code
│   ├── angular.json    # Angular configuration
│   ├── package.json    # Node.js dependencies
│   ├── Dockerfile      # Docker build file
│
│── docker-compose.yml  # Docker Compose file
│── README.md
│── License
```

## 🖥️ Accessing the Application
- **Frontend:** `http://localhost:4200`
- **Backend API:** `http://localhost:5000`
- **Database (MySQL):** Accessible on `localhost:3506`

## 🗄️ Database Initialization
The database is automatically set up when the MySQL container starts. The following SQL script initializes the database and inserts some sample data:

```sql
CREATE DATABASE IF NOT EXISTS db;
USE db;

CREATE TABLE IF NOT EXISTS book (
    id VARCHAR(32) PRIMARY KEY NOT NULL,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL,
    read_flag BOOLEAN DEFAULT FALSE
);

INSERT INTO book (id, title, author, read_flag) VALUES
    ('ce13a4af4fb245f1b0cb14798fbc5f11', 'On the Road', 'Jack Kerouac', TRUE),
    ('72d6668394a8493f8c15b74cfb5527fd', 'Harry Potter and the Philosopher\s Stone', 'J. K. Rowling', FALSE),
    ('72d6668394a8493f8c15b74cfb5527fd', 'Green Eggs and Ham', 'Dr. Seuss', TRUE);

ALTER USER 'root'@'%' IDENTIFIED WITH 'caching_sha2_password' BY 'rootpassword';
FLUSH PRIVILEGES;
```

## 📦 Stopping the Containers
To stop all running services, use:
```bash
docker-compose down
```

## 🛠️ Troubleshooting
- If MySQL takes time to initialize, the Flask backend might fail to connect. Restart the backend after MySQL is fully running:
```bash
docker-compose restart backend
```
- If you encounter port conflicts, make sure the ports **4200 (Frontend), 5000 (Backend), and 3506 (MySQL)** are not already in use.


🚀 Happy coding!

