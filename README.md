How to make project work:

Since the code is pretty much done for you and explained with the comments. All you have to make sure is that you have Python installed on your operating system. 

Step 1: Open VSCODE where code is at. \n
Step 2: Open Command Prompt or use the python terminal on VSCODE
Step 3: Run the server.py file on command prompt or either VSCODE, to the run the server just do "py server.py". A message should pop up saying "Server is on port: 9872, Ready to Serve".
Step 4: Open up a broswer and search, "http://localhost:9872/test.html"
Step 5: It should work and on page say, "I AM HERE!" or maybe a poem? I should make it interesting.
Step 6: If it fails, a 404 Error will pop up letting you know.
Step 7: Smile, cause you just opened up a server.

In this assignment, you will develop a simple Web server in Python that is capable
of processing only one request. Specifically, your Web server will
(i) Create a connection socket when contacted by a client (browser)
(ii) Receive the HTTP request from this connection
(iii) Parse the request to determine the specific file being requested
(iv) Get the requested file from the server’s file system
(v) Create an HTTP response message consisting of the requested file
preceded by header lines
(vi) Send the response over the TCP connection to the requesting browser.
If a browser requests a file that is not present in your server, your server should
return a “404 Not Found” error message.
Your job is to code the steps above, run your server, and then test your server by
sending requests from browsers running on different hosts. If you run your server
on a host that already has a Web server running on it, then you should use a different
port than port 80 for your Web server.
 Make sure to test your program before submission, if your programs contains
syntax errors, the grade is zero.
 Include a README file for instructions on how to run your program.
 Documentation, write comments in your source code so that anyone reading
your code will be able to understand it.
 Submit the zip file through private post on Piazza
 Name your zip file as 379-yourlastname.zip


