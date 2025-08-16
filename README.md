[![Trade Portal Live Demo]](https://www.youtube.com/watch?v=3ZOv9Dc9c2o)

****Trade Porta: A Backend Application using Django****

This is a comprehensive full-stack web application designed to help users create and manage a personal stock watchlist. It showcases a modern development workflow from a Django backend and a front end to Docker containerization.

**Features**

1.**User Authentication:** Secure user registration and login system.

2.**Company Search:** Search for companies by name, symbol, or scripcode.

3.**Dynamic Wishlist:**  Add and remove companies from a personal watchlist.

4.**MySQL Database:** All user and watchlist data is stored and managed in a persistent database.

5.**Containerized Deployment:** The entire application is packaged with Docker for consistency across development and production environments.

**Tech Stack**

1.**Backend:** Python, Django, Django REST Framework

2.**Database:** MySQL

3.**Frontend:** HTML, CSS, JavaScript

4.**Deployment:** Docker, Docker Compose

**Installation & Deployment**

This project is designed to be run entirely with Docker and Docker Compose. No local dependencies for Django or MySQL are required.

1.**Clone the Repository**

Start by cloning the project to your local machine:

git clone https://github.com/Shaik-Althaf-TechAZsure/TradePortal.git

cd TradePortal

2.**The Docker Environment**

The project's deployment is defined by the following files:

"start.sh"

this script handles the server startup and database migrations.

"python manage.py makemigrations TradePortal

python manage.py migrate

gunicorn --bind 0.0.0.0:8000 TradePortal.wsgi --workers 4"

"docker-compose.yml"

This file orchestrates the django and MySql services, connecting them in a single network.

version: '3.8'

services:

  web:
  
    build: .
    
    command: sh -c "./start.sh"
    
    volumes:
    
      - .:/code
      
    ports:
    
      - "8000:8000"
      
    depends_on:
    
      - db

    environment:
    
      - MYSQL_DATABASE=${MYSQL_DATABASE}
      
      - MYSQL_USER=${MYSQL_USER}
      
      - MYSQL_PASSWORD=${MYSQL_PASSWORD}
      
      - DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY}
      
      - DJANGO_ALLOWED_HOSTS=${DJANGO_ALLOWED_HOSTS}

  db:
  
    image: mysql:8.0
    
    container_name: mysql_db
    
    restart: always
    
    environment:
    
      MYSQL_DATABASE: ${MYSQL_DATABASE}
      
      MYSQL_USER: ${MYSQL_USER}
      
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}
      
      MYSQL_ROOT_PASSWORD: ${MYSQL_PASSWORD}
      
    ports:
    
      - "3306:3306"
      
    volumes:
    
      - ./data/mysql:/var/lib/mysql

3.**Build and Run**

To build the Docker images and start the services, run the following command. The -d flag runs the containers in detached mode.

"docker-compose up -d --build"

<img width="950" height="657" alt="image" src="https://github.com/user-attachments/assets/82862e1f-4790-4064-99a5-d2314a8c08c0" />


**API Endpoints(with Postman)**

All backend interactions are handled through a RESTful API. Below are examples of the main endpoints and their responses, as shown in Postman.

1.**Register API**

**>URL:**  http://localhost:8000/api/register/

**>Method:** POST

**>Description:** Creates a new user account

<img width="1352" height="887" alt="image" src="https://github.com/user-attachments/assets/8d155acd-a2e7-4279-9999-1b20a2f70594" />


2.**Login API**

**>URL:**  http://localhost:8000/api/login/

**>Method:** POST

**>Description:**  Authenticates a user and returns a token.

<img width="1378" height="930" alt="image" src="https://github.com/user-attachments/assets/88b6a397-187a-40ca-b2d6-b48dca99c024" />


3.**Copying the authentication token**

**>Description:** Copy the access token to authenticate to the rest of the api's

<img width="1213" height="67" alt="image" src="https://github.com/user-attachments/assets/cd81564c-4b42-4f49-98db-ecd629abd824" />


Copy this access token and

1.Go to authentication tab

2. select bearer token and paste it.
   
<img width="1348" height="363" alt="image" src="https://github.com/user-attachments/assets/cb456430-96b9-4610-a5e5-563f9293078d" />


4.**Retreive Company List**

**>URL:**  http://localhost:8000/api/companies/

**>Method:** GET

**Access:** Paste the access token at authentication type

**>Description:**  dds a new company to the authenticated user's watchlist.

<img width="1358" height="880" alt="image" src="https://github.com/user-attachments/assets/5ac54084-517c-4a45-8306-2f782ab318b5" />


