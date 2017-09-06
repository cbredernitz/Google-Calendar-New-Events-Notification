# Google-Calendar-New-Events-Notification
This program looks at your personal Google Calendar and informs you in your terminal what your calendar looks like and who is attending.  In order for this to only show current events, after each run the program writs a txt file to compare it's new results to the old results.
This program runs off of your Google Calendars events to show what has changed from the previous time running the script, to what the live data shows. It does this by first setting up your credentials by running the get_credentials() function provided by Google in the quickstart.py file. The rationale behind this program is to highlight the changes in events since Google Calendars doesn't always send you notifications to events being canceled or attendees changing. It does this by pulling live information from your Google Calendars and writing a text file of the information to then iterate through and use to compare.  The output will be a string containing the information of the event that has been changed.  The program may give errors when trying to run off Python 2.7.  This is because when I had to create a virtual environment to install the Google packages, it made my terminal run off python 3.6.

*If you want to change the desired  max number of events returned, change maxResults variable on line 71

2. Explain exactly what needs to be done to run your program (what file to run, anything the user needs to input, anything else) and what we should see once it is done running (should it have created a new text file or CSV? What should it basically look like?).
(Your program running should depend on cached data, but OK to write a program that would make more sense to run on live data and tell us to e.g. use a sample value in order to run it on cached data.)

	In order to run this code, first you will need to pip install some packages.  The first will be httplib2, the second will be virtualenv (will talk more about this step if needed below), and the last will be the package from Google.  To install this last one type into your terminal window, as you would normally pip install, ‘pip install --upgrade google-api-python-client’.  Next, you will need to get your client_secret.json from Google.  I will be laying out the instructions on how to get this file, however, they can also be found at ‘https://developers.google.com/google-apps/calendar/quickstart/python'. Step one, Use this wizard(found at the above link) to create or select a project in the Google Developers Console and automatically turn on the API. Click Continue, then Go to credentials. Next, on the Add credentials to your project page, click the Cancel button. At the top of the page, select the OAuth consent screen tab. Select an Email address, enter a Product name if not already set, and click the Save button. Select the Credentials tab, click the Create credentials button and select OAuth client ID.  Select the application type Other, enter the name "Google Calendar API Quickstart", and click the Create button.  After, click OK to dismiss the resulting dialog. Finally, click the file_download (Download JSON) button to the right of the client ID.  Move this file to your working directory and rename it client_secret.json.  It is important that you name the file ‘client_secret.json’ since the code will not run without it named correctly.
	After obtaining the ‘client_secret.json’ file and moving it into your working folder, run the quickstart.py program.  This program was provided by Google and can be found on the step-by-step instructions on the webpage provided above. Do not copy and paste their quickstart.py since I have provided it for you. This file will attempt to open a webpage.  If it doesn’t then copy the URL in the terminal into an open tab.  The webpage that you are directed to will prompt you to sign into your Google account.  If there are multiple accounts then it will ask you to select one for authorization.  After completing this step you have now gained access to fetching data from your Google calendar. 
	Now you are ready to run the main program ‘Google_Calendars_Compare_si106.py’.  You will need to run the program one time before being able to see a comparison since it needs to be able to cache your information as a text file named ‘previous_cache.txt’.  This text file described previously should now be created and visible in your working folder.  Now every time you run the program it will show the events that are no longer in your cache or added to your live data in the terminal window.  Below that you will see a statement for each event showing the key information of the event.
	
****This part is if you need to create a virtual environment in order to run the program.  This is needed if the Google api package is not installing correctly.  First, you will need to ‘pip install virtualenv’  Next, you will want to cd to your working directory.  You will do this by typing into your terminal window ‘cd’ followed by the path of your working folder.  After that, you will need to create an environment by typing into your terminal window ‘virtualenv’ followed by whatever name you would like to give it (Ex. ‘virtualenv venv’ would create an environment named ‘venv’).  Now that you have a virtual environment created you will need to activate it by typing in ‘source venv/bin/activate’ (In the case of this example, I used ‘venv’ when activating.  You would replace ‘venv’ with whatever you named your environment).  If these steps are done correctly then you will see the virtual enviornemnt name in () before your command line in your terminal. Finally, you will need to pip install your needed models below again in this virtualenv.  As it was stated before make sure that you have Python 3.6 active.  My virtualenv says that it is operating with 2.7, however the syntax behaves in Python 3.6.

3. List all the names of the files you are turning in, with a brief description of each one. (At minimum, there should be 1 Python file, 1 file containing cached data, and the README, but if your project requires others, that is fine as well! Just make sure you have submitted them all.)

	I am turning in the main python file named ‘Google_Calendars_Compare_si106.py’, the ‘quickstart.py’ to gain the credentials provided by Google, and an example of my events.  You do not need this txt file ‘previous_cache.txt’ in the working dictionary since the program will re-write on specific to your calendar. However, I am including the text file as an example of what you should be seeing.

4. Any Python packages/modules that must be installed in order to run your project (e.g. requests …):

pip install requests
pip install httplib2
pip install virtualenv (if needed)
pip install --upgrade google-api-python-client

5. What data sources did you use? Provide links here and any other description necessary.

	The data source I used were the following links all provided by Google as well as my own personal Google Calendar:

https://developers.google.com/google-apps/calendar/quickstart/python
https://developers.google.com/google-apps/calendar/v3/reference/events
	-This shows how the events dictionary is categorized

http://docs.python-guide.org/en/latest/dev/virtualenvs/
	
	Another source I used was part of the code for fetching the data from Google shown under the commented out main() contained in quickstart.py.

6. Approximate line numbers in Python file to find the following mechanics requirements: - 

Sorting with a key function: - line 90 + 97

Class definition: - line 29

Creating instance of a class: - line 80-82 

Calling methods on a class instance (list all line numbers where you invoke any method on a class instance): - lines 104-107

Beginnings of each class method definition: - lines 30, 41, 51

(If applicable) Beginnings of each function definition outside classes: - lines 72, 79, 86, 93, 100

Beginning of code that handles:
	data caching: - lines 119 - 134

	using cached data: - lines 93-97, 104, 107, 109

Test cases: lines 138 - 150


8. Rationale for project: why did you do this project? Why did you find it interesting? Did it work out the way you expected?

	I chose this project because it was interesting to use the Google API.  It was something that I personally wanted to work with since it was a challenge and it was something that would be useful to many people if completed.  Professor Resnick came up with the idea since it was something that could be used by the School of Information to pull calendar updates not easily shown before.  It was interesting to me since I plan on working with Google API in the future on personal code.  It was also interesting since it is a more complicated API to tackle and would be a challenge to work with and develop. I plan on applying to the MSI program here at the University of Michigan and wanted to make something that could be utilized by people on a day-to-day basis.  It didn't come out the way I originally hoped in that it highlights all of the differences between events, but I am happy with what it does accomplish. I plan on working on it more in my free time to get it to behave the way I want in the near future.
