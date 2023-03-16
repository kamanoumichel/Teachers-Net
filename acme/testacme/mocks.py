from django.http import Http404
class Post():
    POSTS=[
        {'id':1,'title':'First Post','body':'This is my first post'},
        {'id':2,'title':'Second Post','body':'This is my second post'},
        {'id':3,'title':'third Post','body':'This is my third post'},
    ]

    @classmethod
    def all(cls):
        return cls.POSTS
    @classmethod
    def find(cls,id):
        try:
            return cls.POSTS[int(id)-1]
        except:
            raise Http404("Sorry| Post#{} Don't exist".format(id))

#Tout les methodes de classe doivent avoir cls comme premier parametre c'est une 
#Convention et tout les methodes d'instances doivent avoir comme premier parametre self
#Ce sont les conventions de python.