# MySQL CRUD Project

Reusable Python MySQL CRUD project.

## Setup

pip install -r requirements.txt

Create database:

CREATE DATABASE studentdb;

USE studentdb;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

Run:

python main.py
