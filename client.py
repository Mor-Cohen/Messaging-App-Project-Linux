import requests

def create_user(username):
    response = requests.post('http://192.168.110.130:5000/users', json={'username': username})
    print(response.json())

def send_message(sender_id, recipient_id, content):
    response = requests.post('http://192.168.110.130:5000/messages', json={'sender_id': sender_id, 'recipient_id': recipient_id, 'content': content})
    print(response.json())

def get_messages(recipient_id):
    response = requests.get(f'http://192.168.110.130:5000/messages?recipient_id={recipient_id}')
    for message in response.json():
        print(message)

def mark_message_as_read(message_id):
    response = requests.patch(f'http://192.168.110.130:5000/messages/{message_id}')
    print(response.json())
