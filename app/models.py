class BlogPost:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.date_created = None

    def display_post(self):
        return {
            "title": self.title,
            "content": self.content,
            "author": self.author,
            "date_created": self.date_created,
        }

    def set_date_created(self, date):
        self.date_created = date

    def update_content(self, new_content):
        self.content = new_content


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, title, content, author):
        post = BlogPost(title, content, author)
        self.posts.append(post)
        return post

    def delete_post(self, title):
        post_to_delete = next((post for post in self.posts if post.title == title), None)
        if post_to_delete:
            self.posts.remove(post_to_delete)
            return post_to_delete
        return None

    def get_all_posts(self):
        return [post.display_post() for post in self.posts]

    def get_post_by_title(self, title):
        post = next((post for post in self.posts if post.title == title), None)
        if post:
            return post.display_post()
        return None

    def update_post(self, title, new_content):
        post = next((post for post in self.posts if post.title == title), None)
        if post:
            post.update_content(new_content)
            return post.display_post()
        return None
