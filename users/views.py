from django import template
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.conf import settings
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import *
import jwt
#for authentication and permission
from rest_framework.permissions import IsAuthenticated,AllowAny

from rest_framework import status
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


import logging
logger = logging.getLogger(__name__)


# def Registerget(request):
#     return render(request,"r.html")
# class RegisterView(APIView):
#     def post(self, request):
#         serializer=UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         #check=send_mail('MailHeader','MailMessgae','psfns.rc@gmail.com',['ptcsam74@gmail.com'],fail_silently=False)
#         html_content=render_to_string('emails.html',{'title':'title','content':'content'})
#         text_content=strip_tags(html_content)
#         email=EmailMultiAlternatives(
#         #subject
#         "Testing",
#         #content
#         text_content,
#         #from Email
#         settings.EMAIL_HOST_USER,
#         #listof Reciepent
#         ['raj.sandip96@gmail.com'])
#         email.attach_alternative(html_content,"text/html")
#         email.send()

#         return HttpResponse("Email Send Successfully")
    # return Response(serializer.data)

class RegisterUniversityView(APIView):
    
    def post(self, request):
        try:
            serializer=UniversitySerializer(data=request.data)
            serializer.is_valid()
            serializer.save()
            # return render(request)
        except:
            print('except block')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    
        return Response({"message":"posted the data successfully"})

        # return render(request, 'f2.html')

class Universitylist(APIView):
    permission_classes = (IsAuthenticated,)
    # permission_classes = [AllowAny]
    def get(self, request):
        students = University.objects.all()
        serialized = UniversitySerializer(students, many=True)
        return Response(serialized.data)



from datetime import datetime
import pytz
UTC = pytz.utc
IST = pytz.timezone('Asia/Kolkata')

class Studentlist(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request):
    #     print("IST in Default Format : ",
    #   datetime.now(IST))
        logger.info('>>>>>>>>>>>>>>>Sample message')
        # logger.info(datetime.now(IST))
        students = Student.objects.all()
        serialized = StudentSerializer(students, many=True)
        return Response(serialized.data)



class Roll_list(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request):
        students = Rollno_mapper.objects.all()
        serialized = RollNoMapperSerializer(students, many=True)
        return Response(serialized.data)


class RegisterDepartmentView(APIView):
    #permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer=DepartmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        logger.info('>>>>>>>>>>>>>>>Sample message')
        serializer.save()
        return Response(serializer.data)


class Departmentlist(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self,request):
        # print("hjhdsuuu")
        snippets = Department.objects.values('id','name')
        serializer = DepartmentSerializer(snippets, many=True)
        return Response(serializer.data)


class RegisterHodView(APIView):
    #permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer=HodSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class Hodlist(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self,request):
        snippets = Hod.objects.all()
        serializer = HodSerializer(snippets, many=True)
        return Response(serializer.data)

# GET FACUILTY
class FacuiltytGet(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self,request):
        snippets = Faculty.objects.all()
        serializer = FacultySerializer(snippets, many=True)
        return Response(serializer.data)


