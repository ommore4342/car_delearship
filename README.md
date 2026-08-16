# car_delearship

## Project Name: Cars Dealership Web Application

**Repository:** [https://github.com/ommore4342/car_delearship](https://github.com/ommore4342/car_delearship)

A full-stack web application for **Cars Dealership**, a national car retailer in the U.S. This application allows users to browse dealership branches, view dealer information, read reviews, and submit their own reviews.

---

## Technologies Used

### Frontend
- **HTML5 / CSS3 / Bootstrap 5** – Responsive static pages (Home, About, Contact)
- **React** – Component-based UI (Register, Login, Dealers, Dealer Detail, Post Review)
- **Vanilla JavaScript** – SPA routing and dynamic dealer rendering

### Backend
- **Django 4.2** – Main web framework (Python)
- **SQLite** – Database for Car Makes, Models, Dealers, Reviews, and user auth
- **Gunicorn** – Production WSGI server
- **WhiteNoise** – Static file serving in production

### Microservices
- **Node.js + Express** – Dealer and Review microservice
- **MongoDB** – NoSQL storage for dealers and reviews
- **Flask** – Sentiment analysis microservice (positive / negative / neutral)

### DevOps
- **Docker** – Containerization of all services
- **Docker Compose** – Multi-container orchestration
- **Kubernetes** – Container orchestration manifests (`k8s/`)
- **Render** – Cloud deployment (free tier)
- **GitHub Actions** – CI/CD pipeline (`.github/workflows/ci-cd.yml`)

---

## Project Structure

```
car_delearship/
├── README.md
├── render.yaml                      # Render deployment config
├── docker-compose.yml               # Multi-service Docker setup
├── .github/
│   └── workflows/
│       └── ci-cd.yml                # GitHub Actions CI/CD
├── k8s/
│   └── deployment.yml               # Kubernetes manifests
├── server/
│   ├── manage.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── build.sh                     # Render build script
│   ├── db.sqlite3                   # SQLite database (seeded)
│   ├── djangoproj/                  # Django project settings & URLs
│   ├── djangoapp/                   # Django app
│   │   ├── models.py                # CarMake, CarModel, Dealer, Review
│   │   ├── views.py                 # Auth, Dealers, Reviews, Sentiment
│   │   ├── urls.py                  # API routes
│   │   ├── admin.py                 # Admin panel configuration
│   │   ├── populate.py              # Seed data functions
│   │   └── migrations/
│   ├── frontend/
│   │   ├── static/
│   │   │   ├── index.html           # Main SPA homepage
│   │   │   ├── About.html           # About Us page
│   │   │   └── Contact.html         # Contact Us page
│   │   └── src/
│   │       └── components/
│   │           ├── Register/        # Register.jsx
│   │           ├── Login/           # Login.jsx
│   │           ├── Header/          # Header.jsx
│   │           ├── Dealers/         # Dealers.jsx
│   │           ├── Dealer/          # Dealer.jsx
│   │           └── PostReview/      # PostReview.jsx
│   ├── database/                    # Node.js + MongoDB microservice
│   │   ├── app.js
│   │   ├── package.json
│   │   ├── Dockerfile
│   │   └── app/
│   │       ├── models/              # dealer.js, review.js
│   │       └── routers/             # dealer.js routes
│   └── sentiment_analyzer/          # Flask sentiment microservice
│       ├── app.py
│       ├── requirements.txt
│       └── Dockerfile
└── submission_outputs/              # Grading evidence files
    ├── django_server
    ├── loginuser
    ├── logoutuser
    ├── getalldealers
    ├── getdealerbyid
    ├── getdealersbyState
    ├── getdealerreviews
    ├── getallcarmakes
    ├── analyzereview
    ├── CICD
    └── deploymentURL
```

---

## Features

- Browse all dealerships nationwide
- Filter dealerships by U.S. state
- View dealer details and customer reviews
- Submit reviews (authenticated users only)
- Sentiment analysis on reviews (positive / negative / neutral)
- User registration and login
- Admin panel for managing car makes, models, dealers, and reviews

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/djangoapp/login` | Login user |
| GET  | `/djangoapp/logout` | Logout user |
| POST | `/djangoapp/register` | Register new user |
| GET  | `/djangoapp/get_dealers` | Get all dealers |
| GET  | `/djangoapp/get_dealers/<state>` | Get dealers by state |
| GET  | `/djangoapp/dealer/<id>` | Get dealer by ID |
| GET  | `/djangoapp/reviews/dealer/<id>` | Get reviews for a dealer |
| POST | `/djangoapp/add_review` | Post a new review |
| GET  | `/djangoapp/get_cars` | Get all car makes and models |
| GET  | `/djangoapp/analyze_review/<text>` | Analyze review sentiment |

---

## Local Setup

```bash
# 1. Clone the repo
git clone https://github.com/ommore4342/car_delearship.git
cd car_delearship/server

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run migrations and seed data
python manage.py migrate
python manage.py seed_data

# 4. Create superuser (optional)
python manage.py createsuperuser

# 5. Start the server
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser.

---

## Docker (All Services)

```bash
docker-compose up --build
```

---

## Live Deployment

Deployed on **Render**. See [`submission_outputs/deploymentURL`](./submission_outputs/deploymentURL) for the live URL.

---

## Author

**ommore4342** — [https://github.com/ommore4342](https://github.com/ommore4342)
