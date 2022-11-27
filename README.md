# Flastagram 구조

1. Backend

주로 api 폴더에서 기능들이 구현된다.
api/resources는 게시물, 유저, 댓글에 관한 CRUD 기능을 구현한다.

사용자가 어떠한 기능을 이용하기 위해 CRUD 기능을 이용할 때
1차로 resources에서 요청을 받은 다음
필요한 스키마, 모델이 있다면 api/schema, api/model 에 접근하여 기능을 구현함

2. Frontend

주로 assets 폴더에서 사용자가 보는 화면을 뿌려주는 역할을 한다.

현재 가능한 기능 목록

1) assets/js/post_create.js : 사용자가 게시물을 작성한다면, 페이지에 띄우는 역할을 한다.

2) assets/js/post_list.js : 사용자가 Flastagram 의 post_list.html 에서 보여주는 메인 페이지를 보려고 할 때
게시물들의 목록을 페이지네이션을 통해 10개의 게시물을 보여주고, 무한스크롤을 구현하여 스크롤을 내린다면 다음 게시물 10개를 보여주는 역할을 한다.