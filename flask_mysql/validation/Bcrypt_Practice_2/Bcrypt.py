from flask_app import app
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, 
                        # which is made by invoking the function Bcrypt with our app as an argument
bcrypt.generate_password_hash('My Special Password')

print(bcrypt)