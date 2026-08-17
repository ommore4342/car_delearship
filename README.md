car_delearship

Project Name: Cars Dealership Web Application

A full-stack web application for Cars Dealership, a national car retailer in the U.S. The application allows users to browse dealership branches, view dealer details and reviews, register/login, and submit reviews.

Repository Details

Repository Name: car_delearship

Project Name: Cars Dealership Web Application

Technologies Used

Frontend

React

HTML5 / CSS3

Bootstrap

JavaScript

Backend

Django

SQLite

Django REST Framework

Microservices

Node.js + Express

MongoDB

Flask sentiment-analysis service

DevOps

Docker

Docker Compose

Kubernetes

IBM Cloud Code Engine

GitHub Actions CI/CD

Main Features

Browse dealership branches

Filter dealers by state

View dealer details

View customer reviews

Submit reviews for a dealer after login

User registration and authentication

Sentiment analysis of review text

Car makes and models API

Django administration panel

Responsive About Us and Contact Us pages

Project Structure

car_delearship/
├── README.md
├── .github/
│   └── workflows/
├── server/
│   ├── djangoapp/
│   ├── djangoproj/
│   └── frontend/
│       ├── src/
│       │   └── components/
│       │       ├── Register/
│       │       ├── Login/
│       │       ├── Dealers/
│       │       ├── Dealer/
│       │       ├── PostReview/
│       │       └── Header/
│       └── static/
│           ├── About.html
│           └── Contact.html
└── submission_outputs/

Running the Django Application

From the server directory:

python manage.py migrate
python manage.py runserver

The Django development server runs at:

http://127.0.0.1:8000/

API / Microservice Endpoints

The project includes dealer, review, car-make/model, authentication, and sentiment-analysis functionality. The exact evidence commands and outputs used for the capstone submission are stored under submission_outputs/.

CI/CD

GitHub Actions is used for linting, testing, React build, Flask checks, and Docker image builds.

Deployment

The project is prepared for deployment using Docker/Kubernetes and IBM Cloud Code Engine. The deployment evidence is stored in submission_outputs/deploymentURL.
