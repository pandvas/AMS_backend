from rest_framework.test import APITestCase
from django.urls import reverse


from django.test import Client
c = Client()
response = c.post('/login/', {'username': 'john', 'password': 'smith'})


class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url=reverse('regit')  
        self.login_url=reverse('login')

        self.user_data ={"name":"shiwam",
            "email":"pracom",
            "password":"prateek",}
        
        return super().setUp()

    def tearDown(self):
        return super().tearDown()    


class TestSetUp2(APITestCase):

    def setUp(self):
        self.register_url=reverse('ctrd')  

        self.user_data ={"name":"shiwam","description":"takeitttt","email":"hj@hjs.com"}
        return super().setUp()
    def tearDown(self):
        return super().tearDown()        

class RegDepartment(APITestCase):

    def setUp(self):
        self.register_url=reverse('regdepart')  

        self.user_data ={"name":"shiwam"}
        
        return super().setUp()

    def tearDown(self):
        return super().tearDown()     

class RegHod(APITestCase):

    def setUp(self):
        self.register_url=reverse('hodreg')  
        self.user_data ={"name":"shiwam","phone":"98989898989","email":"prateek@gmail.com","id_hod":"1","address":"Noida"}       
        return super().setUp()

    def tearDown(self):
        return super().tearDown()    


class Regfacultyy(APITestCase):
    def setUp(self):
        self.register_url=reverse('regfaculty')  
        self.user_data ={"name":"shiwam","email":"prateek@gmail.com","designation":"developer"}
        return super().setUp()

    def tearDown(self):
        return super().tearDown()         



class Regstudent(APITestCase):

    def setUp(self):
        self.register_url=reverse('regstudent')  
        self.user_data ={"name":"shiwam","email":"prateek@gmail.com","address":"Sector 135 Noida","contactdetails":"9787676566","yearofpassing":"2021"}
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
       


class Regevent(APITestCase):

    def setUp(self):
        self.register_url=reverse('eventreg')  
        self.user_data ={"name":"Alumani Meet","date":"2021-10-25","venue":"Noida Sector 135"}
        return super().setUp()

    def tearDown(self):
        return super().tearDown()   



class Regst(APITestCase):

    def setUp(self):
        self.register_url=reverse('stpass')  
        self.user_data ={"studentid":"Alumani Meet","password":"Noid123"}
        return super().setUp()

    def tearDown(self):
        return super().tearDown()