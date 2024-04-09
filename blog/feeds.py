
from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post

class BlogPostFeed(Feed):
    title = "Blog newest post"
    link = "/rss/feed"
    description = "The best blog ever."

    def items(self):
        return Post.objects.filter(status=True)[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:200]
