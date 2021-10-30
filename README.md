# FunMaths
#### Video Demo:  https://youtu.be/bOdN__GK2XE
#### Description:

FunMaths is a fun web application made with Flask and Frontend languages like HTML, CSS (Bootstrap) and JavaScript.


On FunMaths first graders or generally students in elementary school can practice basic math operations like addition subtraction,
multiplication and division, and test themselves on all of those using the exam mode.

In my applications.py file I created the routes and functions to check valididity of the registrants and logins, and created the exam mode as well as evaluted
other operations' answers.

In helpers.py we have the function decorater login_required and the error function, both taken from the previous problem set in CS50.

In operations.py I have the 4 operation modes on the site.

All of the HTML files in the templates folder are probably self explanatory. But still, we have the layout.html for a boiler plate to files like
register.html, login.html, index.html and error.html, and then we have operations.html and divd.html for the operation pages.

Exam.html is for the exam mode and here I used jQuery and JavaScript to dynamically change the websites look after user submits the answers.
It shows the correct answer if any question is not answered or the answer was wrong. For division it also shows the actual remainder if that was not given
or again false.

The JavaScript code for the exam.html file is contained in the static folder in exam.js which is explained below.

In the static folder I have my favicon (the abacus emoji),
the styles.css file for the layout,
symbols.css file which styles the operation symbols design on the index page (I am very proud of this one actually,
never enjoyed css that much before),
and the exam.js which dynamically changes the exam page by evaluating users' input.

In my database I only have one `users` table to store users' information such as
username,
email,
password,
and optional information like
school,
birthday,
grade,
and whether they are disabled or not.

I actually wanted to add the functionality that the site would speak to the user using speech_recognition library in Python
so that disabled users could also practice using voice assistance. But Flask gave me endless errors and I could not find another
way (using JS or something else) without having to make my site secure (httpS) so I decided I would maybe do it in the future
when I am more confident using these technologies. That is why I am leaving the disabled checkbox on the registration page.

I could also get the total number of correct and false answers in the exam mode and recommend the user that they would practice the operation
they are least confident in when they log in the next time.

But all of those things are not implemented in the project right now.
