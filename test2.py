import imaplib, email

user = 'USER_EMAIL_ADDRESS'

password = 'USER_PASSWORD'

imap_url = 'imap.gmail.com'


# Function to get email content part i.e its body part
def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))

        return msg.get_payload(None, True)


# Function to search for a key value pair

def search(key, value, con):
    result, data = con.search(None, key, '"{}"'.format(value))
    return data