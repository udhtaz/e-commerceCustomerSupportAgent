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

---

## **🖥️ Tech Stack**
- **Backend:** FastAPI, LangChain, SQLite, Python  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** SQLite (Auto-Generated Sample Orders)  
- **API:** REST API with FastAPI  

---

## **🛠️ Installation Guide**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/udhtaz/e-commerceCustomerSupportAgent.git
cd e-commerceCustomerSupportAgent
```

### **2️⃣ Set Up Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Run the Application**
```sh
python main.py
```
🎯 **Server will start on:** `http://127.0.0.1:8000`

📚 **you can access the Swagger documentation also on:** `http://127.0.0.1:8000//docs`

---

## **📂 Project Structure**
```
e-commerce-chatbot/
│── agents/
│   ├── conversation_agent.py      # Defines AI-based chatbot logic
│── data/
│   ├── orders.db                  # SQLite database for order tracking
│   ├── contact_info.csv           # CSV storing customer names, email and phone number
│── static/
│   ├── styles.css                 # Stylesheet for frontend
│   ├── script.js                  # JavaScript for chat interaction
│   ├── webbackgroundimage.png     # Background image for UI
│── templates/
│   ├── index.html                 # Frontend HTML
│── main.py                        # FastAPI backend and endpoints
│── .env                           # Store environmental variables like your OpenAI API key
│── setup_db.py                    # Database setup script (runs on startup)
│── schemas.py                     # Defines API request schema
│── README.md                      # Documentation
│── requirements.txt               # Python dependencies
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

## **📜 License**
This project is licensed under the **Apache License**.

---

## **⏳ Future Improvements**
- ✅ **User Authentication:** Secure order tracking with login functionality.  
- ✅ **Multi-Language Support:** Support for different languages for diverse users.  
- ✅ **Live Agent Chat Integration:** A real-time connection to human agents when needed.  

👨🏾‍💻 **Developed by:** Taiwo (Udhtaz) | 💡 **Powered by FastAPI, OpenAI & LangChain**
