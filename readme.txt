Documentation:

Navigate to project root and type docker-compose up

In a browser go to http://localhost to open the frontend

You can login with a test user:
Username: client1
Password: qvantel1

Or add new users in http://localhost/admin/
Username: admin
Password: qvantel

The Django project has 2 applications:
itemApp: Basic application for the content of the shop
    API REST Request:
        - http://localhost/api/items/ #Return the articles of the shop
cartApp: Application including the request required for the test
    API REST Requests:
        - http://localhost/api/cart/<cartId>/ #Returns the content of a cart with a given cart id
        - http://localhost/api/cart/checkout/ #Receives the conten of a cart, saves it to the database and returns a cart id
        - http://localhost/api/login/
        - http://localhost/api/refresh/
