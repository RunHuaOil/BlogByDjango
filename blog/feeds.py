from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatechars
from .models import Post


class LatestPostsFeed(Feed):
    title = 'RunHuaOil\'s blog'
    link = '/blog/'
    description = '我的博客有新文章啦.'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatechars(item.body, 30)
