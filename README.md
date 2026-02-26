# ENS Social Network - Backend API

Django REST API backend for the ENS Social Network application. Manages friendship connections between ENS identities with persistent PostgreSQL storage.

<img width="1507" height="849" alt="image" src="https://github.com/user-attachments/assets/f8fdf382-a4b2-4c8d-9bdb-bcdaec675c16" />



<img width="1501" height="831" alt="image" src="https://github.com/user-attachments/assets/2b1684a4-6a98-4d21-90c1-00be8c610f41" />



## 🌟 Features

- RESTful API for managing ENS friendships
- PostgreSQL database with Neon
- CORS-enabled for frontend integration
- Deployed on Vercel serverless functions

## 🚀 Live API

**Base URL:** https://ns-ens-backend.vercel.app  
**Endpoints:** `/api/edges/`

## 📡 API Endpoints

### Get all friendships
```http
GET /api/edges/
```
**Response:**
```json
[
  {
    "id": 1,
    "from_ens": "vitalik.eth",
    "to_ens": "balajis.eth",
    "created_at": "2026-02-26T06:20:41.408572Z"
  }
]
```

### Create friendship
```http
POST /api/edges/
Content-Type: application/json

{
  "from_ens": "vitalik.eth",
  "to_ens": "balajis.eth"
}
```

### Delete friendship
```http
DELETE /api/edges/{id}/
```

## 🛠️ Tech Stack

- Django 6.0
- Django REST Framework
- PostgreSQL (Neon)
- python-decouple (Environment variables)
- CORS Headers

## 📦 Installation
```bash
# Clone repository
git clone https://github.com/omsant02/NS_ENS_BACKEND.git
cd NS_ENS_BACKEND

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cat > .env << EOF
DATABASE_URL=your_postgresql_connection_string
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
EOF

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

## 🗄️ Database Schema

### Friendship Model
```python
class Friendship(models.Model):
    from_ens = CharField(max_length=255)
    to_ens = CharField(max_length=255)
    created_at = DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('from_ens', 'to_ens')
```

## 📝 Environment Variables
```
DATABASE_URL=postgresql://user:password@host/database
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=.vercel.app
```

## 🏗️ Project Structure
```
ens_network/
├── settings.py          # Django settings
├── urls.py             # URL routing
└── wsgi.py             # WSGI application

friendships/
├── models.py           # Friendship model
├── serializers.py      # DRF serializers
├── views.py            # API views
└── urls.py             # App URLs
```

## 🚢 Deployment

Deployed on Vercel with serverless functions.
```bash
# Deploy
git push origin main
# Vercel auto-deploys on push
```

**Configuration files:**
- `vercel.json` - Vercel deployment config
- `requirements.txt` - Python dependencies

## 🔗 Related

- Frontend Repository: https://github.com/omsant02/NS_ENS
- Live Frontend: https://ns-ens-kohl.vercel.app

## 👤 Author

**Om Santoshwar**  
GitHub: [@omsant02](https://github.com/omsant02)

## 📄 License

MIT
