from rest_framework import serializers
from .models import User,University,Department,Hod,Faculty,Student,Course,Event, Eventpoll, StudentPassword,Contact,Department_mapper,Faculty_mapper, Student_mapper, Rollno_mapper, Event_mapper
from django.contrib.auth import password_validation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','name','email','password']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def create(self, validated_data):
        # Extracting the password
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model=University
        fields=['id','name','address','password','email']


    def validate(self, value):
        if value['name']:
            for n in value['name']:
                if n.isdigit():
                    raise serializers.ValidationError({"error":"UNIVERSITY NAME CAN NOT CONTAIN NO"}, code=None)

        
        if len(value['address']) < 5:
                raise serializers.ValidationError({"error":"Adddd"})   
  

                
        return value
    # def validate_password(self,value):
    #     password_validation.validate_password(value,self.instance)
    #     return value
       
        
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields=['id','name']

    def validate(self, value):
        if value['name']:
            for n in value['name']:
                if n.isdigit():
                    raise serializers.ValidationError({"error":"DEPARTMENT NAME CAN NOT CONTAIN NO"}, code=None)

        return value    

class HodSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hod
        fields=['id','name','phone','email','id_hod','address']

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model=Faculty
        fields=['id','name','email','designation']

    def validate(self, value):
        if value['name']:
            for n in value['name']:
                if n.isdigit():
                    raise serializers.ValidationError({"error":"FACULTY NAME CAN NOT CONTAIN NO"}, code=None)

        
        # if len(value['designation']) < 5:
        #         raise serializers.ValidationError({"error":"ENTER VALID DESIGNATION!"})
                
        return value    

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','name','email','address','contactdetails','yearofpassing']

    def validate(self, value):
        if value['name']:
            for n in value['name']:
                if n.isdigit():
                    raise serializers.ValidationError({"error":"FACULTY NAME CAN NOT CONTAIN NO"}, code=None)

        
        if len(value['address']) < 5:
                raise serializers.ValidationError({"error":"ENTER VALID ADDRESS!"})

        if ((value['yearofpassing'] < 2000) or (value['yearofpassing'] > 2021)):
                raise serializers.ValidationError({"error":"ENTER VALID YOP!"})     

        if len(value['contactdetails']) < 10:
                raise serializers.ValidationError({"error":"ENTER VALID DETAILS!"})           
                
        return value    

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=['name','departmentid']
from datetime import date


# print("Today's date:", today)

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=['id','name','date','venue']

    def validate(self,value):
        today = date.today()
        if value['date']< today:
             raise serializers.ValidationError({"error":"Event cannot be in past date!"})  
        return value

                

class EventpollSerializer(serializers.ModelSerializer):
    class Meta:
        model=Eventpoll
        fields=['id','interested','eventid','studentid']

class StudentPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentPassword
        fields=['studentid','password']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields=['name','email','description']



#--------------------------------------------------------------------

class DepartmentMapperSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department_mapper
        fields=['departmentid','universityid','hodid']

class FacultyMapperSerializer(serializers.ModelSerializer):
    class Meta:
        model=Faculty_mapper
        fields=['facultyid','departmentid','universityid']

class StudentMapperSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student_mapper
        fields=['studentid','courseid','universityid','departmentid']

class RollNoMapperSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rollno_mapper
        fields=['rollno','studentid']

class EventMapperSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event_mapper
        fields=['eventid','departmentid']
        
                
# logic for authentication    
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer       
class AuthenticationSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)
        

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['id'] = self.user.id
        data['email'] = self.user.email
        data['username'] = self.user.username

        return data

from  .models import Poll2
class Poll2Serializer(serializers.ModelSerializer):
    class Meta:
        model=Poll2
        fields=['option']