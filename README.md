![Managey_drf - Django REST Framework API]()

This is the backend REST API repository whic is used for my frontend project []()

View Live site: []()

View API site: []()

View Frontend README.md file: []()
 
View Backend README.md file: []()

# Table of Contents
## [User story](user-story)
## [Entity Relationship Diagram](ERD)
## [Models](Models)
## [Testing](Tests)
## [Technologies Used](Tech-stack)
## [Deployment to Heroku](Deployment)
## [Credits](Credits)
    - [Content]()
    - [Media]()
## [Acknowledgement](Acknowledgements)



# [User story](user-story)

# [Entity Relationship Diagram](ERD)
- The following image represents the database model structure of the web application: ![ERD-Image](). The image was created using [Lucid]()

# [Models](Models)
## User 
- The user model is part of the django alluth library
- The user model contains all the information of the user
- Has a one to one relationship with the owner field in the profile model
- Has a one to many relatiionship with the Task model
- Has a one to many relatiionship with the Comments model 
## Profile
- The profile model has a one to one relationship with the user, this is refrenced by the userID field within the profile. 
- The model contains the following fields: created_at, updated_at, name, bio, image, owner, is_owner
## Task
- The task model has a one to many relationship with the user. It refrences the UserID
- The model contains the following fields: owner, created_at, updated_at, title, description, attachment, overdue, assigned_users, priority, state
## Comments
- The comments model has a one to many relationship with user, it references the UserID
- It has a foreignkey relation with the task moel, it references the TaskID
- It has the follwowing fields: id, owner, created_at, updated_at, content taskID

# [Testing](Tests)

# [Technologies Used](Tech-stack)
## Languages
- [Python]()
## Libraries and Frameworks
- [Django]()
- [Django REST Framework]()
## Packages
- [cloudinary]()
- [rest_framework]()
- [Pillow]()
- [cloudinary_storage]()
- [django-filter]()
## Other tools
- [GitHub]()
- [Gitpod]()
- [Heroku]()
- [Cloudinary]()
- [GitBash]()
- [asgiref]()
- [ElephantSQL]()