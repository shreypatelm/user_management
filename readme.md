# The User Management System Final Project


---
## Closed Issues Documentation

[Issue#1 - Email Verification](https://github.com/shreypatelm/user_management/issues/1)
**Description:** The email verification process was not being executed properly due to issue of connecting it properly with Mailtrap.By resolving the issue the email verification link was sent to the registered user's email address and only after verification the user was been checked as verified. <br>

[Issue#2 - Admin Veriification handling](https://github.com/shreypatelm/user_management/issues/3) 
**Description:** The admin was getting verified automatically without being verified via mailtrap. The first user will be admin but the verification for the admin has be implemented.<br>

[Issue#3 - Password Logic implementation](https://github.com/shreypatelm/user_management/issues/5)  
**Description:** The user should enter atleast one digit, one special character, one uppercase alphabet, one lowercase alphabet and atleast 10 characters. <br>

[Issue#4 - Skip and limit values validation](https://github.com/shreypatelm/user_management/issues/7) 
**Description:** The issue was while getting the list of the user, when we enter the negative value for skip and limit then instead of error it returns 200(Ok).<br>

[Issue#5 - Showing is_professional false](https://github.com/shreypatelm/user_management/issues/9) 
**Description:** The issued is fixed. Now when we mark the is_professional as true then while getting the user we will get true instead of false.<br>


---


## Docker Hub Repo
[Link to my Docker Repo](https://hub.docker.com/repository/docker/shreyp30/user_management/general)

## Docker Hub Image
![Docker_Hub_Image](https://github.com/shreypatelm/user_management/blob/main/Docker_Hub%20Image.png)

## Docker Desktop Image
![Docker_Desktop Image](https://github.com/shreypatelm/user_management/blob/main/Docker_Desktop%20Image.png)  


---


## New Feature Added - "User Profile Management"
[Link to the Feature Branch](https://github.com/shreypatelm/user_management/tree/new_feature)

### About feature
This feature allows users to manage their profile information. It enables managers and admins to upgrade users to professional status.

### Feature Implemented Images
![Profile Management](https://github.com/shreypatelm/user_management/blob/main/User_Profile_Management.png)
![Verified_User](https://github.com/shreypatelm/user_management/blob/main/is_professional%20.png)


---


## What I learned from this project
Throughout this project, I gained valuable experience in real-world software development, particularly in user management systems. I learned how to effectively collaborate in a team environment, contributing to feature implementation, bug fixing, and ensuring code quality. By implementing a new feature, I followed industry best practices for coding, testing, and documentation. I also enhanced the system's test coverage, identifying gaps and writing additional tests to handle edge cases and error scenarios.

This project provided hands-on experience with tools and practices commonly used in the software industry, such as version control with Git, Docker for deployment, and continuous integration for automated testing. I also developed problem-solving skills by debugging and addressing issues, ensuring the system remained functional and reliable. Overall, this project has equipped me with practical skills and a deeper understanding of the development process, preparing me for future professional challenges.
