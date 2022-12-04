from flask_restful import Resource, request
from marshmallow import ValidationError
from api.models.comment import CommentModel
from api.models.post import PostModel
from api.models.user import UserModel
from api.schemas.comment import CommentSchema

from flask_jwt_extended import jwt_required, get_jwt_identity

comment_schema = CommentSchema()
comment_list_schema = CommentSchema(many=True)

class CommentList(Resource):
    @classmethod
    def get(cls, post_id):
      # 게시물 id를 URL 로부터 얻어오기
      # 게시물 id에 달려 있는 전체 댓글 조회
      
      # URL 로부터 게시물의 ID 를 얻어와 게시물을 특정하고,
        post = PostModel.find_by_id(post_id)
        # 해당 게시물에 달려 있는 모든 댓글들을 ID의 역순으로 정렬한 다음,
        ordered_comment_list = post.comment_set.order_by(
            CommentModel.id.desc()
        )
        # 그것을 직렬화하여 반환!
        return comment_list_schema.dump(ordered_comment_list)
    
    @classmethod
    @jwt_required()
    def post(cls, post_id):
        # 게시물 id 를 URL 로부터 얻어오기
        # 게시물 id를 외래키로 하여 새로운 댓글 작성
        comment_json = request.get_json()
        # jwt로부터 작성자의 정보를 얻어와 작성자 id 를 특정하고,
        username = get_jwt_identity()
        author_id = UserModel.find_by_username(username).id
        try:
            # 댓글 인스턴스를 생성하고,
            new_comment = comment_schema.load(comment_json)
            new_comment.author_id = author_id  # 작성자를 추가해 준다.
            new_comment.post_id = post_id  # 어떤 게시물에 달린 댓글인지를 추가해 준다.
        except ValidationError as err:
            return err.messages, 400
        try:
            # 새 댓글을 데이터베이스에 저장한다.
            new_comment.save_to_db()
        except:
            return {"Error": "저장에 실패하였습니다."}, 500
        return comment_schema.dump(new_comment), 201


class CommentDetail(Resource):
    @classmethod
    @jwt_required()
    def put(cls, post_id, comment_id):
        comment_json = request.get_json()
        username = get_jwt_identity()
        author_id = UserModel.find_by_username(username).id
        post = PostModel.find_by_id(post_id)
        comment = CommentModel.find_by_id(comment_id)
        # 게시물의 존재 여부를 체크한다.
        if not post:
            return {"Error": "게시물을 찾을 수 없습니다."}, 404

        # 댓글의 존재 여부를 체크한다.
        if not comment:
            return {"Error": "댓글을 찾을 수 없습니다."}, 404
        
        # 기존 유저의 id 값과 댓글을 다는 작성자의 id값이 같을경우 수정한다.
        if author_id == comment.author_id:
            comment.update_to_db(comment_json)
        else:
            return {"Error": "댓글은 작성자만 수정할 수 있습니다."}, 403

        return comment_schema.dump(comment), 200

    @classmethod
    @jwt_required()
    def delete(cls, post_id, comment_id):
        username = get_jwt_identity()
        author_id = UserModel.find_by_username(username).id
        post = PostModel.find_by_id(post_id)
        comment = CommentModel.find_by_id(comment_id)
        
        # 게시물의 존재 여부를 체크한다.
        if not post:
            return {"Error": "게시물을 찾을 수 없습니다."}, 404

        # 댓글의 존재 여부를 체크한다.
        if not comment:
            return {"Error": "댓글을 찾을 수 없습니다."}, 404
        
        if post and author_id == comment.author.id:
            comment.delete_from_db()
            return {"message": "댓글이 성공적으로 삭제되었습니다."}, 200
        else:
            return {"Error" : "댓글은 작성자만 삭제할 수 있습니다."}, 403