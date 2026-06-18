from fastapi import FastAPI , HTTPException
app = FastAPI()


# first endpoint --> static route
@app.get('/')
def root():
    return {"message": "Welcome to main bitch"}


# dynamic route
@app.get("/products/{id}")
def get_products(id: int):
    products = ['abc' , 'def' , 'fgh' , 'ijk']
    return products[id] if products[id] else HTTPException(status_code=404 ,detail= "No product found!")

