from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "everything ok"}


contact_list = [
    {
        "id": 1,
        "name": "Monzur Alam",
        "phone": "01512-345678",
        "location": "Banasree, Dhaka",
    },
    {
        "id": 2,
        "name": "Ruhin Mia",
        "phone": "01712-345678",
        "location": "Aftabnagor, Dhaka",
    },
    {"id": 3, "name": "Rubel Mia", "phone": "01912-345678", "location": "Badda, Dhaka"},
]


@app.get("/contacts")
def get_contacts():
    return contact_list


@app.get("/contacts/{term_id}")
def get_contact(term_id: int):
    for contact in contact_list:
        if contact["id"] == term_id:
            return contact
        return {"message": "term_id not found"}