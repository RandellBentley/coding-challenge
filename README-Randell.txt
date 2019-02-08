#Coding Challenge App

I've created a basic app for creating links for websites and keeping track of how many clicks each website currently has.

In the table each added website becomes a link for the landing page where it will display the name and number of clicks.

I've added the ability to edit the link title and the number of clicks.

I used IntegrityError along with setting the model which contains the link title to require it to be unique in,
in order to prevent naming conflicts.

I added a home button to direct the user back to the home page after clicking on the link for a page.

I used rest_framework even though I am relatively new to it. I followed a few tutorials to put in a basic model
employing the framework. Although, when I put in the router.url portion into my linkApp/urls.py file (line 21) I
was able to view the api for the serialized models but wasn't sure how this fits into the bigger picture so I've
commented that portion out. I didn't want to delay the deployment any longer but I'd like to go back and research
the rest_framework more to see how it is commonly used.