5.**Watchlist Add API**

**>URL:**  http://localhost:8000/api/watchlist/add/

**>Method:** POST

**Access:** Paste the access token at authentication type and type the json text at body

**>Description:**  Adds a new company to the authenticated user's watchlist.

<img width="1375" height="741" alt="image" src="https://github.com/user-attachments/assets/30ec46b4-e648-4c49-a431-74085d0f77b1" />


6.**Watchlist Get API**

**>URL:**  http://localhost:8000/api/watchlist/

**>Method:** GET

**Access:** Paste the access token at authentication type

**>Description:**  Retrieves the complete watchlist for the authenticated user.

<img width="1382" height="813" alt="image" src="https://github.com/user-attachments/assets/ecb00e5b-b334-4cb0-aa2f-1eba423a9b96" />


7.**Watchlist Remove API**

**>URL:**  http://localhost:8000/api/watchlist/remove/

**>Method:** POST

**Access:** Paste the access token at authentication type and type the json text at body

**>Description:**  Removes the selected company to the authenticated user's watchlist.

<img width="1362" height="762" alt="image" src="https://github.com/user-attachments/assets/5ae9f7ec-58e4-4341-aee0-0bb02b278e22" />


8.**Searches and Filters API**

**>URL:**  http://localhost:8000/api/companies/?company_naame_icontains=<Company Name>

**>Method:** POST

**Access:** Paste the access token at authentication type

**>Description:**  Removes the selected company to the authenticated user's watchlist.

<img width="1382" height="836" alt="image" src="https://github.com/user-attachments/assets/48fa3263-75f3-4948-81f2-7a0692978d24" />


**Database Scheme & Data(MySQL)**

The application uses a MySQL database with a straightforward schema to manage users and their watchlists.

1. cmd > docker ps
   
><img width="1631" height="113" alt="image" src="https://github.com/user-attachments/assets/d7f5b4d2-4afc-48b6-a3b5-3adc13c179d1" />


2. cmd >docker exec -it tradeportal-db mysql -u tradeuser -p
   
and enter the password : trade123

<img width="826" height="248" alt="image" src="https://github.com/user-attachments/assets/685c007c-7b10-4817-9d22-4426edacef5a" />


3. mysql > show databases;
   
4. mysql > use tradeportal
   
5. mysql > show tables
   
<img width="666" height="650" alt="image" src="https://github.com/user-attachments/assets/403d32ff-c152-432e-91dc-701313fdcaed" />


6. mysql > select * from auth_user;
   
<img width="1918" height="281" alt="image" src="https://github.com/user-attachments/assets/b0839cec-9628-4b74-a931-408291c30097" />


7. mysql > select * from TradePortal_company;
   
<img width="797" height="932" alt="image" src="https://github.com/user-attachments/assets/599e58a9-07dc-4189-9a7f-a89f359ec366" />


8.mysql >select * from TradePortal_wishlist;

<img width="441" height="180" alt="image" src="https://github.com/user-attachments/assets/05a37989-0317-4952-8f70-26c4345ac174" />


**Frontend Demo**

The frontend provides a clean, user-friendly interface to interact with the backend API.

1.**Register Page**

Users can create a new account from this page.

<img width="731" height="807" alt="image" src="https://github.com/user-attachments/assets/d4d5a35b-5b51-4c9e-8bf0-bef16d56cee4" />


2.**Login Page**

The login page allows existing users to authenticate.

<img width="582" height="712" alt="image" src="https://github.com/user-attachments/assets/13d5065f-2ea1-488d-9ffc-4f7561da7b9a" />


3.**Company Search & List**

After logging in, users are presented with a list of companies they can add to their watchlist.

<img width="1668" height="870" alt="image" src="https://github.com/user-attachments/assets/67a76f9d-b4e9-421c-9be0-8e861cd107fe" />


4.**Watchlist Display**

This page shows the user's personal watchlist with dynamic data (company names, symbols, etc.) fetched from the backend.

<img width="1601" height="572" alt="image" src="https://github.com/user-attachments/assets/b26b2490-ce99-47c6-a8a8-6a5b71bb18bc" />


<img width="1602" height="492" alt="image" src="https://github.com/user-attachments/assets/e69bebab-bfd2-4b41-9573-0decc37a5087" />


5.**Remove from Watchlist**

Users can easily remove companies from their watchlist with a single click.

<img width="1630" height="458" alt="image" src="https://github.com/user-attachments/assets/50013721-4f10-4944-86f6-bbf666f87557" />