class RegisterFacultyView(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer=FacultySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class RegisterStudentView(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer=StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class RegisterCourseView(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer=CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

# get event
class EventGet(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        snippets = Event.objects.all()
        serializer = EventSerializer(snippets, many=True)
        return Response(serializer.data)


class RegisterEventView(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer=EventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class EventpollView(APIView):
    def post(self, request):
        serializer=EventpollSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class StudentPasswordView(APIView):
    def post(self, request):
        serializer=StudentPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class ContactView(APIView):

    def post(self, request):
        serializer=ContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class DepartmentMapperView(APIView):
    def post(self, request):
        serializer=DepartmentMapperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class FacultyMapperView(APIView):
    def post(self, request):
        serializer=FacultyMapperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class StudentMapperView(APIView):
    def post(self, request):
        serializer=StudentMapperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class RollNoMapperView(APIView):
    def post(selfself, request):
        serializer=RollNoMapperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class EventMapperView(APIView):
    def post(selfself, request):
        serializer=EventMapperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

from rest_framework_simplejwt.views import TokenObtainPairView


from rest_framework.renderers import TemplateHTMLRenderer

class LoginView(TokenObtainPairView):
    # permission_classes = (AllowAny,)
    serializer_class = AuthenticationSerializer




# class UserView(APIView):
#     # permission_classes = (IsAuthenticated,)
#     def get(self, request):
#         token=request.COOKIES.get('jwt')
#         if not token:
#             raise AuthenticationFailed('Unauthenticated')
#         try:
#             payload=jwt.decode(token, 'secretMessage', algorithms=['HS256'])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated')

#         user =User.objects.filter(id=payload['id']).first()
#         serializer=UserSerializer(user)
#         return Response(serializer.data)

# class LogoutView(APIView):

#     def post(self, request):
#         response=Response()
#         response.delete_cookie('jwt')
#         response.data={
#             'message':'Logout SuccessFull'
#         }
#         return response



from rest_framework import status
class UserViewSet3(APIView):
    def get_obj(self,id):
        try:
            print("11")
            return Faculty.objects.get(id=id)

        except Faculty.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        obj = self.get_obj(id=id)
        print("222")
        serializer = FacultySerializer(obj)
        return Response(serializer.data)

    def put(self,request,id):
        print("3333")
        obj = self.get_obj(id)
        print(obj.id)
        serializer = FacultySerializer(obj,data=request.data)
        if serializer.is_valid():
            print("111")
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)




class departmentUpdate(APIView):
    def get_obj(self,id):
        try:
            print("11")
            return Department.objects.get(id=id)

        except Department.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        obj = self.get_obj(id=id)
        print("222")
        serializer = DepartmentSerializer(obj)
        return Response(serializer.data)

    def put(self,request,id):
        print("3333")
        obj = self.get_obj(id)
        print(obj.id)
        serializer = DepartmentSerializer(obj,data=request.data)
        if serializer.is_valid():
            print("111")
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


class Universityupdate(APIView):
    def get_obj(self,id):
        try:
            print("11")
            return University.objects.get(id=id)

        except University.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        obj = self.get_obj(id=id)
        print("222")
        serializer = UniversitySerializer(obj)
        return Response(serializer.data)

    def put(self,request,id):
        print("3333")
        obj = self.get_obj(id)
        print(obj.id)
        serializer = UniversitySerializer(obj,data=request.data)
        if serializer.is_valid():
            print("111")
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)





class Universitydelete(APIView):
    def get_obj(self,id):
        try:
            return University.objects.get(id=id)

        except University.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        obj = self.get_obj(id=id)
        serializer = UniversitySerializer(obj)
        return Response(serializer.data)
        # return render(request,'updateFaculty.html')


    def delete(self,request,id):
        obj = self.get_obj(id)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        # return render(request,'showFaculty.html')       





class UserViewSetDel(APIView):
    def get_obj(self,id):
        try:
            return Faculty.objects.get(id=id)

        except Faculty.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        obj = self.get_obj(id=id)
        serializer = FacultySerializer(obj)
        # return Response(serializer.data)
        return render(request,'updateFaculty.html')


    def delete(self,request,id):
        obj = self.get_obj(id)
        obj.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)
        return render(request,'showFaculty.html')





class departmentSetDel(APIView):
    def get_obj(self,id):
        try:
            return Department.objects.get(id=id)

        except Department.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        obj = self.get_obj(id=id)
        serializer = DepartmentSerializer(obj)
        return Response(serializer.data)


    def delete(self,request,id):
        obj = self.get_obj(id)
        obj.delete()
        return render(request,'showDepartment.html')


# student
class studentUpdate(APIView):
    def get_obj(self,id):
        try:
            print("11")
            return Student.objects.get(id=id)

        except Student.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        obj = self.get_obj(id=id)
        print("222")
        serializer = StudentSerializer(obj)
        return Response(serializer.data)

    def put(self,request,id):
        print("3333")
        obj = self.get_obj(id)
        print(obj.id)
        serializer = StudentSerializer(obj,data=request.data)
        if serializer.is_valid():
            print("111")
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)



# event curd

class eventUpdate(APIView):
    def get_obj(self,id):
        try:
            print("11")
            return Event.objects.get(id=id)

        except Event.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        obj = self.get_obj(id=id)
        print("222")
        serializer = EventSerializer(obj)
        return Response(serializer.data)

    def put(self,request,id):
        print("3333")
        obj = self.get_obj(id)
        print(obj.id)
        serializer = EventSerializer(obj,data=request.data)
        if serializer.is_valid():
            print("111")
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


# event del
class EventDel(APIView):
    def get_obj(self,id):
        try:
            return Event.objects.get(id=id)

        except Event.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        obj = self.get_obj(id=id)
        serializer = EventSerializer(obj)
        return Response(serializer.data)
        # return render(request,'updateFaculty.html')


    def delete(self,request,id):
        obj = self.get_obj(id)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        # return render(request,'showFaculty.html')


# student del
class StudentDel(APIView):
    def get_obj(self,id):
        try:
            return Student.objects.get(id=id)

        except Student.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        obj = self.get_obj(id=id)
        serializer = StudentSerializer(obj)
        return Response(serializer.data)
        # return render(request,'updateFaculty.html')


    def delete(self,request,id):
        obj = self.get_obj(id)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        # return render(request,'showFaculty.html')



def vote(request):
    return render(request, 'vote.html')







from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
import jwt, datetime


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# class LoginView(APIView):
#     def post(self, request):
#         email = request.data['email']
#         password = request.data['password']

#         user = User.objects.filter(email=email).first()

#         if user is None:
#             raise AuthenticationFailed('User not found!')

#         if not user.check_password(password):
#             raise AuthenticationFailed('Incorrect password!')

#         payload = {
#             'id': user.id,
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#             'iat': datetime.datetime.utcnow()
#         }

#         token = jwt.encode(payload, 'secret', algorithm='HS256')

#         response = Response()

#         response.set_cookie(key='jwt', value=token, httponly=True)
#         response.data = {
#             'jwt': token
#         }
#         return response


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response


from .models import Event_mapper
from rest_framework.decorators import api_view
@api_view(['GET','POST'])
def complaint(request):
	if request.method == 'GET':
		queryset= Event_mapper.objects.values('id')
		return Response(queryset)

	if request.method == 'POST':
		ordernumber1 = request.data['id']
		queryset = Department.objects.values('name').filter(id=ordernumber1)
		return Response(queryset)



from .models import Poll2
from .serializers import Poll2Serializer
class poll2view(APIView):
    def get(self,request):
        snippets = Poll2.objects.all()
        serializer = Poll2Serializer(snippets, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = Poll2Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            context={"message":"Data posted successully"}
            return Response(context)
	    
