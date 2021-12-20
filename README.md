![Header](https://user-images.githubusercontent.com/72696677/146715701-51533be6-5767-4783-94b1-6b8be50dc9be.png)


# FamPay_Backend-Ass

Project Assignment Name - API creation for fetching latest videos

Organization Name - Fampay

Prepared by - Vaibhav Patel

### Project Goal

To create an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.


## Instrcutions to run the server and test the API.

+ Download the Zip Folder Repository which contains all the code.
+ Open the Project Directory on your machine using a Text Editor of your choice.
+ First you need to install all the dependencies/packages that were used to create the API.
+ Open your project Folder directory in Command Line and run the code **"pip install -r requirements.txt"**.
+ After installing the requirements, start the Server using command **"python manage.py runserver"**.

## After starting the Server, you can test the API using two ways : 

1) Paste the url **"http://127.0.0.1:8000/showVideos/"** in your Web Browser, it will show a Paginated response of of Searched videos in reverse chronological order of their publishing date-time.
2) Use an Application [Postman](https://www.postman.com/) which is used for Test an API. Paste the URL **"http://127.0.0.1:8000/showVideos/"** in the Field given below and then click on Send. Make sure **GET** request is selected as shown below.

![postman](https://user-images.githubusercontent.com/72696677/146718877-9946713b-240e-479a-a236-7485f8ecadef.png)

