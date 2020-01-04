This is CS50, and this is How Are You? Mental Health Resources Made Accessible @Harvard

# Starting the Webpage
Execute "cd" to ensure that you’re in ~/ (i.e., your home directory).
Execute "cd project" to change into (i.e., open) the ~/project/ directory.
Execute "cd howareyou" to change into (i.e., open) the ~/project/howareyou/ directory.
Execute "flask run" to start the webpage.
Visit the URL outputted by flask to see the distribution code in action.

# Using the Webpage
The webpage starts you off with a homescreen (index.html) that invites you to have a conversation. To start having the conversation, click on the button on the home page.
After clicking the button that says  "What's On Your Mind?", it will take you to another page that invites you to enter your name (yourname.html).
After entering your name, you will get to answer 7 questions (question1.html, question2.html ... question7.html) about school and personal life. Please feel free to be as elaborate as you would like and as you are comfortable with sharing. The more you share, the better we will be able to give better suggestions.
Based on inputs from the user and the concerns they highlight in their responses, the mental health resource(s) that is applicable to them will be shown at the end of the form, which is our recommendation.html page.
At the bottom of this recommendations page is a button that will links an html page with a list of all mental health related resources on campus.
In order to go back or to navigate between the questions, for example to change an answer, simply click on the back and forward arrow keys provided by the web browser.
This web application is designed to be case specific to suite the needs of the user in terms of navigating mental health resources on campus.

# The tables at the end
The table at the end displays the mental health resources that would best apply to the person filling out the form. In this table, there will be a space for their phone number, location, hours, and focus.
If no groups were found to be of match, then there will be no table of recommendations, but there will still be a recommendation that the user possibly reach out to Room 13, which is a general purpose mental health resource.

# The full list of resources button
After the table of applicable resources, there is a button that allows the user to view the full list of resources available at Harvard, including contact information, addresses, and other pertinent information.
This full list also includes hotlines that are available 24 hours a day, seven days a week: CAMHS, HUPD, and OSAPR.

# If nothing is entered or no match
If nothing is entered into the text boxes or there is no match, we have accounted for that. If that happens then they will be told that we can't find a specific match, but we will still recommend that if they still feel like they need to talk with someone, then they are free to stop by Room 13 because it is a
general resource, and we also recommend to speak with trusted friends and other trusted people.

# The parsing
This curcial part of the project detects one word entries, for example if someone wants to put that they have not been eating consistently, they may input the words "eating inconsistently". In this case, the key word is inconsistently, thus when it is typed, the parsing mechanism is coded such that it refers the
user to ECHO as a result of the word inconsistently being used ot answer this question.