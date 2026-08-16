# agfzl-xrfgt-dealership

## Project Name: Cars Dealership Web Application

A full-stack web application for **Cars Dealership**, a national car retailer in the U.S. This application allows users to browse dealership branches, view dealer information, read reviews, and submit their own reviews.

## Technologies Used

### Frontend
- **React** – Component-based UI
- **HTML5 / CSS3** – Static pages (About, Contact)
- **Bootstrap** – Responsive design

### Backend
- **Django** – Main web framework (Python)
- **SQLite** – Database for Car Make/Model and user data
- **Django REST Framework** – API endpoints

### Microservices
- **Node.js + Express** – Dealer and Review microservice
- **MongoDB** – NoSQL storage for dealers and reviews
- **Flask** – Sentiment analysis microservice

### DevOps
- **Docker** – Containerization of all services
- **Docker Compose** – Multi-container orchestration
- **Kubernetes** – Container orchestration (deployment)
- **IBM Cloud Code Engine** – Cloud deployment
- **GitHub Actions** – CI/CD pipeline

## Project Structure

```
agfzl-xrfgt-dealership/
├── README.md
├── docker-compose.yml
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── server/
│   ├── djangoapp/              # Django app (models, views, urls)
│   ├── djangoproj/             # Django project settings
│   ├── frontend/               # React frontend + static HTML
│   │   ├── src/
│   │   │   └── components/
│   │   │       ├── Register/
│   │   │       ├── Login/
│   │   │       ├── Dealers/
│   │   │       ├── Dealer/
│   │   │       ├── PostReview/
│   │   │       └── Header/
│   │   └── static/
│   │       ├── About.html
│   │       └── Contact.html
│   ├── database/               # Node.js + MongoDB microservice
│   └── sentiment_analyzer/     # Flask sentiment microservice
└── submission_outputs/         # Grading evidence files
```

## Features

- Browse all dealerships nationwide
- Filter dealerships by state
- View dealer details and customer reviews
- Submit reviews (authenticated users only)
- Sentiment analysis on reviews (positive/negative/neutral)
- User registration and authentication
- Admin panel for managing car makes, models, and dealers

## Setup & Running

See individual service READMEs for setup instructions, or use Docker Compose:

```bash
docker-compose up --build
```

## Live Deployment

Deployed on IBM Cloud Code Engine. See `submission_outputs/deploymentURL` for the live URL.
