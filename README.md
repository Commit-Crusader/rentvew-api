# RentView API

RentView API is a **Django REST Framework** backend for a property rental platform with integrated **virtual tour support**.  
It allows landlords to list properties, tenants to explore available rentals, and both to interact through a secure authentication system.  
This project is my **ALX Backend Web Development Capstone Project**.

---

## 🚀 Features

- **User Authentication & Profiles**  
  - Register, login, logout with JWT tokens  
  - Role-based access control (`landlord` or `tenant`)  
  - User profiles with contact information  

- **Property Management**  
  - Landlords can create, update, delete their own listings  
  - Tenants can browse and search properties  
  - Soft delete to preserve data integrity  

- **Virtual Tours**  
  - Upload and manage 360° images for immersive viewing  
  - Publicly accessible property + tour details  

- **File Uploads**  
  - Property images (JPG, PNG, JPEG up to 10MB)  
  - Virtual tour images (JPG, PNG, JPEG up to 20MB)  

---

## 📦 Tech Stack

- Python 3.10+  
- Django 5+  
- Django REST Framework  
- SimpleJWT (for authentication)  
- SQLite (development) / PostgreSQL (production-ready)  

---

## ⚙️ Installation

Clone the repo:

```bash
git clone https://github.com/<your-username>/rentview-api.git
cd rentview-api

