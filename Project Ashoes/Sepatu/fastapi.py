from fastapi import FastAPI, HTTPException, Depends
from typing import List
from pydantic import BaseModel
import mysql.connector
from fastapi import Depends

app = FastAPI()

# Konfigurasi Koneksi Database
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'ashoes',
    'port': '3306',
}

# Fungsi Dependency untuk Mendapatkan Koneksi Database
def get_db():
    db = mysql.connector.connect(**db_config)
    try:
        yield db
    finally:
        db.close()

# Model Produk
class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    stock_quantity: int
    image_url: str 
    category_name: str


@app.get("/product/", response_model=List[Product])
def get_products(db: mysql.connector.connect = Depends(get_db)):
    cursor = db.cursor(dictionary=True)
    cursor.execute(
        """
        SELECT sp.*, k.name as category_name
        FROM sepatu_product sp
        JOIN sepatu_category k ON sp.category_id = k.id
        """
    )
    products = cursor.fetchall()
    return products


@app.get("/product/{product_id}", response_model=Product)
def get_product(product_id: int, db: mysql.connector.connect = Depends(get_db)):
    cursor = db.cursor(dictionary=True)
    cursor.execute(
        
        """
        SELECT sp.*, k.name as category_name
        FROM sepatu_product sp
        JOIN sepatu_category k ON sp.category_id = k.id
        WHERE sp.id = %s
        """
        
        
        , (product_id,))
    product = cursor.fetchone()

    if product:
        return product
    raise HTTPException(status_code=404, detail="Product not found")

