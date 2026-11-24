import jwt


def decode_jwt(token: str) -> dict:
    return jwt.decode(token, options={"verify_signature": False})

def encode_jwt(payload: dict, secret: str) -> str:
    return jwt.encode(payload, secret, algorithm="HS256")



# jwt_token = (
#     "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9." #HEADER
#     "eyJ1c2VyX2lkIjoxLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3MDAwMDAwMDB9." #PAYLOAD
#     "c2lnbmF0dXJlbm8tdmFsaWRhZGEtcG9yUXVpZXItY29uLXNpZ251bnRlcg" #SIGNATURE
# )
header = {"alg": "HS256", "typ": "JWT"}
payload = {"user_id": 1, "role": "admin", "exp": 1700000000}
secret = "c2lnbmF0dXJlbm8tdmFsaWRhZGEtcG9yUXVpZXItY29uLXNpZ251bnRlcg"

jwt_token = encode_jwt(payload, secret)

payload = decode_jwt(jwt_token)

print(f"\nJWT Token: {jwt_token}\n")

print (f"Decoded JWT Payload: {payload}\n")

print(f"\nContenido del JWT:")
for key, value in payload.items():
    print(f"{key}: {value}")

print(f"\n--------------------------------\n")

payload = {"frase": "AlvaroLovesHater"}

encoded_jwt = encode_jwt(payload, secret)
print(f"Encoded JWT: {encoded_jwt}\n")

decoded_payload = decode_jwt(encoded_jwt)
print(f"Decoded JWT Payload: {decoded_payload}\n")