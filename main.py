from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, text
from typing import List, Dict

app = FastAPI()

# -----------------------------
# CORS Settings
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 🔥 Open for testing, later restrict for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Database Configuration
# -----------------------------
DB_USER = "tejaswini"                        # AlwaysData MySQL username
DB_PASS = "teju1919"                         # AlwaysData MySQL password
DB_HOST = "mysql-tejaswini.alwaysdata.net"   # Host from AlwaysData
DB_NAME = "tejaswini_hi"                     # ⚡ USE THE DB NAME from AlwaysData panel (not the .sql file name!)

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# -----------------------------
# Helper Function to Fetch Table Data
# -----------------------------
def fetch_table(table_name: str) -> List[Dict]:
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT * FROM {table_name}"))
        data = [dict(row._mapping) for row in result]
    return data

# -----------------------------
# API Endpoints
# -----------------------------
@app.get("/")
def root():
    return {"message": "E-commerce API is running"}

@app.get("/Users")
def get_customers():
    return fetch_table("Users")

@app.get("/Products")
def get_products():
    return fetch_table("Products")

@app.get("/Orders")
def get_orders():
    return fetch_table("Orders")

@app.get("/Order_items")
def get_order_items():
    return fetch_table("Order_items")

@app.get("/Categories")
def get_categories():
    return fetch_table("Categories")

@app.get("/Payments")
def get_payments():
    return fetch_table("Payments")

@app.get("/Shipments")
def get_shipments():
    return fetch_table("Shipments")

@app.get("/Reviews")
def get_reviews():
    return fetch_table("Reviews")