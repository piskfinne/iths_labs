from cryptography.fernet import Fernet

def generate_key():
    """
    Generates a new symmetric encryption key using the Fernet module and saves it to a file.
    """
    
    # Generate a symmetric encryption key using the Fernet module
    key = Fernet.generate_key()
    
    # Open (or create) a file named 'key_file.key' in write-binary mode ('wb') to store the key
    with open("key_file.key", "wb") as key_file:
        
        # Write the generated key to the file
        key_file.write(key)
    
    # Print confirmation that the key has been successfully generated and saved
    print(f"Encryption key generated and saved to key_file.key")

# Check if the script is being run directly (not imported as a module) and call generate_key()
if __name__ == "__main__":
    generate_key()
