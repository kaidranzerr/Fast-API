from fastapi import FastAPI , HTTPException
from .services.products import get_all_products
app = FastAPI()


# first endpoint --> static route
@app.get('/')
def root():
    return {"message": "Welcome to main bitch"}


# # dynamic route
# @app.get("/products/{id}")
# def get_products(id: int):
#     products = ['abc' , 'def' , 'fgh' , 'ijk']
#     return products[id] if products[id] else HTTPException(status_code=404 ,detail= "No product found!")

@app.get("/products")
def get_products():
    return get_all_products()