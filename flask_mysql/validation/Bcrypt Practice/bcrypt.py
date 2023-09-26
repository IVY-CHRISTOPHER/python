from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, 
    # which is made by invoking the function Bcrypt with our app as an argument


bcrypt.generate_password_hash('$2b$12$sqjyok5RQccl9S6eFLhEPuaRaJCcH3Esl2RWLm/cimMIEnhnLb7iC')