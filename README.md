# messageboard
Global anonymous message board

High level overview:
This Python-based web application serves as a simple solution for a global anonymous message board allowing users to post messages that are displayed from most to least recent. The applications consists of a Python file implementing the server side logic, an HTML file mapping out the style and structure of the webpage, and a text file, 'entries.txt' to store posted messages with their corresponding timestamps. 

Python File ('main.py'):
The Python file implements the 'HTTPServer' class from http.server. The request handler class MessageBoardHandler inherits from BaseHTTPRequestHandler. The do_GET method handles GET requests on the root page ('/'), writing into the HTML file 'messageboard.html' the messages from the text file 'entries.txt' as list elements in an unordered list. If the path is not the root path, it sends an error response. The do_POST method handles POST requests from the post page ('/post'), allowing users to submit new messages. It makes sure that the length of the entered message is at most 128 characters and then adds a UTC-zone timestamp in ISO format along with the message to the 'entries.txt' file. The server listens on port 8000 and runs indefinitely. 

HTML File ('messageboard.html'):
The HTML file provides the structure and styling of the webpage. It includes a title, a form with a textarea and submit button, and the sent-in messages. It leaves the div with class "center," as well as the head and body tags, open to allow for the messages to be written into continuously, with the closing tags in the python file. The HTML file also includes CSS styling and Javascript, specifying how to display the timestamps from the 'entries.txt' file, the title, the form submission, and the list elements/messages.

Text File ('entries.txt'):
The 'entries.txt' file stores posted messages and timestamps so that in the case of a server restart, messages are retained. They are styled with span tags to be styled/formatted using class selectors, as well as having <br> to place the message and timestamp on separate lines.

User Interaction Flow:
Users access the message board on the replit webpage, https://messageboard.wangamy3.repl.co/, where they can input messages in the provided textarea. When the user hits send, a POST request is sent to the server, where the message is validated and then appended to 'entries.txt' with a timestamp. The server redirects the suer back to the root path, and the updated message list is displayed through HTML structure/styling.

Fulfilling the requirements:
Users are able to type a message and post it to the message board through the form element in the HTML file and the do_POST method in the Python file. Because the textarea element has 'required' and a maxlength of 128, users can't submit an empty or longer than 128 character message. The python code also ensures the message is not empty or longer than 128 characters, sending a 400 response code in those cases. Users can see the messages on the message board from most to least recent because the messages are added to the html file in reverse order as list elements in the python code. Users on different computers can post to the same board and view each other's messages through the replit host webpage, created using the instructions below.

How to start the application: 
To start the application, create a new Replit by signing in or creating an account at https://replit.com/, clicking the "Create Repl" button, and creating a Python file named main.py to paste the code from the GitHub main.py file into. Then, create a new file named messageboard.html in the same Repl and paste the code from the messageboard.html file into it. Finally, create an empty text file named 'entries.txt' in the same Repl. Once those three files have been added, open the '.replit' file and either set the run field to python main.py, ex. run = ["python3", "main.py"], or ensure that the run field is set to python main.py, to specify the "Run" command. Finally, click the "Run" button and click the "Open in a new tab" button for a web preview. Other users can test by going to the link provided by Replit, which will look like https://your-replit-name.your-replit-username.repl.co. Once the "Stop" button on replit is clicked, the webpage will not be available anymore. Alternatively, go to https://replit.com/@wangamy3/messageboard?v=1 and click the green "Run" button, where the webpage will be hosted on https://messageboard.wangamy3.repl.co/ for users until stopped.
