# 🍽️ Restaurant Menu Validation using Pydantic v2

> **Data Validation, Serialization, and Schema Modeling with Python & Pydantic**

<p align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-v2-E92063?style=for-the-badge)
![JSON](https://img.shields.io/badge/JSON-Data-yellow?style=for-the-badge&logo=json)
![Validation](https://img.shields.io/badge/Data-Validation-success?style=for-the-badge)

</p>

---

# 📖 Overview

This project demonstrates how to use **Pydantic v2** to build robust and type-safe data models in Python.

A restaurant menu stored in JSON format is validated against predefined schemas to ensure data integrity. The project showcases field validation, model validation, computed fields, nested models, strict type checking, serialization, and configuration settings available in Pydantic.

It also demonstrates how invalid data such as negative prices, incorrect data types, and invalid category values can be detected automatically during validation.

---

# ✨ Features

- 🍽️ Restaurant Menu Validation
- ✅ Field Validation
- ✅ Model Validation
- 🧮 Computed Fields
- 🔒 Strict Type Checking
- 🏗️ Nested Pydantic Models
- 📤 JSON Serialization
- 📥 Dictionary Serialization
- ⚙️ Pydantic Configuration
- ❌ Invalid Data Detection

---

# 📂 Project Structure

```text
Restaurant-Menu-Pydantic/
│
├── model.py
├── menu.json
├── README.md
└── requirements.txt
```

---

# 📊 Dataset

The project validates a restaurant menu containing:

- Item ID
- Item Name
- Price
- Category
- Availability
- Description

Example Menu Items

- Paneer Tikka
- Butter Chicken
- Dal Makhani
- Masala Chai
- Gulab Jamun

The dataset also intentionally includes invalid records to demonstrate Pydantic's validation capabilities.

---

# 🧠 Pydantic Concepts Covered

## Field Validation

Validate individual fields such as:

- Minimum Name Length
- Positive Price
- Data Types

---

## Model Validation

Validate multiple fields together.

Example:

- Available items must have a valid positive price.

---

## Computed Fields

Automatically calculates:

```
Price + 5% Tax
```

without storing additional data.

---

## Nested Models

Restaurant Item

↓

Category Model

This demonstrates reusable schema design.

---

## Strict Validation

The project enables:

- Strict Data Types
- Assignment Validation
- Frozen Models
- Extra Field Handling

---

# 🛠 Technologies Used

- Python
- Pydantic v2
- JSON

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/your-username/Restaurant-Menu-Pydantic.git
```

```bash
cd Restaurant-Menu-Pydantic
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
```

Activate

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install pydantic
```

---

## Run the Project

```bash
python model.py
```

---

# 🔄 Workflow

```text
menu.json
      │
      ▼
Load JSON Data
      │
      ▼
Pydantic Schema
      │
      ▼
Field Validation
      │
      ▼
Model Validation
      │
      ▼
Computed Fields
      │
      ▼
Dictionary / JSON Serialization
      │
      ▼
Validation Output
```

---

# 📚 Concepts Demonstrated

- BaseModel
- Field()
- field_validator
- model_validator
- computed_field
- ConfigDict
- Nested Models
- Strict Mode
- Frozen Models
- Serialization
- JSON Validation

---

# 🎯 Skills Demonstrated

- Data Validation
- Python Programming
- Pydantic v2
- JSON Processing
- Schema Design
- Object Serialization
- Type Safety
- Backend Data Modeling

---

# 📦 requirements.txt

```text
pydantic>=2.0
```

---

# 🚀 Future Improvements

- FastAPI Integration
- REST API Validation
- Database Integration
- Menu CRUD Operations
- User Authentication
- Automatic API Documentation
- Unit Testing

---

# 👨‍💻 Author

**Ayushmaan Gupta**

🎓 B.Tech CSE (Artificial Intelligence & Machine Learning)

---

# ⭐ Support

If you found this project useful,

⭐ Star this repository

🍴 Fork this repository

📢 Share it with others

---

<div align="center">

### 🍽️ Built with Python & Pydantic

*"Validate early, build reliable applications, and let your data speak with confidence."*

</div>
