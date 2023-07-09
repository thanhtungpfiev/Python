from post import Post


class PostManager:
    def __init__(self):
        self.blog_posts = {}

    def init_blog_posts(self, json_text):
        self.blog_posts = {str(item['id']): Post(item['id'], item['title'], item['subtitle'], item['body']) for item in
                           json_text}
