from csv import DictReader
from django.core.management import BaseCommand

from reviews.models import Category, Genre, Title, User, Review, Comment


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the csv data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = 'Loads data from csv files'

    def handle(self, *args, **options):
        # Show this if the data already exist in the database
        if Category.objects.exists():
            print('category data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        # Show this before loading the data into the database
        print('Loading category data')
        handle_category()
        handle_genre()
        handle_title()
        handle_user()
        handle_review()
        handle_comments()


def handle_category():
    #Code to load the data into database
    for row in DictReader(open('static/data/category.csv')):
        Category.objects.get_or_create(id=row['id'], name=row['name'], slug=row['slug'])

def handle_genre():
    for row in DictReader(open('static/data/genre.csv')):
        Genre.objects.get_or_create(id=row['id'], name=row['name'], slug=row['slug'])

def handle_title():
    for row in DictReader(open('static/data/titles.csv')):
        Title.objects.get_or_create(id=row['id'], name=row['name'], year=row['year'], category_id=row['category'])
    for row in DictReader(open('static/data/genre_title.csv')):
        Title.objects.get(id=row['title_id']).genre.add(row['genre_id'])

def handle_user():
    for row in DictReader(open('static/data/users.csv')):
        # Для кастомной модели Юзер - не работают миграции
        # User.objects.get_or_create(id=row['id'], username=row['username'], email=row['email'], role=row['role'], bio=row['bio'], first_name=row['first_name'], last_name=row['last_name'])
        # Для дефолтной модели Юзер (auth_user)
        User.objects.get_or_create(id=row['id'], username=row['username'], email=row['email'])

def handle_review():
    for row in DictReader(open('static/data/review.csv')):
        Review.objects.get_or_create(id=row['id'], title_id=row['title_id'], text=row['text'], author_id=row['author'], score=row['score'], pub_date=row['pub_date'])

def handle_comments():
    for row in DictReader(open('static/data/comments.csv')):
        Comment.objects.get_or_create(id=row['id'], review_id=row['review_id'], text=row['text'], author_id=row['author'], pub_date=row['pub_date'])