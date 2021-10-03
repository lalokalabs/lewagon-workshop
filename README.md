# Developing Django on Repl.it

- Fork this template to get started
- Simply hit run to start the server
- The server will autoreload as needed. You don't need to restart the server manually.

# Preparation before the course

The course will be conducted through replit.com.

- Participant should create a free account on Replit prior to the course time
- Signup at https://otp.dev/ for a free trial - we will use its OTP API to validate email address and phone number

# What will you learn in this course?
This course is designed as a quickstart, with project structure already created and a number of useful apps for development also added.

By the end of this course you should know about:-

- Basic structure for Django project
- How to define models and relationship
- How to use the webshell and django admin site for modelling your application data entity
- How to use form to collect and validate user input
- How to use views to process incoming http request and return response with Django templates
- Integrate your views with third party API - GetOTP for verifying email address and phone number

## Bonus
- Effective debugging and troubleshooting using interactive web debugger

# Shell

Django utilizes the shell for managing your site. For this click on the `?` in the lower-right corner and click "Workspace shortcuts" from there you can open a new shell pane. 

# Database

By default this template utilizes the sqlite database engine. While this is fine for development it won't work with external users of your app as we don't persist changes to files when they happen outside the development environment. 

We suggest bringing a database using an outside service. 

See Django documentation on how to setup a database: https://docs.djangoproject.com/en/3.0/intro/tutorial02/

