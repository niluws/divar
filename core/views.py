import ghasedakpack
from random import randint
from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import User, PhoneOtp
from uuid import uuid4
from rest_framework.authtoken.models import Token

sms = ghasedakpack.Ghasedak("d05a1073f01cf408a3358b9bd919d29ed1502685dbedd00474ac917a01b23af3")
template = "randcode"
# param1 = "تست 1"
receptor = "09385118659"
type = '1'


class ValidatePhoneNumber(APIView):
    '''This class view takes phone number
    if it doesn't  already exists then it sends otp for coming phone numbers then redirect to register view, and
    if it does then sent otp and redirect to verify existed user and login '''

    def get(self, request):
        return Response({'please enter your phone number'})

    def post(self, request, *args, **kwargs):
        token = str(uuid4())
        phone_number = request.data.get('phone_number')
        if phone_number:
            token = str(uuid4())
            phone = phone_number
            if User.objects.filter(phone_number=phone):
                user = User.objects.get(phone_number=phone)
                send_otp(phone, token)
                return HttpResponseRedirect(
                    reverse('account:validate_exist_user') + f'?token={token}&user_id={user.id}')
            else:
                send_otp(phone, token)
                return HttpResponseRedirect(reverse('account:register') + f'?token={token}')
        else:
            return Response({" please enter your phone number "})


class UserRegisterView(APIView):
    def get(self, request):
        return Response({'now rgister by otp code'})

    def post(self, request):
        recived_otp_code = request.data.get('otp_code')
        username = request.data.get('username')
        request_token = request.GET.get('token')
        if PhoneOtp.objects.filter(token=request_token, otpcode=recived_otp_code).exists():
            phoneotp = PhoneOtp.objects.get(token=request_token)
            user = User.objects.create(phone_number=phoneotp.phone_number, username=username)
            phoneotp.delete()
            id = User.objects.get(username=username).id
            token = user_login_token(id)
            return Response({f'token :{token} '})
        else:
            return Response({" wrong code "})


class ValidateExistUser(APIView):
    '''if user try to register with a existing phone number then he/she will redirect to this view and recived
    a otp_code then by giving that code will login'''

    def get(self, request):
        return Response({'your phone number already exist please send us your otp code  then you are logined'})

    def post(self, request):
        request_user_id = request.GET.get('user_id')
        recived_otp_code = request.data.get('otp_code')
        request_token = request.GET.get('token')
        phoneotp = PhoneOtp.objects.get(token=request_token, otpcode=recived_otp_code)
        if phoneotp:
            id = User.objects.get(id=request_user_id).id
            token = user_login_token(id)
            phoneotp.delete()
            return Response({f'token :{token} '})
        else:
            return Response({'wrong otpcode'})


def send_otp(phone, token):
    '''this function takes a phone number and token and create  a rondom code and create instance from PhoneOtp model then send code with sms'''
    if phone:
        print(phone)
        key = randint(1000, 9999)
        sms.verification({'receptor': '09385118659','type': '1','template': 'randcode','param1': key})
        PhoneOtp.objects.create(phone_number=phone,
                                otpcode=key,
                                token=token)
        return key
    else:
        return False


def user_login_token(id):
    '''this function will take a user id and crate a token for that user then return it'''
    user = User.objects.get(id=id)
    token, create = Token.objects.get_or_create(user=user)
    return token.key
