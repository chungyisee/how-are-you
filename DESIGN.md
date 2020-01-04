# Colour choice and language

A green-yellow gradient of colours was chosen because they are bright and welcoming. It also makes the webpage look more "fun" and less professional, making it more inviting for users.
The gradient was programmed in using background: linear-gradient in CSS.

# The use of bubbles

Our logo (favicon.png in /static/) is a green and yellow speech bubble with a question mark inside it. The idea of bubbles as a consisitent theme is used to convey the message that your thought and speech (bubbles) should be allowed to flow freely, and that you should not feel afraid to share.
Bubbles continuously float and rise up the screen from bottom to top. Their movement is slow and calming, aiming to make the user feel at ease.
The code for the bubbles was adapted from https://codepen.io/Mark_Bowley/pen/mEtqj. Implemented in CSS, each individual bubble's speed, size and travel starting time is set in CSS, and runs in a cycle.

# Button design

When hovering over a button, bubbles rise rapidly across the background, and the gradient of colours on the button changes. This immediately signals to the user that the button can be clicked, and that they can quickly move on to the next page.
The code for the button was adapted from https://tutorialzine.com/2010/10/css3-animated-bubble-buttons. Implemented in CSS, the background colour of the button was changed to fit the colour gradient of the website.

# Choice of fonts

Pacifico was used on the index page - as a cursive, eye-catching and playful font, it is welcoming and puts the user at ease.
Arimo and Quicksand are used as header and explanatory fonts for subsequent pages. These are clean, rounded fonts that are visually appealing and take away clutter from the page, allowing the user to focus on keying in their responses.

# How the Web App Works
On line 13 of application.py, app.secret_key = urandom(24) generates a random key for each session each time a new user uses our website. Using session in flask, a unique cookie is passed through each successive html webpage so that submissions to each form are passed to the same row in the SQL table called "resources" in howareyou.db
The responses to each question are stored in the "responses" table in howareyou.db. The responses are then selected and then the string is scanned for particular words. Certain words keyed in mean that certain groups will be recommended. For instance, words relating to eating disorders (such as anorexia, inconsistently, appearance, image)
will indicate to the programme that ECHO should be recommended to the user.The final recommmendations page (recommendation.html) will compile all the recommendations into a table. Any, all or none of the 5 student-run counseling groups could be recommended to you (Contact, ECHO, Indigo, Response, Room 13).
You also have the option to go to a full list of resources (resources.html) after receiving your recommendations.

Recommendations are given based off of keywords detected in a user's responses. Responses are retrived from the SQL table, and the string is split into individual substrings by punctuation and whitespace using RegEx.
Iterating through the substrings, keywords that have been programmed into application.py checked against. If a specific keyword is matched, then a particular peer-counseling group is recommended (such as "anorexia" for ECHO, or "identity" for Contact)

In order to figure out what to display, we used the {% if ~~condition is true~~ %} which is adopted from the CS50 Finance index code. In order to use this, we created boolean varaibles at the start of our recommendation.html page in the "GET" section. We created a separate boolean value for each club on campus, along with a boolean value called ToRecommend.
When a certain word is entered to answer a certain question, which is detected by our parsing mechanism, then this means we have a "hit" for a specific club on campus, then this boolean value is changed to true. If any of the boolean values becomes true, then the ToRecommend variable will also become true, which will cause the table to appear.
Using the {% if ~~condition is true~~ %} and {% else %} and {% endif %} tags, then we can change the size of our table which will show up in the recommendation.html page. The way our table is formatted is so that the text in the left columns is bigger than the text inside and the headers are the biggest.
If there are no matches, then the {% else %} tag will cause the alternate, formatted text to appear.

If no groups are applicable to the person, the web application is designed in such a way that it still recommends that the user possibly reach out to Room 13, which is a general purpose mental health resource.
We have coded in a way so that even if no input is given, there will still be a message displayed and a link in the form of a button to all of the possible resources. And by extension, if there are no matches to a particular group, for whatever reason, then there will still be a message displayed and a link to a list of all of the possible resources.

