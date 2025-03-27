# **🛒 E-Commerce Customer Support Conversational Agent**

## **📌 Overview**
The **E-Commerce Customer Support Conversational Agent** is an AI-powered assistant designed to **handle customer support queries** for an e-commerce platform. It provides **real-time responses** to inquiries regarding:
- 📦 **Order Status Tracking**  
- 🔄 **Return Policies**  
- 👨‍💼 **Escalation to Human Representatives**  

The chatbot uses **LangChain** to manage **multi-turn conversations** and integrate with a **SQLite database** for order information retrieval.

---

https://github.com/user-attachments/assets/f1c240ae-6a90-49ef-be54-1cbbd33e8879

---

## **⚙️ Features**
✅ **AI-Powered Chatbot:** Handles queries related to orders, returns, and support requests.  
✅ **Real-time Order Tracking:** Users can provide order IDs to check their shipment status.  
✅ **Return Policy Lookup:** Determines if an item is returnable based on predefined rules.  
✅ **Human Representative Escalation:** Transfers users to a support agent if needed.  
✅ **Dark Mode & Theme Toggle:** Users can switch between light and dark themes.  
✅ **Database Integration:** Stores order details in **SQLite** with dynamic data generation on startup.  
✅ **Frontend UI:** Intuitive chat interface with an embedded background image for a modern e-commerce experience.  
✅ **Test Coverage & CI:** Unit-tested with coverage reporting and Docker-based testing.  
✅ **Docker & Docker Compose Support:** Run development and tests via containers.  
✅ **Modular Architecture:** Clean, scalable layout based on FastAPI best practices.  

---

## **🖥️ Tech Stack**
- **Backend:** FastAPI, LangChain, SQLite, Python  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** SQLite (Auto-Generated Sample Orders)  
- **API:** REST API with FastAPI  
- **Containerization:** Docker, Docker Compose  
- **Testing:** Pytest + Coverage  

---

## **🛠️ Installation Guide**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/udhtaz/e-commerceCustomerSupportAgent.git
cd e-commerceCustomerSupportAgent
```

### **2️⃣ Set Up Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Run the Application**
```bash
uvicorn app.main:app --reload
```

🎯 **Server will start on:** `http://127.0.0.1:8000`  
📚 **Swagger documentation:** `http://127.0.0.1:8000/docs`

---

## **📂 Project Structure**
```
e-commerceCustomerSupportAgent/
├── app/
│   ├── agents/                   # LangChain agent setup
│   ├── api/
│   │   ├── routes/              # Chat, Orders, Pages endpoints
│   │   └── schemas/             # Pydantic models
│   ├── config.py                # App settings (env-based)
│   ├── core/
│   │   ├── assets.py            # Static files mount
│   │   ├── templates.py         # Jinja2 template loader
│   │   ├── exceptions.py        # Custom exception handlers
│   │   └── logging.py           # Logging config
│   ├── domain/                  # Business models and policies
│   ├── infrastructure/         # Database & CSV repositories
│   ├── services/               # Tool service layer
│   ├── use_cases/              # Application logic (track orders, escalate, return policies)
│   ├── static/                 # Frontend assets (JS, CSS)
│   ├── templates/              # index.html UI
│   ├── setup_db.py             # Auto-create database and sample orders
│   └── main.py                 # App entry point
├── data/                       # Orders database and contact CSV
├── migrations/                 # Alembic migrations
├── tests/                      # Unit & integration tests
├── Dockerfile
├── docker-compose.yml
├── docker-compose.test.yml
├── run_test_coverage.sh
├── requirements.txt
├── .env
├── .coveragerc
└── README.md
```

---

## 🏗️ **System Architecture Overview**

                                            ┌──────────────────────--─┐
                                            │    Browser / Client     │
                                            └────────────┬────────────┘
                                                         │
                                                         ▼
                                         ┌────────────────────────────────┐
                                         │ Frontend (HTML / CSS / JS)     │
                                         └────────────┬───────────────────┘
                                                      │
                                                      ▼
                                       ┌────────────────────────────────────┐
                                       │ FastAPI App (Chat + API Endpoints) │
                                       └────────────┬────────────┬──────────┘
                                                    │            │
                                                    ▼            ▼
                        ┌──────────────────────────────┐   ┌────────────────────────┐
                        │ LangChain Agent + Tools      │   │ CSV File for Contacts  │ 
                        │ (OrderTool, PolicyTool, etc) │   │ (Escalation to Human)  │
                        └────────────┬─────────────────┘   └────────────────────────┘
                                     │
                                     ▼
                            ┌─────────────────────┐
                            │   SQLite Database   │
                            │  (Order Info, etc)  │
                            └─────────────────────┘

**🔁 Flow Summary:**
```
User Input ──> /chat ──> LangChain Agent
                        ├─> Calls Tool (e.g., OrderStatusTool)
                        ├─> Tool read/write from SQLite/CSV
                        └─> Tool Output ──> Final Answer ──> JSON API Response
```
---

## **🛠️ API Endpoints**

### **1️⃣ Chat Endpoint**
🔹 **Send a message to the chatbot**  
**`POST /chat`**  
```json
{
  "message": "Where is my order?"
}
```
📌 **Response:**
```json
{
  "response": {
    "output": "Please provide your order ID so I can check the status for you."
  }
}
```

### **2️⃣ Get All Orders**
🔹 **Fetch all order data from the database**  
**`GET /orders`**  
📌 **Response:**
```json
[
  {
    "order_id": "10001",
    "item": "Laptop",
    "purchase_date": "2025-02-01",
    "status": "Shipped",
    "shipped_date": "2025-02-10",
    "delivery_date": "N/A",
    "payment_method": "Card",
    "return_policy": "Returnable"
  },
  ...
]
```

---

## **🎨 Frontend UI**
The chatbot interface is built with **HTML, CSS, and JavaScript** and features:
- **A modern e-commerce background** 🎨
- **A chat bubble UI for messages** 💬
- **Typing indicator for a realistic chat experience** ⏳
- **A dark mode toggle for better accessibility** 🌙☀️

---

## **🧪 Tests & Coverage**

Run tests using:

```bash
pytest --cov=app tests/
```

Or via Docker Compose:

```bash
bash run_test_coverage.sh
```

🧪 **Includes:**  
- Unit tests for endpoints  
- Coverage reports  
- CI-ready Docker Compose test setup

![Coverage](https://img.shields.io/badge/Coverage-75%25-brightgreen)

---

## **🐳 Docker Support**

### Run Locally with Docker
```bash
docker build -t conversational_agent:1.00 .
docker run -p 8000:8000 conversational_agent:1.00
```

### Test Coverage in Container
```bash
docker-compose -f docker-compose.test.yml up --build
```

---

## **📜 License**
This project is licensed under the **Apache License**.

---

## **⏳ Future Improvements**
- ✅ **User Authentication:** Secure order tracking with login functionality  
- ✅ **Multi-Language Support:** Support for different languages  
- ✅ **Live Agent Chat Integration:** A real-time connection to human agents when needed  

👨🏾‍💻 **Developed by:** Taiwo (Udhtaz)  
💡 **Powered by FastAPI, OpenAI & LangChain**
