![Header](https://user-images.githubusercontent.com/72696677/146715701-51533be6-5767-4783-94b1-6b8be50dc9be.png)


# FamPay_Backend-Ass

Project Assignment Name - API creation for fetching latest videos

Organization Name - Fampay

Prepared by - Vaibhav Patel

### Project Background

To create an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

- Created an API which fetches the latest videos in reverse Chronological Order and returns the data in a JSON Object.
- Search Query used - **official**
- JSON Object contains elaborated data for every search queries video.
- Use this object to store  channel_title, video_title, video_description, date_time,thumbnail URL in the database which helps in building a Dashboard.
- JSON Object is sent to an HTML Page for displaying the result in a Paginated Response.
- For testing an API, JSON Object can be directly sent as a JsonResponse.

## Instrcutions to run the server and test the API.

+ Download the Zip Folder Repository which contains all the code.
+ Open the Project Directory on your machine using a Text Editor of your choice.
+ First you need to install all the dependencies/packages that were used to create the API.
+ Open your project Folder directory in Command Line and run the code **"pip install -r requirements.txt"**.
+ After installing the requirements, start the Server using command **"python manage.py runserver"**.

## After starting the Server, you can test the API using two ways : 

1) Paste the url **"http://127.0.0.1:8000/showVideos/"** in your Web Browser, it will show a Paginated response of of Searched videos in reverse chronological order of their publishing date-time.

![1](https://user-images.githubusercontent.com/72696677/146721527-0e712444-a1ea-4b9e-9686-bd00bf43f3d1.png)

2) Use an Application [Postman](https://www.postman.com/) which is used for Test an API. Paste the URL **"http://127.0.0.1:8000/showVideos/"** in the Field given below and then click on Send. Make sure **GET** request is selected as shown below.

##### Note :
If you want to use Postman to Test the API, you need to go to views.py file in **webApp** folder and then comment and uncomment some code to successfullt test the API in Postman. The Code that needs to be commneted and uncommneted in mentioned there. As Postman requires a JSON Response, while Rendering result in a Paginated response requires rendering that JSON Object. So return type is different for both. 

![postman](https://user-images.githubusercontent.com/72696677/146718877-9946713b-240e-479a-a236-7485f8ecadef.png)

#### Below is the result after testing/Running the API in Postman

![2](https://user-images.githubusercontent.com/72696677/146721543-6ff69cbe-9e26-482b-8bf5-e85537c8fed3.png)

### I hope you Liked the Application, feel free to reach out to me on LinkedIN if you have any queries.

[Vaibhav Patel - LinkedIN](https://www.linkedin.com/in/vaibhavpatel19/)

