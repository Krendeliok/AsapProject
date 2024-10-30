# Launch Instructions
1. Clone the repository
2. Run the following command in the terminal to run application:
```docker compose up --bild```

### All needed dependencies will be installed in the Dockerfile

### To test endpoints you can open http://localhost:5000/books or http://localhost:5000/books/{id} in your browser

To run tests you can run the following command in the terminal while docker containers are running:
```docker exec -it books_web ./manage.py test```