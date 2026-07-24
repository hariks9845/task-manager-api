# 📋 Task Manager API

A high-performance RESTful API built with **Django REST Framework (DRF)** featuring **JWT Authentication**, custom **Priority-Based Task Scheduling using a Min-Heap Data Structure**, and fully automated testing via **GitHub Actions CI/CD**.

---

## ✨ Features

- **🔐 Token-Based Authentication**: Secure endpoints protected with JSON Web Tokens (JWT via `djangorestframework-simplejwt`).
- **⚡ Min-Heap Scheduling Engine**: Custom priority queue algorithm ($O(N \log N)$ complexity) that dynamically sequences user tasks by priority level and due date.
- **📂 Category & Task Management**: Complete CRUD operations with relational data mapping and ownership isolation per user.
- **🔄 CI/CD Pipeline**: Automated unit testing and build verification on every commit via GitHub Actions.

---

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **Framework**: Django & Django REST Framework
- **Authentication**: SimpleJWT
- **Data Structures**: Min-Heap (`heapq`) for priority queuing
- **CI/CD**: GitHub Actions
- **Database**: SQLite (Development) / PostgreSQL-ready

---

## 🚦 Getting Started

### Prerequisites

- Python 3.10+
- `pip` package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/hariks9845/task-manager-api.git](https://github.com/hariks9845/task-manager-api.git)
   cd task-manager-api
