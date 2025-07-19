
# E-Commerce Platform (Django + React)

A full-stack e-commerce application built using Django REST Framework for the backend and React with Redux for the frontend. It includes authentication, product catalog management, cart functionality, and order processing.

## Tech Stack Used

<img src="https://img.shields.io/badge/-Django%20REST%20Framework-grey?style=flat&logo=django&logoColor=white"/>
<img src="https://img.shields.io/badge/-PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white"/>
<img src="https://img.shields.io/badge/-React-20232A?style=flat&logo=react&logoColor=61DAFB"/>
<img src="https://img.shields.io/badge/-Redux-764ABC?style=flat&logo=redux&logoColor=white"/>
<img src="https://img.shields.io/badge/-Material--UI-0081CB?style=flat&logo=mui&logoColor=white"/>
<img src="https://img.shields.io/badge/-Redis-DC382D?style=flat&logo=redis&logoColor=white"/>
<img src="https://img.shields.io/badge/-Axios-5A29E4?style=flat&logo=axios&logoColor=white"/>

## Features

- User authentication with JWT
- Product catalog with category filtering
- Shopping cart and order placement
- Admin dashboard for managing products and orders
- Redis caching support
- Responsive frontend with React and Material-UI

## Prerequisites

Make sure you have the following installed on your system:

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
# Navigate to the backend directory
cd ecommerce-project/ecommerce

# Create and activate virtual environment (Windows)
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
copy .env.example .env
notepad .env

# Apply migrations and create superuser
python manage.py migrate
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```

### 2. Frontend Setup (React)

```powershell
# Navigate to the React frontend directory
cd ecommerce-frontend

# Install dependencies
npm install

# Create and configure environment variables
copy .env.example .env
notepad .env

# Start the frontend development server
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

1. Start the backend server:

```powershell
cd ecommerce-project/ecommerce
python manage.py runserver
```

2. Start the frontend server:

```powershell
cd ecommerce-project/ecommerce/ecommerce-frontend
npm start
```

3. Access the application at:

- Frontend: http://localhost:3000
- Admin Panel: http://localhost:8000/admin
- API Base: http://localhost:8000/api/

## Deployment

### Backend

- Set `DEBUG=False` in `.env`
- Use Gunicorn with Nginx or host on services like PythonAnywhere or Render
- Run `python manage.py collectstatic` before deploying

### Frontend

```bash
npm run build
```

- Deploy the contents of the `build/` folder to a static host like Netlify or Vercel

## Troubleshooting

1. Ensure PostgreSQL and Redis are running correctly.
2. Double-check environment variables in both backend and frontend `.env` files.
3. Run migrations again if database changes are made.

## License

This project is licensed under the MIT License.
