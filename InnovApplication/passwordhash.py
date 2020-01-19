import hashlib, binascii, os


def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

print(hash_password("Inn0v@te!"))

def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

print(verify_password("c8de4afd226e649f555c1c8eb60fdea5391ef0bdfec6f5f2b1f55fb8e730ae491b1721cb9644294cd78faa07143c7678aad4596b1404f7faa86a6b1bacc742797804b19d5ddee0142b06b68f55277e3bc619e486f2f4bceb4c93f4829029e0cf", "Inn0v@te!"))