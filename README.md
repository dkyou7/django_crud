# django_crud 만들어보기

## 1. VSCODE에서 가상환경 설치 및 서버 실행해보기

```bash
$ python -m venv 'venv' #가상환경 생성

$ source venv/scripts/activate # 가상환경 실행

(myvenv) # 가상환경 켜짐
# 꺼짐은 deactivate

$ pip3 install django # django 설치, 필자는 2.1.5 버전을 좋아한다.
# 따라서 pip3의 django==2.1.5 버전을 설치하였음
# pip3 install django==2.1.5

$ django-admin startproject 'config' . # 프로젝트 생성
# 이때 manage.py가 위치한 프로젝트 안(BASE_DIR)으로 들어간다. 

$ python manage.py startapp 'blog' # app 생성

$ python manage.py runserver # http://127.0.0.1:8000/
# vscode에 있는 liveserver 등 extension들도 로컬 서버를 지원한다. 
```

