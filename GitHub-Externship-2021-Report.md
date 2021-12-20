
![Header](https://user-images.githubusercontent.com/51144829/135295467-506b3dc8-53d8-413f-8821-2fb3050768b4.jpg)




# GitHub Externship'21 @ IncubateIND

Project Name: Fellows

Prepared by: Shekhar Kumar Singh

Organization Name: IncubateIND

Mentor: Mr. Kaushik Roy
 
 
## Background

I'm a pre-final year student at Army Institute of Technology, Pune, currently pursuing Bachelor of Engineering in Information Technology. I have developed expertise over the years in Android Development and Backend. I've worked with JavaScript, Node.js, Kotlin, and multiple databases.

## About the project

 <img text-align="center" src="https://user-images.githubusercontent.com/51144829/135296068-56a16bc0-7c2c-46ba-84c5-86d44de6efac.png">


IncubateIND Technology Fellowship is a one-of-a-kind and exclusive program for tomorrow's coders, hackers, designers, and innovators. The program aims to encourage and nurture a community of learners while also laying the groundwork for a strong foundation of competitive, self-reliant individuals. This platform will make management easier for respective community leaders while also providing transparency to explorers who want to participate in various activities of communities of their choice and interests. Technically, this platform is based on the MERN stack.
- It's a Community platform with three main applications.
   + Listing of Community Events
   + Leaderboard for the Community
   + Governing the Community
- A profile system for tracking various Community leaders and their initiatives.
The leaderboard will function automatically based on a scoring scheme provided, as well as it will provide manual functionalities for Administrators only.

 
## Project Goal


Few of the future goals to achieve::

+ Community and Chapter grant forms
+ Community Event Listing - List of events from various communities will be displayed to the users based upon their interests 
+ Automated notification and Events statistics

## My Tasks assigned to me


+ Setup project code and maintain Repository
+ Code review and Deployment 
+ API & Database Schema documentation
+ Fellows REST API implementation
+ Authentication and sessions 
+ Fellows leaderboard 

## Word Done


**Week 1**: Introduction and Code familiarity
We had several meetings during the first week and were introduced to the project, it’s scope, and future prospects. There wasn't much code to explore, so we were assigned to do some research on different platforms and how they work.

**Week 2**: Initial code setup, Monorepo, and MVC structure implementation
 
This week marks the beginning of the implementation and coding process. I was assigned to work on the application's backend. We were tasked with going through the previously pushed code and deciding which features to build first. I was specifically assigned the responsibility of maintaining the repository and ensuring that everything functions properly so that we can have an operational deployment.
We decided to work on the Monorepo architecture. All of the application's modules/components are housed in a single repository. In our case, we have two packages. One was for the front end of the application, and the other was for the backend. 
 
I pushed the app's starter code, which followed the Monorepo architecture. For the backend of the application, I used MVC architecture. The benefit of this is that it allows you to focus on a specific part of the application name, such as how information is presented to and accepted by the user. It contributes to efficient code reuse and parallel application development. Even if the project structure differs from an ideal MVC structure, the basic program flow into and out of the application remains the same.

Model: The model represents the structure of data, the format, and the constraints with which it is stored. It maintains the data of the application. Essentially, it is the database part of the application.
 
View: View is what is presented to the user. Views utilize the Model and present data in a form in which the user wants. A user can also be allowed to make changes to the data presented to the user. They consist of static and dynamic pages which are rendered or sent to the user when the user requests them.
 
Controller: The controller controls the requests of the user and then generates an appropriate response which is fed to the viewer. Typically, the user interacts with the View, which in turn generates the appropriate request, this request will be handled by a controller. The controller renders the appropriate view with the model data as a response.
 
**Week 3**: Database schema and application flow
 
Fellows is a sophisticated application with numerous features and layered access. To create an efficient, scalable, and robust application, I had to brainstorm various solutions. In this week I started working on various data models for our database and finally, I arrived at a particular schema that we will be employing. I had to figure out which entities we had in the collection and how we could model the data so that we could have fewer retrieval operations and a faster response time.
 
	
I was also tasked with improving the application's flow and documenting it so that we could refer to it in the future.

**Week 4**: Documentation

This week was mostly spent documenting the Project as it lacked documentation for Monorepo, database schema, and contribution guidelines. I wrote the documentation for the backend application, as well as the database schema. We were documenting the entire project on GitHub readme, but it was causing collaboration issues because multiple people were contributing to the same files. We could even pull it off using this process, but it was time-consuming, so I moved the documentation to GitBook. Gitbook makes it simple to document various things.

Documentation - http://fellows.gitbook.io/
	
**Week 5**: Linting and pre-commits hooks setup
 
This week I was involved in setting up the linting of the project. The project is contributed by a bunch of people. It was necessary that we should follow proper code guidelines for maintaining consistency. So I decided to set up linting and pre-commit hooks for the codebase. 
The main issue was that the project was using a mono-repo approach where we had different workspaces in a single repository, which required me to figure out how to configure ESlint and Husky. The use of ESlint in a JavaScript project ensures that your code is consistent throughout. I configured ESlint to check for the formatting, errors, and best practices mentioned in the Airbnb style guideline. 
 
The next issue was that you had to run ESlint on each file that you wanted to format, so I just wrote a script that runs with a pre-commit hook. That is, whenever someone commits their code,  scripts are automatically run to execute the ESlint command on the Javascript file to check and format the codes. If the stagged files contain code that does not adhere to proper guidelines, all warnings are displayed in the CLI, and we must resolve the issue before we can commit.
 
**Week 6**: Authentication and database setup
We needed authentication because we had different types of users: administrators, speakers, event organizers, core team members, and regular users. We could have used an email and password strategy, but instead, we used OAuth for third-party authentication. We used passport.js to implement this. It is a Node.js authentication middleware. Passport is extremely flexible and modular, and it can be seamlessly integrated into any Express-based web application. It offers a comprehensive set of strategies that support authentication via a username and password, Facebook, Twitter, and other services. For implementing authentication in the application, we only used Google, GitHub, and LinkedIn strategies.
 
This week, I also worked on configuring the MongoDB database and the Mongoose authentication API.
 
**Week 7**: Explored Redis 
 
This week was mostly spent documenting how community members and administrators are assigned different access permissions and roles.
 
I need to improve my caching and make a real-time leaderboard. In order to implement it, I had to use the Redis database. I spent most of my week learning about Redis and how we can cache APIs to gain a better understanding of it and how to implement it.
 
 
**Week 8**: Review, testing, and deployment
 
The majority of the eighth week was devoted to code review and testing. Despite being incomplete, the first basic version was ready for deployment on the testing domain. I had some trouble deploying it because we used a Monorepo project structure, but I eventually figured it out by writing some prebuilt scripts and utilizing yarn workspaces.

<img align="center"  src="https://user-images.githubusercontent.com/51144829/135298236-f4f6e4bd-d9c8-4830-a6d0-b478df288a72.png">

**Testing version deployment - [Fellows](https://fellows-incubate.herokuapp.com/home)**
 

<p align="center">
<img align="center"  width=70% src="https://user-images.githubusercontent.com/51144829/135296772-569122ab-4d8a-40a2-9ac4-fd9d9180af4e.png">
</p>

<p align="center">
	<b>Dashboard</b>
</p>

<p align="center">
<img align="center" width=70% src="https://user-images.githubusercontent.com/51144829/135296815-32c8d48e-dac7-4ea4-8b05-8c1a9aae87af.png">
</p>

<p align="center">
	<b>Home Page</b>
</p>



 
 
**Week 9**: Fellows API and caching
 
I worked on developing APIs for the community, events, and chapters. It was a time-consuming process at first because I had to create fake data for the database, but I later used mockaroo to generate a larger set of fake data in less time. Fellows will be used globally by various communities, so there is a good chance that it will contain a large amount of data, so I need to design the API in such a way that it is fast and efficient. I added pagination support to these APIs. By providing the page number and page size, arguments can now be sent with the endpoint to access different pages of the queried result.
I also used Redis to cache API responses to reduce the load on our primary database.
 
**Week 10 & 11**: Fellows Leaderboard and Redis setup
 
I have spent these weeks working on the fellows’ leaderboard. It was the most exciting feature that I had worked on during this program, fellows applications aimed at having a leaderboard, where different organizations will be ranked based on certain metrics such as how many events they hold for the community and other such things.
 
This type of Leaderboard is a great example of real-time analytics in action, as well as a demonstration of how quickly your data layer handles reads, writes, sorting, and other critical operations. This was a difficult feature to create because you don't want MongoDB to sort the scores of the various communities every time a server request is made because it is time-consuming and expensive.
 
You can even index your score, but on a larger scale, this approach falls short, so I used Redis Database to solve this problem because Redis is internally designed to provide linear or constant time query results, making it the ideal choice for building a real-time leaderboard. Redis has a built-in data structure called Sorted Sets (ZSETs) that makes creating and manipulating leaderboards simple. The built-in Sorted Set commands make it simple to perform quick native sorting and reporting operations.

<p align="center">
<img align="center" src="https://user-images.githubusercontent.com/51144829/135297456-2c49978a-6540-4871-a553-73d72719b005.png">
</p>

The "ZRANGE" command, for example, returns a set of members. The time complexity will be O(log(N)+M), where N is the number of elements in the sorted set and M is the number of elements returned.
 
"ZRANGEBYSCORE" returns a set of members based on a set of scores. The function "ZRANK" returns the ranking of a given member.
 
We can only store scores and Id of the organization in the sorted set. This is not very useful so a separate Hash data structure was used to store organization details.
 
<p align="center">
<img  src="https://user-images.githubusercontent.com/51144829/135297464-dc5667bb-5873-4000-966f-da458f2367c0.png">
</p>
 
The main issue I encountered was that storing ranks in a sorted set and organization details in a Hash data structure added an additional overhead on the server to perform union on both datasets and return it to the client. Assume we have a sorted set of 1000 organizations with their details in HASH (which is not in order). A simple approach is that every time we retrieve a range of rankings, we query all the ids of elements in the sorted set in HASH and retrieve it from Redis. In the worst-case scenario, even if we had around 1000 organizations, we would have to make an additional two network round trips for each organization, totaling 2000 round trips. This is when a single API call is made; imagine if there were thousands of users. 
 
I pipelined all of the queries and operations to solve this problem. This was also insufficient to reduce the number of operations, so we wrote a Lua script that will run on the Redis and reduce the number of round trips from 2000 to two.

<p align="center">
<img src="https://user-images.githubusercontent.com/51144829/135298425-5c072beb-a351-4958-ac9f-3506512949ed.png">
</p>
 


 
Now I needed to figure out how I was going to load data into Redis. We can accomplish this through two methods:

+ When a cache miss occurs, the new ranking is retrieved from the primary database. This single API call will load data into the Redis cache, and subsequent queries will be loaded from the cache in O(1) time.
+ We only fetch from Redis and add a scheduler that loads data from the primary database into Redis. As a result, we no longer need to be concerned about TTL and cache misses because all API requests will now be loaded from Redis.

I implemented the second one, but I hope to implement both in the future. The designed system now resembles this diagram.
 
 
 
 <img text-align="center" src="https://user-images.githubusercontent.com/51144829/135297247-2f691ce2-60c0-4b5a-baf5-d343997d2246.png">

 
**Week 12**: Reviewing, testing, and Deployment
In last week, work revolved around cleaning the codebase and preparing it for the second deployment. 



## Overall Code Contributions

Here is the list of Commits and PRs that I created during GitHub externship



| Commit  | Description  |  Branch |
|---|---|---|
| [#33c1af0f](https://github.com/incubateind/fellows/commit/33c1af0f2732514aecfd6d1e4374cf5d02a746f4)  | Monorepo boilerplate code  | Backend  |
| [#7df2126a](https://github.com/incubateind/fellows/commit/7df2126affe3f2b82a82d8bb34592941133e701e)  |  Connect MongoDB and Save Third-Party Auth user data | Backend  |
| [#1d06df9a](https://github.com/incubateind/fellows/commit/1d06df9a63ece35bbfab399692ed90eb5cb1784b)  | Build: Heroku post-build script,  Chore: change static client folder, Feat: serve on a single port  | Backend  |

 
 

| PR Link | Commit | Description | Status |
|---|---|---|---|
| [#5](https://github.com/incubateind/fellows/pull/5)  | [#21bde28](https://github.com/incubateind/fellows/pull/5/commits/21bde2881f3d2e6def3d74c1bf29f2639f62e200) | Chore: Updated Backend package readme  | Merged ✅  |
| [#9](https://github.com/incubateind/fellows/pull/9) | [#7df2126](https://github.com/incubateind/fellows/pull/9/commits/7df2126affe3f2b82a82d8bb34592941133e701e) | Feat: Third-party OAuth implementation with storage of auth data  | Merged ✅  |
| [#10](https://github.com/incubateind/fellows/pull/10)  | [#44792ca](https://github.com/incubateind/fellows/pull/10/commits/44792ca7b4b266c14a8cfaaec68d67d49476716b) | Fix: LinkedIn incorrect user schema and undefined profile data response  | Merged ✅  |
| [#14](https://github.com/incubateind/fellows/pull/14)  | [#62f4f56](https://github.com/incubateind/fellows/pull/14/commits/62f4f56c38f5ee3066554ed50f1c5c5d513e847e)  | Chore: ESlint, husky, prettier, and hooks added  | Merged ✅ |
| [#16](https://github.com/incubateind/fellows/pull/16)  | [#1d06df9](https://github.com/incubateind/fellows/pull/16/commits/1d06df9a63ece35bbfab399692ed90eb5cb1784b) [#65daf2d](https://github.com/incubateind/fellows/pull/16/commits/65daf2db85c74b709361b0922097f720b6146825)   |  Merge: Merge develop branch | Merged ✅ |
| [#19](https://github.com/incubateind/fellows/pull/19)| [#a749622](https://github.com/incubateind/fellows/pull/19/commits/a7496223c932b1c3ea421a73f94cc4fb7cd49936)  [#744c4fe](https://github.com/incubateind/fellows/pull/19/commits/744c4fe003d2bec78279c6c66e184e9798358a2f)  [#68c0b6d](https://github.com/incubateind/fellows/pull/19/commits/68c0b6d27ca43d0933a3c2a15f3bed930fdbc515)  [#c2b42ee](https://github.com/incubateind/fellows/pull/19/commits/c2b42ee4e5d9c00f81255bc8f3f047204a92d977) |  Redis database setup Data migration scheduler Lua script for internal database operation Leaderboard API for organization ranking | Merged ✅  |
| [#20](https://github.com/incubateind/fellows/pull/20)  | [#d05aaa6](https://github.com/incubateind/fellows/pull/20/commits/d05aaa6fe28ee31c5475cc5a46c3f60eb6a9844a) | Feat: Community API route with pagination support  | Merged ✅  | 



## Work Left to do


We expected to accomplish a lot and provide fellows with a better and more complete version by the end of this externship. We completed the majority of our target features, but due to time constraints, we were unable to complete some of them. The majority of our work left is focused on various areas like -

+ Dashboard part of the application.
+ Event Forms 
+ CDN
+ Notifications and mailing process.

## Learnings


One of the most notable aspects of this externship, in my opinion, was learning how to write clean code. Also, my understanding of backend design underwent a significant shift. This program taught me how to be more efficient at work. From a technical standpoint, these three months were jam-packed with opportunities to experiment with Redis, Lua Scripting, and various architectures. I worked with people who were full of energy and knowledge, collaborating and helping one another. I really liked how people worked in open source.

## Acknowledgments


I'd like to take this opportunity to express my gratitude towards my mentors for their assistance and support throughout this process. We were extremely fortunate to have Mr. Kaushik Roy as our mentor who was involved and contributed in GSoC 2019 and he assisted us in resolving some technical difficulties we were facing. I would also like to thank GitHub India and Incubate India for providing us with this great platform and making this experience a memorable one.

## Conclusion


The last three months have been extremely beneficial and fruitful. I have seen an exponential rise in my learning capabilities and coding experience. I also learnt to manage and prioritize my tasks and work in a well-organized and structured environment. I am grateful for this marvelous opportunity as I was also able to amplify my collaboration skills by working with a fantastic team. I appreciate the Github Externship program for sowing the seeds of my Open Source Journey. 

 
 
 



