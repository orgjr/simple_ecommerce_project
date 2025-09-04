# 🛒 Django E-commerce Project

This project is a simple **e-commerce web application** built with Django.  
It provides user authentication, product management, and a shopping cart system.

---

## 📌 Features

- User registration & login (custom `Customer` model).
- Product catalog with name, description, and price.
- Shopping cart with quantity tracking.
- Orders linked to users.
- Responsive frontend with **Bootstrap 5**.

---

## 📂 Project Structure
```
simple_ecommerce_project/
│── core/ # Main application
│ ├── models.py # Database models: Customer, Product, Cart, Order
│ ├── views.py # Views: product listing, add to cart, etc.
│ ├── templates/core/ # HTML templates
│── manage.py # Django management script
│── package.json # Frontend dependencies (Bootstrap)
```

---

## ⚙️ Requirements

- Python **3.10+**
- Django **5.x**
- pipenv or virtualenv (recommended)
- Node.js (for Bootstrap via npm)

---

## 🚀 Installation & Setup

1. **Clone the repository**
   ```
   git clone https://github.com/your-username/my_project.git
   cd my_project
2. **Create a virtual environment & install dependencies**
```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install django
```
3. **Install frontend dependencies**

```
npm install
```
4. **Run database migrations**
```
python manage.py migrate
```
5. **Create a superuser**
```
python manage.py createsuperuser
```
6. **Start the development server**
```
python manage.py runserver http://127.0.0.1:8000
```
🌐 Usage
Open http://127.0.0.1:8000 to access the app.

Log in with your superuser account.

Add products via the Django Admin panel.

Test adding products to the cart.

📦 Future Improvements
Payment gateway integration.

Product images and categories.

REST API with Django REST Framework.

Docker deployment.
