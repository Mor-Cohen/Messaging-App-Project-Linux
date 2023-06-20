# Messaging-App-Project-Linux
Linux Messenger - A  efficient messaging application for seamless communication between Linux machines, offering features such as user creation, message sending, retrieval, and read status tracking


## Installing:

### Server:
- Make sure you have Python and pip installed on your machine.


        sudo yum update
        sudo yum install python3
        sudo yum install python3-pip
- Install Flask and SQLAlchemy.
        
        pip3 install flask flask_sqlalchemy
### Client:
- Make sure you have Python and pip installed on your machine.
        
        sudo yum update
        sudo yum install python3
        sudo yum install python3-pip
    
- Install the requests library.
    
        pip3 install requests
- Open the client.py file and update the IP to your server IP.
### Server VM:
Navigate to the directory of the app.py file.
- Open a terminal and run the following command:
    ```bash
    python3 app.py
Now the server is running.

### Client VM:
Navigate to the directory of the client.py file.
- Open a terminal and run the following commands:
    ```bash
    python3
    from client import create_user, send_message, get_messages, mark_message_as_read
Now you can create users, send messages, read messages, and mark them as read.

#### Commands:
- To create a user:
    ```bash
    create_user("user")
    
- To send a message:
    ```bash
    send_message("sender", "receiver", "message")
- To retrieve messages for a recipient:
    ```bash
    get_messages("receiver")
- To mark a message as read (provide the message ID):
    ```bash
    mark_message_as_read(message_id)
