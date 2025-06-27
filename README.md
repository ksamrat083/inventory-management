# 📦 Inventory Management System

A simple inventory management system built with **Flask**, **SQLAlchemy**, and **SQLite**. This application allows you to manage products, categories, and suppliers with full CRUD (Create, Read, Update, Delete) functionality.

---

## 🚀 Features

- Add, view, update, and delete products
- Categorize products and manage suppliers
- RESTful API built with Flask Blueprints
- SQLite as the backend database
- Database migrations with Flask-Migrate

---

## 📂 Project Structure

inventory-management/
├── app/
│ ├── init.py
│ ├── models.py
│ ├── routes/
│ │ ├── products.py
│ │ └── categories.py
├── migrations/
├── instance/
│ └── inventory.db
├── run.py
├── requirements.txt
├── .gitignore
└── README.md


---

## ⚙️ Setup Instructions

### 1. Clone the Repository
git clone https://github.com/your-username/inventory-management.git
cd inventory-management

### 2. Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

### 3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt

### 4. Initialize the Database
bash
Copy
Edit
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

### 5. Run the Server
bash
Copy
Edit
flask run
Visit: http://127.0.0.1:5000

📬 API Endpoints
### Products
GET /products/ – List all products

GET /products/<id> – Get product by ID

POST /products/ – Create a new product

PUT /products/<id> – Update a product

DELETE /products/<id> – Delete a product

### Categories
GET /categories/ – List all categories

POST /categories/ – Create a new category

PUT /categories/<id> – Update category

DELETE /categories/<id> – Delete category

🛠 Technologies Used
Python

Flask

Flask SQLAlchemy

Flask-Migrate

SQLite

🙌 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

📝 License
MIT

📧 Contact
Created by @your-username – feel free to reach out!

---
