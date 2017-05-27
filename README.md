Pehgaam
==============

Simple chat application using Flask and Javascript

How to run
------------------

It is always a good idea using a virtual environment to run your
application. That will avoid interference from your hosting
environment. That can be done using [virtualenv](https://virtualenv.pypa.io/en/stable/):

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ python chat.py

Now open your browser, type `localhost:5000` in your 1st tab.
Fill in your name and the group you want to interact with.

Now open a new tab with the same URL (localhost:5000) and type in
a different name but the same group.

Testing for real time chat.
---------------------------

Post your message on the 1st tab. You'll be able to see it on both tabs.
Similarly, anything that that you post on the 2nd tab will be visible on the 1st tab.

> :)
