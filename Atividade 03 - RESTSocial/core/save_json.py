from core.models import Profile, Post, Comment
import json

def import_json(name_arquivo='db.json'):
    save_profiles(name_arquivo)
    save_posts(name_arquivo)
    save_comments(name_arquivo)


def save_profiles(arquivo):
    with open(arquivo) as data:
        data_json = json.load(data)
        profiles = []
        for registro in data_json['users']:
            profiles.append(
                Profile(
                    id=registro['id'],
                    name=registro['name'],
                    email=registro['email'],
                    address=registro['address']
                )
            )
    Profile.objects.bulk_create(profiles)
            
            
def save_posts(arquivo):
    with open(arquivo) as data:
        data_json = json.load(data)
        posts = []
        for registro in data_json['posts']:
            posts.append(
                Post(
                    userId=Profile.objects.get(id=registro['userId']),
                    id=registro['id'],
                    title=registro['title'],
                    body=registro['body']
                )
            )
    Post.objects.bulk_create(posts)
            
            
def save_comments(arquivo):
    with open(arquivo) as data:
        data_json = json.load(data)
        comments = []
        for registro in data_json['comments']:
            comments.append(
                Comment(
                    postId=Post.objects.get(id=registro['postId']),
                    id=registro['id'],
                    name=registro['name'],
                    body=registro['body'],
                    email=registro['email']
                )
            )
    Comment.objects.bulk_create(comments)
            