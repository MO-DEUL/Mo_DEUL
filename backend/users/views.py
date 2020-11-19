import os
import requests
from django.views import View
from django.shortcuts import redirect, reverse


class LoginView(View):
    # GET /users/login
    def get(self, request):
        pass

    # POST /users/login
    def post(self, request):
        pass


class KaKaoException(Exception):
    pass


def kakao_login(request):
    client_id = os.environ.get("KAKAO_ID")
    redirect_url = "http://127.0.0.1:8000/users/login/kakao/callback"
    return redirect(f"https://kauth.kakao.com/oauth/authorize?client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&response_type=code")


def kakao_callback(request):
    try:
        code = request.GET.get("code")
        client_id = os.environ.get("KAKAO_ID")
        token_request = requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id=KAKAO_ID")
    except KaKaoException:
        return redirect(reverse("users:login"))
