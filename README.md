# **INF601 - Advanced Programing in Python**
Ryder Cook
## **Mini Project 4**
## _Description_
This is a portfolio website that shows my skills, and services that I offer for digital content creation.
It uses Python, Django, HTML, and Bootstrap. Users have the ability to create and account to leave feedback on my work. It utilizes Django to generate tables for incoming posts, reading poll answers, as well as creating users. To get started read the instructions below.

## _Disclaimer_
Bootstrap V5 Modal
- Does not work as intended
  - Replaced it with a separate page that is displayed to the user before deleting post

## _Execution Instruction_
1. Clone or download repository
2. Install necessary packages

   `pip install -r requirements.txt`

## _Initialize Database_

   `python3 manage.py makemigrations portfolio`
   `python3 manage.py migrate`

## _Create Super User_
   
   `python3 manage.py createsuperuser`  

## _Run Project Via PyCharm_
    - Start the app by clicking the ▶ button
    - In Browser Navigate To: http://127.0.0.1:8000

## _Run Project Via Terminal_

   `python3 manage.py runserver 8000`

    - In Browser Navigate To: http://127.0.0.1:8000

## _Create Account or Login With Provided Info_
    - Username: reviewerone
    - Password: #1+22R3^x=0