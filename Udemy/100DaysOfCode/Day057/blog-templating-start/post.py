class Post:
    def __init__(self, blog_id, title, subtitle, body):
        self.blog_id = blog_id
        self.title = title
        self.subtitle = subtitle
        self.body = body

    def __repr__(self):
        return f"{self.blog_id}, {self.title}, {self.subtitle}, {self.body}"
