
# E-Commerce Platform (Django + React)

A full-stack e-commerce application built using Django REST Framework for the backend and React with Redux for the frontend. It includes authentication, product catalog management, cart functionality, real-time notifications, caching, and order processing.

## Tech Stack Used

<p>
  <img src="https://img.shields.io/badge/-Django%20REST%20Framework-grey?style=flat&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/-PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white"/>
  <img src="https://img.shields.io/badge/-React-20232A?style=flat&logo=react&logoColor=61DAFB"/>
  <img src="https://img.shields.io/badge/-Redux-764ABC?style=flat&logo=redux&logoColor=white"/>
  <img src="https://img.shields.io/badge/-Material--UI-0081CB?style=flat&logo=mui&logoColor=white"/>
  <img src="https://img.shields.io/badge/-Redis-DC382D?style=flat&logo=redis&logoColor=white"/>
  <img src="https://img.shields.io/badge/-Axios-5A29E4?style=flat&logo=axios&logoColor=white"/>
</p>

## Features

- JWT authentication for users
- User registration, login, and profile management
- Product catalog with filtering and pagination
- Admin-only product and category management
- Shopping cart and order placement
- Order status tracking: Pending → Shipped → Delivered
- Real-time order status updates via WebSockets (Django Channels)
- Redis-based caching for optimized performance

## Prerequisites

- [Python 3.9+](https://www.python.org/downloads/)
- [Node.js 16+](https://nodejs.org/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Redis](https://redis.io/docs/getting-started/installation/)
- [Git](https://git-scm.com/downloads)

## Project Structure

```
ecommerce-project/
├── ecommerce/                      # Django backend root
│   ├── ecommerce/                  # Django project config
│   ├── ecommerce-frontend/         # React frontend
│   │   ├── public/                 # Static assets
│   │   └── src/                    # React source code
│   ├── orders/                     # Orders app
│   ├── products/                   # Products app
│   ├── users/                      # Users app
│   ├── .env                        # Environment variables for backend
│   ├── manage.py                   # Django management script
│   └── requirements.txt            # Python dependencies
└── venv/                           # Python virtual environment (optional)
```

## Setup Instructions

### 1. Backend Setup (Django)

```powershell
cd ecommerce-project/ecommerce
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
notepad .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### 2. Frontend Setup (React)

```powershell
cd ecommerce-frontend
npm install
copy .env.example .env
notepad .env
npm start
```

## Environment Configuration

### Backend (`.env`)

```
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=ecommerce
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
REDIS_URL=redis://localhost:6379/0
```

### Frontend (`.env`)

```
REACT_APP_API_URL=http://localhost:8000/api
```

## Running the Project

```powershell
# Start backend
cd ecommerce-project/ecommerce
python manage.py runserver

# Start frontend
cd ecommerce-project/ecommerce/ecommerce-frontend
npm start
```

- Frontend: http://localhost:3000
- Admin Panel: http://localhost:8000/admin
- API Base: http://localhost:8000/api/

## Deployment

### Backend

- Set `DEBUG=False` in `.env`
- Use Gunicorn with Nginx or host on Render/VPS
- Run `python manage.py collectstatic`

### Frontend

```bash
npm run build
```

- Deploy the `build/` directory to Vercel or Netlify

## Troubleshooting

- Ensure PostgreSQL and Redis services are running
- Validate environment variables and ports
- Rerun migrations if DB schema changes

## License

This project is licensed under the MIT License.
