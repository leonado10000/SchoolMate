<p align="center">
  <img src="static/demo.gif" alt="SchoolMate Demo" width="100%" />
</p>

<p align="center">
  <b>Manage students. Structure data. Generate insights.</b><br>
  A modern Django-powered system built for real-world academic workflows.
</p>

<p align="center">
  <a href="https://github.com/leonado10000/SchoolMate"><img src="https://img.shields.io/badge/Repo-Active-black?style=for-the-badge&logo=github"></a>
  <a href="https://www.kaggle.com/datasets/leonado10000/students-data"><img src="https://img.shields.io/badge/Dataset-Kaggle-blue?style=for-the-badge&logo=kaggle"></a>
  <a href="https://rahul-jangra-leonado10000.vercel.app/"><img src="https://img.shields.io/badge/Portfolio-Live-green?style=for-the-badge"></a>
</p>

---

## 🧠 Overview

**SchoolMate** is a full-stack school management system designed to:

- Centralize student data
- Simplify administrative workflows
- Generate structured datasets for analysis

This is not just CRUD — it's a **data-backed system** that connects application design with real-world data usage.

---

## ✨ Core Capabilities

### 🧑‍🎓 Student Lifecycle Management
- Create, update, and manage student profiles
- Store academic + personal details
- Structured and scalable schema

### 🏫 Batch & Class Organization
- Assign students to classes dynamically
- Maintain hierarchical structure

### 📊 Data-Driven Design
- Generates real dataset used on Kaggle
- Enables ML / analytics workflows

### ⚡ Admin-Focused UX
- Minimal friction UI
- Fast data entry + retrieval
- Designed for operational efficiency

---

## 📸 Interface Preview

<p align="center">
  <img src="https://raw.githubusercontent.com/leonado10000/SchoolMate/refs/heads/master/static/er_light.png">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/leonado10000/SchoolMate/refs/heads/master/static/er_dark.png">
</p>

> Images are sourced from `/static/` — update filenames if needed.

---

## 🏗️ Tech Architecture

| Layer        | Technology |
|-------------|-----------|
| Backend     | Django (Python) |
| Frontend    | HTML, CSS, Bootstrap |
| Database    | SQLite (default) |
| Data Layer  | Kaggle dataset integration |

---

## ⚙️ Local Setup

```bash id="setup-2026"
git clone https://github.com/leonado10000/SchoolMate.git

cd SchoolMate

python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
