# 💰 Expense Tracker API

A production-ready FastAPI application for tracking expenses, built with Docker support.

## 🚀 Features

- ✅ Complete CRUD operations (Create, Read, Update, Delete)
- ✅ Input validation with Pydantic
- ✅ SQLite database (easily upgradeable to PostgreSQL/SQL Server)
- ✅ Logging and error handling
- ✅ Health check endpoint
- ✅ CORS enabled
- ✅ Docker & Docker Compose ready
- ✅ Auto-generated API documentation

## 📁 Project Structure

```
expense_api/
├── app/
│   ├── __init__.py
│   ├── main.py          # Application entry point
│   ├── config.py        # Configuration management
│   ├── database.py      # Database connection
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── crud.py          # Database operations
│   └── routes/
│       └── expenses.py  # API endpoints
├── .env                 # Environment variables
├── requirements.txt     # Python dependencies
├── Dockerfile          # Docker image definition
├── docker-compose.yml  # Docker Compose config
└── README.md
```

## 🛠️ Local Development Setup

### Prerequisites
- Python 3.11+
- pip

### Installation

1. **Clone the repository**
```bash
git clone <your-repo>
cd expense_api
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Create .env file**
```bash
cp .env.example .env
# Edit .env with your settings
```

5. **Run the application**
```bash
uvicorn app.main:app --reload
```

6. **Access the API**
- API: http://localhost:8000
- Docs: http://localhost:8000/docs
- Health: http://localhost:8000/health

## 🐳 Docker Setup

### Using Docker Compose (Recommended)

1. **Build and run**
```bash
docker-compose up --build
```

2. **Run in detached mode**
```bash
docker-compose up -d
```

3. **View logs**
```bash
docker-compose logs -f
```

4. **Stop containers**
```bash
docker-compose down
```

### Using Docker directly

1. **Build image**
```bash
docker build -t expense-tracker-api .
```

2. **Run container**
```bash
docker run -d -p 8000:8000 --name expense-api expense-tracker-api
```

3. **Stop container**
```bash
docker stop expense-api
docker rm expense-api
```

## 📚 API Endpoints

### Base URL
- Local: `http://localhost:8000/api/v1`
- Docker: `http://localhost:8000/api/v1`

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root endpoint |
| GET | `/health` | Health check |
| POST | `/api/v1/expenses/` | Create expense |
| GET | `/api/v1/expenses/` | List all expenses |
| GET | `/api/v1/expenses/{id}` | Get expense by ID |
| PUT | `/api/v1/expenses/{id}` | Update expense |
| DELETE | `/api/v1/expenses/{id}` | Delete expense |
| GET | `/api/v1/expenses/category/{category}` | Get by category |

### Example Requests

**Create Expense**
```bash
curl -X POST "http://localhost:8000/api/v1/expenses/" \
  -H "Content-Type: application/json" \
  -d '{
    "amount": 50.00,
    "category": "Food",
    "description": "Lunch at restaurant"
  }'
```

**Get All Expenses**
```bash
curl "http://localhost:8000/api/v1/expenses/"
```

**Update Expense**
```bash
curl -X PUT "http://localhost:8000/api/v1/expenses/1" \
  -H "Content-Type: application/json" \
  -d '{
    "amount": 55.00
  }'
```

**Delete Expense**
```bash
curl -X DELETE "http://localhost:8000/api/v1/expenses/1"
```

## 🧪 Testing

Access the interactive API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 📊 Database

The application uses SQLite by default. To upgrade to SQL Server:

1. Update `DATABASE_URL` in `.env`:
```
DATABASE_URL=mssql+pyodbc://user:password@server/database?driver=ODBC+Driver+17+for+SQL+Server
```

2. Add to `requirements.txt`:
```
pyodbc==5.0.1
```

3. Rebuild Docker image

## 🔧 Configuration

Edit `.env` file:

```bash
APP_NAME=Expense Tracker API
APP_VERSION=1.0.0
DEBUG=False
DATABASE_URL=sqlite:///./expenses.db
API_PREFIX=/api/v1
CORS_ORIGINS=http://localhost:3000,http://localhost:8080
```

## 📝 Logging

Logs are configured in `app/main.py` and include:
- Request/response logging
- Error tracking
- Database operations
- Health check status

## 🚀 Production Deployment

1. Set `DEBUG=False` in `.env`
2. Use a production database (PostgreSQL/SQL Server)
3. Set up proper CORS origins
4. Use environment variables for secrets
5. Enable HTTPS
6. Set up monitoring

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

MIT License

## 👨‍💻 Author

Vilva 