# NextDoor API

Backend for a location-aware house rental platform. Tenants find rental listings near them, view photos and details, then contact the landlord directly by WhatsApp or phone, no middleman.

Built with FastAPI, deployed on Render, backed by PostgreSQL on Neon.

Live API docs: https://nextdoor-grf8.onrender.com/docs

## What it does

Landlords and tenants sign up under different roles with role-based permissions. Landlords post listings with photos (stored on Cloudinary) and details. Tenants search by proximity to find houses near their current location, open a listing to see full details, and get the landlord's contact info directly, so the actual negotiation happens off-platform, the way house hunting usually works here.

## Stack

FastAPI, PostgreSQL, SQLAlchemy, Cloudinary for image storage, JWT auth, role-based access control. Deployed on Render with Neon for the database.

## API overview

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register as a tenant or landlord |
| POST | `/auth/login` | Login and receive a JWT token |
| POST | `/houses` | List a new rental property (landlord) |
| GET | `/houses/nearby` | Find houses near current location (tenant) |
| GET | `/houses/{id}` | View full details of a listing |
| PUT | `/houses/{id}` | Update a listing (landlord only) |
| DELETE | `/houses/{id}` | Remove a listing (landlord only) |
| GET | `/houses/{id}/contact` | Get landlord contact details |

Full interactive docs are at the live link above.

## Running locally

```bash
git clone https://github.com/b100mBUG/nextdoor.git
cd nextdoor
pip install -r requirements.txt
cp .env.example .env
# fill in DATABASE_URL, SECRET_KEY, CLOUDINARY_URL
uvicorn main:app --reload
```

## Environment variables

| Variable | Description |
|----------|--------------|
| `DATABASE_URL` | PostgreSQL connection string (Neon) |
| `SECRET_KEY` | JWT signing secret |
| `CLOUDINARY_URL` | Cloudinary API URL for image uploads |

## Author

Were Fidel Castro. [GitHub](https://github.com/b100mBUG). [Portfolio](https://werefidelcastro.onrender.com).