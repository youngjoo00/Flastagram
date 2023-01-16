# 프로젝트 이름

<p align="center">
  <br>
  Flask를 활용한 인스타그램 클론코딩
  <br>
</p>

## 프로젝트 소개

<p align="justify">
프로젝트 개요
  Flask-study 를 통해 Backend 를 공부해보고자 시작했고, <br>
  현존하는 가장 크고 인지도가 높은 인스타그램을 클론코딩하여 만드는 것이 목적이다.
</p>

<br>

## 기술 스택

Flask, JavaScript

<br>

## 구현 기능

### 기능 1 (BackEnd)

주로 api 폴더에서 기능을 구현함
api/resources는 게시물, 유저, 댓글에 관한 CRUD 기능을 구현

사용자가 어떠한 기능을 이용하기 위해 CRUD 기능을 이용할 때 1차로 resources에서 요청을 받고 -> 필요한 스키마, 모델이 있다면 api/schema, api/model 에 접근

### 기능 2 (FrontEnd)

assets/js/post_create.js : 사용자가 게시물을 작성한다면, 페이지에 띄우는 역할

assets/js/post_list.js : 사용자가 Flastagram 의 post_list.html 에서 보여주는 메인 페이지를 보려고 할 때 게시물들의 목록을 페이지네이션을 통해 10개의 게시물을 보여주고, 무한스크롤을 구현하여 스크롤을 내린다면 다음 게시물 10개를 보여줌

assets/js/login.js : Token을 활용한 사용자 로그인

assets/js/profile.js : 이미지 업로드를 이용한 사용자 프로필 화면 수정

### 기능 3

### 기능 4

<br>

## 배운 점 & 아쉬운 점

<p align="justify">

</p>

<br>

## 라이센스

<!-- Stack Icon Refernces -->

[js]: /images/stack/javascript.svg
[ts]: /images/stack/typescript.svg
[react]: /images/stack/react.svg
[node]: /images/stack/node.svg
