# 🍽️ Advanced Restaurant Menu Validation with Pydantic v2

> **A Python project demonstrating robust data validation, schema modeling, and JSON serialization using Pydantic v2.**

<p align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-v2-E92063?style=for-the-badge)
![JSON](https://img.shields.io/badge/JSON-Data-yellow?style=for-the-badge&logo=json)
![Validation](https://img.shields.io/badge/Data-Validation-success?style=for-the-badge)

</p>

---

# 📖 Overview

This project demonstrates how to build **type-safe and reliable data models** using **Pydantic v2**.

A restaurant menu stored in JSON format is validated against predefined schemas to ensure data consistency and integrity. The project highlights advanced Pydantic features such as nested models, field validators, computed fields, email validation, automatic date parsing, strict type checking, and serialization.

Several intentionally invalid records are included in the dataset to demonstrate how Pydantic automatically detects validation errors before data reaches the application.

---

# ✨ Features

- 🍽️ Restaurant Menu Validation
- ✅ Nested Pydantic Models
- ✅ Field Validators
- 📧 Email Validation (`EmailStr`)
- 📅 Date Parsing & Validation
- 🧮 Computed Fields (Price + Tax)
- 🔒 Strict Type Checking
- 📤 Dictionary Serialization
- 📦 JSON Serialization
- ❌ Automatic Detection of Invalid Records

---

# 📂 Project Structure

```text
Restaurant-Menu-Pydantic/
│
├── work.py
├── work.json
├── requirements.txt
└── README.md
```

---

# 📊 Dataset

The project validates restaurant menu items with the following attributes:

- Item ID
- Item Name
- Price
- Category
- Availability
- Description
- Chef Email
- Date Added

The dataset also contains intentionally invalid entries such as:

- Negative prices
- Short item names
- Invalid category values
- Incorrect data types
- Invalid email formats
- Incorrect date formats

These examples help demonstrate Pydantic's validation capabilities.

---

# 🧠 Pydantic Concepts Demonstrated

## 🏗 Nested Models

Reusable `Category` schema for validating menu categories.

---

## ✅ Field Validators

Custom validation and preprocessing for:

- Category conversion
- Name formatting

---

## 📧 Email Validation

Ensures every menu item contains a valid email address using `EmailStr`.

---

## 📅 Date Validation

Automatically parses and validates ISO-formatted dates.

---

## 🧮 Computed Fields

Calculates the final price including a 5% tax without storing additional data.

---

## ⚙️ ConfigDict Features

- Strict Type Checking
- Frozen Models
- Assignment Validation
- Extra Field Handling

---

# ⚙️ Technologies Used

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
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install pydantic[email]
```

---

## Run the Project

```bash
python work.py
```

The script validates menu records, formats data, computes additional fields, and serializes the validated model into dictionary and JSON formats.

---

# 🔄 Workflow

```text
Restaurant Menu JSON
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
Email & Date Validation
          │
          ▼
Nested Model Validation
          │
          ▼
Computed Fields
          │
          ▼
Dictionary / JSON Serialization
          │
          ▼
Validated Output
```

---

# 📚 Key Concepts

- BaseModel
- Field
- field_validator
- computed_field
- ConfigDict
- Nested Models
- EmailStr
- Date Validation
- Strict Mode
- Serialization
- JSON Validation

---

# 🎯 Skills Demonstrated

- Python Programming
- Data Validation
- Schema Design
- JSON Processing
- Type Safety
- Object Serialization
- Backend Data Modeling
- Pydantic v2

---

# 📦 requirements.txt

```text
pydantic>=2.0
email-validator>=2.0
```

---

# 🚀 Future Improvements

- FastAPI Integration
- REST API Validation
- Database Connectivity
- CRUD Operations
- User Authentication
- Unit Testing
- Docker Support

---

# 👨‍💻 Author

**Ayushmaan Gupta**

B.Tech CSE (Artificial Intelligence & Machine Learning)

---

# ⭐ Support

If you found this project useful:

- ⭐ Star this repository
- 🍴 Fork this repository
- 🤝 Contribute with improvements

---

# 📜 License

This project is licensed under the **MIT License**.

---

<div align="center">

### 🍽️ Built with Python & Pydantic v2

**"Reliable applications begin with reliable data."**

</div>
