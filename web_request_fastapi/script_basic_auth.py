import base64

def decode_basic_auth(auth_header: str):
    if not auth_header.startswith("Basic "):
        raise ValueError("Invalid Basic Auth header")
    
    encoded_credentials = auth_header.split(" ")[1]
    decoded_bytes = base64.b64decode(encoded_credentials)
    decoded_credentials = decoded_bytes.decode("utf-8")
    
    username, password = decoded_credentials.split(":", 1)
    return username, password

header = "Basic YWx2YXJvOnBhc3N3b3JkMTIz" # This is the Base64 encoded string for "alvaro:password123"
username, password = decode_basic_auth(header)
print(f"Username: {username}, Password: {password}")