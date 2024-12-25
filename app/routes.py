from flask_restful import Resource
from flask import request
from app.models import Blog

# Initialize the blog object
blog = Blog()

class BlogPostResource(Resource):
    def get(self, title=None):
        if title:
            post = blog.get_post_by_title(title)
            if post:
                return post, 200
            return {"message": "Post not found"}, 404
        else:
            posts = blog.get_all_posts()
            return {"posts": posts}, 200

    def post(self):
        data = request.get_json()
        title = data.get('title')
        content = data.get('content')
        author = data.get('author')

        if not title or not content or not author:
            return {"message": "Title, content, and author are required"}, 400

        post = blog.add_post(title, content, author)
        return post.display_post(), 201

    def put(self, title):
        data = request.get_json()
        new_content = data.get('content')

        if not new_content:
            return {"message": "Content is required to update the post"}, 400

        updated_post = blog.update_post(title, new_content)
        if updated_post:
            return updated_post, 200
        return {"message": "Post not found"}, 404

    def delete(self, title):
        deleted_post = blog.delete_post(title)
        if deleted_post:
            return {"message": f"Post '{title}' deleted successfully"}, 200
        return {"message": "Post not found"}, 404


# Initialize routes
def initialize_routes(api):
    api.add_resource(BlogPostResource, "/posts", "/posts/<string:title>")
