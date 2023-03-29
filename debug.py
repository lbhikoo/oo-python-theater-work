import ipdb
from lib import *

role1 = Role('The boogey man')
role2 = Role('Jeepers Creepers')


a1=Audition('Brad Pitt', 'New York', False, role1)
a2=Audition('Bruce Willis', 'LA', True, role2)
a3=Audition('Leonardo Dicaprio', 'Florida', False, role2)
a4=Audition('Lebron James', 'Ohio',True, role1)


# the below line allows us to stop & try stuff!
ipdb.set_trace()