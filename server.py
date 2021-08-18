# Import everything from socket
from socket import *

# Define the server port to desired port
serverPort=9872

serverSocket = None
# Start main function
def main():
    global serverSocket
    # Alert user that server is up
    print("the web server is up on port:",serverPort)
    #Loop indefinitely
    while True:
    #Establish the connection
        serverSocket = socket(AF_INET, SOCK_STREAM)
    #Prepare a sever socket
        serverSocket.bind(("",serverPort))
        serverSocket.listen(1)
        print("Ready to serve")

        connectionSocket, addr = serverSocket.accept()
    # Attempt to do following
        try:
        #Recive message on the set up socket
            message = connectionSocket.recv(1024)
        #Output the message
            print (message, "::", message.split()[0],":",message.split()[1])
        # Set desired file as requested file
            filename = message.split()[1]
            print 
            filename,"||",filename[1:]
        # Open the file
            f = open(filename[1:])
        # Read the file
            outputdata = f.read()
    # Do this if an error occurs
        except IOError:
            connectionSocket.send(b"Error 404: File not found")
        # Close connection
            connectionSocket.close()
            pass
        else:
            # Print the file
            print (outputdata)
        #Send one HTTP header line into socket, the b is for bytes.
            connectionSocket.send(b"\nHTTP/1.1 200 OK\n\n")
            #this will encode it into bytes instead of a string
            connectionSocket.send(outputdata.encode())
        # Close connection
            connectionSocket.close()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("something went wrong:", e)
        serverSocket.close()

