
# Django Blog Application with DRF API

This is a **Django blog application** that provides a platform to create, update, delete, and interact with blog posts and comments. It also includes a **RESTful API** using Django REST Framework (DRF) for programmatic CRUD operations.

---

## Features

### Web Application
1. **Post Management**:
   - List all posts.
   - View post details with associated comments.
   - Create, edit, and delete posts.

2. **Comment Management**:
   - Add, edit, and delete comments for a specific post.

3. **Rich Text Editing**:
   - Includes **Django Summernote** for rich text post content.

### RESTful API
1. **Post API**:
   - List, create, retrieve, update, and delete posts.
   - Supports filtering, searching, and ordering.

2. **Comment API**:
   - Extendable for comment management via DRF.

### Documentation
- Includes **Swagger** and **ReDoc** for API documentation with **drf-yasg**.

---

## Technologies Used

- **Django**: Web framework for backend.
- **Django REST Framework**: For building APIs.
- **SQLite**: Default database (can be configured for PostgreSQL, MySQL, etc.).
- **Django Summernote**: Rich text editor for posts.
- **drf-yasg**: Interactive API documentation.
- **Django Filters**: For advanced filtering options in APIs.

---

## Setup Instructions

### Prerequisites
- Python >= 3.8
- Django >= 4.x
- Install `pip` for Python package management.

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   - Web app: `http://127.0.0.1:8000/`
   - Swagger API: `http://127.0.0.1:8000/swagger/`

---

## Endpoints

### Web App URLs

| URL Pattern                       | View (FBVs & CBVs)      | Description                  |
|-----------------------------------|-------------------------|------------------------------|
| `/posts/`                         | `post_list` (FBV)       | List all posts              |
| `/posts/<int:pk>/`                | `post_detail` (FBV)     | View post details           |
| `/add_post/`                      | `creat_post` (FBV)      | Add a new post              |
| `/edit_post/<int:pk>/`            | `edit_post` (FBV)       | Edit an existing post       |
| `/delete_post/<int:pk>/`          | `delete_post` (FBV)     | Delete a specific post      |
| `/posts/<int:post_pk>/<int:comment_pk>/` | `comment_edit` (FBV) | Edit a comment              |
| `/posts/<int:post_pk>/<int:comment_pk>/delete/` | `comment_delete` (FBV) | Delete a comment            |

### API Endpoints

| Method | Endpoint                   | Description                  |
|--------|----------------------------|------------------------------|
| GET    | `/posts/api/`              | List all posts               |
| POST   | `/posts/api/`              | Create a new post            |
| GET    | `/posts/api/<int:pk>/`     | Retrieve post details        |
| PUT    | `/posts/api/<int:pk>/`     | Update a specific post       |
| DELETE | `/posts/api/<int:pk>/`     | Delete a specific post       |

---

## Directory Structure

```
project/
│
├── posts/
│   ├── views.py         # Function-based views
│   ├── views2.py        # Class-based views
│   ├── api.py           # DRF API views
│   ├── models.py        # Post and Comment models
│   ├── serializers.py   # DRF serializers for APIs
│   ├── urls.py          # App-specific URL patterns
│   ├── templates/       # HTML templates for the app
│   └── forms.py         # Forms for posts and comments
│
├── manage.py            # Django management script
├── settings.py          # Project settings
└── urls.py              # Project-level URL patterns
```

---

## API Documentation

The project includes interactive API documentation via **Swagger** and **ReDoc**:

- **Swagger UI**: `/swagger/`
- **ReDoc UI**: `/redoc/`
- **Raw Schema**: `/swagger.json` or `/swagger.yaml`

---

## Contribution Guidelines

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.
