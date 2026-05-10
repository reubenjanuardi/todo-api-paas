# Todo API PaaS AWS

REST API sederhana berbasis Flask yang dideploy menggunakan AWS Elastic Beanstalk dan menggunakan PostgreSQL AWS RDS sebagai managed database service.

## Deskripsi Proyek

Project ini merupakan implementasi Platform as a Service (PaaS) menggunakan AWS Elastic Beanstalk sebagai platform deployment aplikasi dan AWS RDS PostgreSQL sebagai layanan database cloud.

Aplikasi menyediakan layanan REST API untuk manajemen tugas (to-do list) yang mendukung operasi CRUD (Create, Read, Update, Delete).

## Teknologi yang Digunakan

| Teknologi             | Fungsi                     |
| --------------------- | -------------------------- |
| Python 3.11           | Bahasa pemrograman utama   |
| Flask                 | Framework backend REST API |
| Flask SQLAlchemy      | ORM database               |
| PostgreSQL            | Database relational        |
| AWS RDS               | Managed database service   |
| AWS Elastic Beanstalk | Platform deployment PaaS   |
| Gunicorn              | WSGI production server     |
| Git & GitHub          | Version control            |

---

# Arsitektur Sistem

```mermaid
flowchart TD
    A[Client / Postman / Browser] --> B[Flask REST API]
    B --> C[AWS Elastic Beanstalk]
    C --> D[Gunicorn Application Server]
    D --> E[Flask Application]
    E --> F[AWS RDS PostgreSQL]
```

---

# MermaidJS Diagram

```mermaid
flowchart TD
  A[User] --> B{Endpoint Dipilih}

  B -->|GET /| C[Info API]
  B -->|GET /health| D[Status Kesehatan]
  B -->|GET /tasks| E[Ambil Semua Task]
  B -->|POST /tasks| F[Tambah Task Baru]
  B -->|PUT /tasks/id| G[Perbarui Task]
  B -->|DELETE /tasks/id| H[Hapus Task]

  F --> I[Simpan ke PostgreSQL]
    G --> I
    H --> I

    I --> J[Response JSON]
```

---

# Sequence Diagram

```mermaid
sequenceDiagram
    participant User
    participant FlaskAPI
    participant PostgreSQL

    User->>FlaskAPI: POST /tasks
    FlaskAPI->>PostgreSQL: INSERT task
    PostgreSQL-->>FlaskAPI: Data berhasil disimpan
    FlaskAPI-->>User: Response JSON sukses

    User->>FlaskAPI: GET /tasks
    FlaskAPI->>PostgreSQL: SELECT * FROM tasks
    PostgreSQL-->>FlaskAPI: Data task
    FlaskAPI-->>User: List task JSON
```

---

# Struktur Folder

```text
TODO-API-PAAS/
│
├── app.py
├── application.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── .gitignore
├── .env
└── README.md
```

---

# Endpoint API

## 1. Home Endpoint

### Request

```http
GET /
```

### Response

```json
{
  "message": "Todo API PaaS Running",
  "version": "1.0.0"
}
```

---

## 2. Health Check Endpoint

### Request

```http
GET /health
```

### Response

```json
{
  "status": "healthy"
}
```

---

## 3. Get All Tasks

### Request

```http
GET /tasks
```

### Response

```json
[
  {
    "id": 1,
    "title": "Belajar AWS",
    "description": "Deploy Flask API",
    "status": "pending"
  }
]
```

---

## 4. Create Task

### Request

```http
POST /tasks
```

### Body

```json
{
  "title": "Belajar PaaS",
  "description": "Deploy aplikasi Flask"
}
```

### Response

```json
{
  "message": "Task created successfully"
}
```

---

## 5. Update Task

### Request

```http
PUT /tasks/1
```

### Body

```json
{
  "status": "completed"
}
```

### Response

```json
{
  "message": "Task updated successfully"
}
```

---

## 6. Delete Task

### Request

```http
DELETE /tasks/1
```

### Response

```json
{
  "message": "Task deleted successfully"
}
```

---

# Cara Menjalankan Project Secara Lokal

## 1. Clone Repository

```bash
git clone https://github.com/USERNAME/todo-api-paas.git
cd todo-api-paas
```

## 2. Membuat Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependency

```bash
pip install -r requirements.txt
```

---

## 4. Konfigurasi Environment Variable

Buat file `.env`

```env
SECRET_KEY=your_secret_key
DATABASE_URL=postgresql://postgres:password@host:5432/postgres
```

---

## 5. Jalankan Aplikasi

```bash
python app.py
```

Aplikasi berjalan di:

```text
http://localhost:5000
```

---

# Deployment AWS Elastic Beanstalk

## Inisialisasi Elastic Beanstalk

```bash
eb init
```

## Membuat Environment

```bash
eb create todo-api-env
```

## Deploy Aplikasi

```bash
eb deploy
```

## Membuka Aplikasi

```bash
eb open
```

---

# Environment Variables

| Variable     | Fungsi                     |
| ------------ | -------------------------- |
| SECRET_KEY   | Secret key Flask           |
| DATABASE_URL | Koneksi PostgreSQL AWS RDS |

---

# Pengujian API

Pengujian dilakukan menggunakan:

- Postman
- Browser
- Curl

Semua endpoint berhasil diuji dengan status sukses.

---

# Keunggulan Implementasi

- Menggunakan konsep Platform as a Service (PaaS)
- Deployment cloud berbasis AWS Elastic Beanstalk
- Managed database menggunakan AWS RDS PostgreSQL
- Konfigurasi aman menggunakan environment variable
- Mendukung operasi CRUD lengkap
- Skalabilitas cloud bawaan AWS

---

# Repository

Tambahkan link repository GitHub di sini:

```text
https://github.com/USERNAME/todo-api-paas
```

---

# Deployment URL

Tambahkan link deployment Elastic Beanstalk di sini:

```text
http://your-app.ap-southeast-2.elasticbeanstalk.com
```

---

# Author

**Stevy Reuben Januardi**  
S1 Sistem Informasi  
Telkom University
