# from .test_setup import TestSetUp2,TestSetUp,RegDepartment,Regfacultyy,RegHod,Regstudent,Regcourse
from .test_setup import *

class TestViews(TestSetUp):
    def test_user(self):
        res=self.client.post(self.register_url)
        self.assertEqual(res.status_code,400)


    # def test_user_can_register_correctly(self):
    #     res=self.client.post(self.register_url,self.user_data,format="json")
    #     self.assertEqual(res.status_code,201)  




class TestViews2(TestSetUp2):
    def test_user_c(self):
        res=self.client.post(self.register_url)
        self.assertEqual(res.status_code,400)

    # def test_user_can_register_correctly(self):
    #     res=self.client.post(self.register_url,self.user_data,format="json")
    #     self.assertEqual(res.status_code,201)

class regDepartmentTest(RegDepartment):
    def test_user_ca(self):
        res=self.client.post(self.register_url)
        self.assertEqual(res.status_code,400)

class regHodTest(RegHod):
    def test_user_ca(self):
        res=self.client.post(self.register_url)
        self.assertEqual(res.status_code,400)        


class regFacultyTest(Regfacultyy):
    def test_user_ca(self):
        res=self.client.post(self.register_url)
        self.assertEqual(res.status_code,400) 

class regStudentTest(Regstudent):
    def test_user_ca(self):
        res=self.client.post(self.register_url)
        self.assertEqual(res.status_code,400)    

           

class regEventTest(Regevent):
    def test_user_ca(self):
        res=self.client.post(self.register_url)
        self.assertEqual(res.status_code,400)


class Regst(Regst):
    def test_user_ca(self):
        res=self.client.post(self.register_url)
        self.assertEqual(res.status_code,400)        