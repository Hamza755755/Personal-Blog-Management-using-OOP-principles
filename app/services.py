from app.models import Blog, BlogPost
from datetime import datetime

# Initialize the blog object
blog = Blog()

def create_blog_post(title, content, author):
    """Service to create a new blog post."""
    # Validate input data
    if not title or not content or not author:
        raise ValueError("Title, content, and author are required.")

    # Create a new post
    post = blog.add_post(title, content, author)
    
    # Set the creation date of the post
    post.set_date_created(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    return post


def update_blog_post(title, new_content):
    """Service to update the content of an existing blog post."""
    if not new_content:
        raise ValueError("New content is required to update the post.")
    
    updated_post = blog.update_post(title, new_content)
    
    if not updated_post:
        raise ValueError(f"Post with title '{title}' not found.")
    
    return updated_post


def delete_blog_post(title):
    """Service to delete a blog post by title."""
    deleted_post = blog.delete_post(title)
    
    if not deleted_post:
        raise ValueError(f"Post with title '{title}' not found.")
    
    return deleted_post


def get_blog_post_by_title(title):
    """Service to fetch a specific blog post by title."""
    post = blog.get_post_by_title(title)
    
    if not post:
        raise ValueError(f"Post with title '{title}' not found.")
    
    return post


def get_all_blog_posts():
    """Service to fetch all blog posts."""
    return blog.get_all_posts()
