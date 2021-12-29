![Header](https://user-images.githubusercontent.com/72696677/146715701-51533be6-5767-4783-94b1-6b8be50dc9be.png)


# FamPay_Backend-Ass

Project Assignment Name - API creation for fetching latest videos

Organization Name - Fampay

Prepared by - Vaibhav Patel

### Project Background

To create an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

- Created an API which fetches the latest videos from Youtube according to the search query used, stores them in DB and returns the data in a JSON Object in reverse Chronological Order.
- Search Query used - **official**
- **(Bonus Point Feature)** -> Created a Dashboard for viewing stored videos with sorting options like - Sort by Video_Title, Channel_Title.
- JSON Object contains elaborated data for every search queries video.
- Used this JSON object to store Index, channel_title, video_title, video_description, date_time,thumbnail URL in the database which will be useful in fetching videos from DB and also helps in building a Dashboard.
- **DjangoRestFramework** was used to created a GET API for fetching videos from database and sending it to the Server.
- Serializers were used to convert QuerySet Object returned from database to JSON Response.
- JSON Object is sent for displaying the result in a Paginated Response.
- Result is sorted in descending order of published datetime.
- Here is a Low Level Diagram Explaination of the API:

![flowdiagram drawio](https://user-images.githubusercontent.com/72696677/147314516-2c145cf8-ae84-49b8-9c4a-6805d1dd0bb1.png)

## Instrcutions to run the server and test the API.

+ Download the Zip Folder Repository which contains all the code.
+ Open the Project Directory on your machine using a Text Editor of your choice.
+ First you need to install all the dependencies/packages that were used to create the API.
+ Open your project Folder directory in Command Line and run the code **"pip install -r requirements.txt"**.
+ After installing the requirements, start the Server using command **"python manage.py runserver"**.

## After starting the Server, you can test the API using two ways : 

1) Paste the url **"http://127.0.0.1:8000/showVideos/"** in your Web Browser, it will show a Paginated response of Searched videos in reverse chronological order of their publishing date-time.


![res](https://user-images.githubusercontent.com/72696677/147314031-4ede553c-52c2-4a3d-8495-0502bd0f7c79.png)

#### And the Search Query result is also getting store in our Database shown below : 

![db](https://user-images.githubusercontent.com/72696677/147314026-61fd6326-a0bb-473e-a69d-2e5729310d83.png)

2) Use an Application [Postman](https://www.postman.com/) which is used for Test an API. Paste the URL **"http://127.0.0.1:8000/showVideos/"** in the Field given below and then click on Send. Make sure **GET** request is selected as shown below.

##### Note :
If you want to use Postman to Test the API, you need to go to views.py file in **webApp** folder and then comment and uncomment some code to successfullt test the API in Postman. The Code that needs to be commneted and uncommneted in mentioned there. As Postman requires a JSON Response, while Rendering result in a Paginated response requires rendering that JSON Object. So return type is different for both. 

![postman](https://user-images.githubusercontent.com/72696677/146718877-9946713b-240e-479a-a236-7485f8ecadef.png)

#### Below is the result after testing/Running the API in Postman

![2](https://user-images.githubusercontent.com/72696677/146721543-6ff69cbe-9e26-482b-8bf5-e85537c8fed3.png)

### Dashboard for showing stored Videos and having sorting options like Sort by Channel_Title, Video_Title:

![dashboard](https://user-images.githubusercontent.com/72696677/147648628-a7a98086-c496-4396-9df6-36b4045ee65a.png)

### Result

![dashboardresult](https://user-images.githubusercontent.com/72696677/147648739-e6f43274-78eb-4655-bbc8-1c78a03b3c5c.png)



### I hope you Liked the Application, feel free to reach out to me on LinkedIN if you have any queries.

[Vaibhav Patel - LinkedIN](https://www.linkedin.com/in/vaibhavpatel19/)

