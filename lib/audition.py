
# Auditions should have an actor (string), 
# location (string), hired (boolean) 
# and belong to a role.

#Audition#role returns an instance of role associated with this audition.



class Audition:
    all = []
    def __init__(self, actor,location,hired,role):
        self.actor = actor
        self.location = location
        self.hired= hired
        self.role = role
        Audition.all.append(self)

    
    def call_back(self):
        self.hired = True 


    #Audition#call_back() will change the the hired attribute to True.