from .audition import Audition

class Role:
    def __init__(self,character):
        self.character = character

    @property
    def auditions(self):
        return [a for a in Audition.all if a.role == self]

    @property
    def actors(self):
        # return list({a.location for a in self.auditions})
        return[a.actor for a in self.auditions]
    
    @property
    def locations(self):
        return [a.location for a in self.auditions]
    

    @property
    def lead(self): 
        list_of_lead_hires = [l.actor for l in self.auditions if l.hired == True]
        # assign to variable instead of using comprehension list 2x
        if list_of_lead_hires:
            return list_of_lead_hires[0]
        else:
            return "no actor has been hired for this role"
        
    
    @property
    def understudy(self):
        list_of_hires = [l.actor for l in self.auditions if l.hired == True]
        if len(list_of_hires) >= 2:
            return list_of_hires[1]
        else:
            return "no actor has been hired for understudy for this role"
        
    # Role#understudy` returns the second instance of the audition that was hired
        

    
        
    
    


#Roles should only have a character_name (string) and have many auditions.


#auditions returns all of the auditions associated with this role.
#actors returns a list of names from the actors associated with this role.
#locations returns a list of locations from the auditions associated with this role.
#lead returns the first instance of the audition that was hired for this role or returns a string 'no actor has been hired for this role'.
#understudy returns the second instance of the audition that was hired for this role or returns a string 'no actor has been hired for understudy for this role'.