import csv

from django.core.management import BaseCommand

from reviews.models import Category, Genre, Title, User, Review, Comment


MODELS = [Category, Genre, Title, User, Review, Comment]

ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the csv data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    help = 'Loads data from csv files'

    def handle(self, *args, **options):
        for Model in MODELS:
            if Model.objects.exists():
                print('category data already loaded...exiting.')
                print(ALREDY_LOADED_ERROR_MESSAGE)
                return
        print('Loading category data')
        handle_category()
        handle_genre()
        handle_title()
        handle_user()
        handle_review()
        handle_comments()


def handle_category():
    with open(('static/data/category.csv'), mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            object_dict = {
                key: value
                for key, value in zip(header, row)
            }
            Category.objects.create(**object_dict)


def handle_genre():
    with open(('static/data/genre.csv'), mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            object_dict = {
                key: value
                for key, value in zip(header, row)
            }
            Genre.objects.create(**object_dict)


def handle_title():
    with open(('static/data/titles.csv'), mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Title.objects.get_or_create(id=row['id'],
                                        name=row['name'],
                                        year=row['year'],
                                        category_id=row['category'])
        with open(('static/data/genre_title.csv'), mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Title.objects.get(
                    id=row['title_id']).genre.add(row['genre_id'])


def handle_user():
    with open(('static/data/users.csv'), mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            object_dict = {
                key: value
                for key, value in zip(header, row)
            }
            User.objects.create(**object_dict)


def handle_review():
    with open(('static/data/review.csv'), mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Review.objects.get_or_create(id=row['id'],
                                         title_id=row['title_id'],
                                         text=row['text'],
                                         author_id=row['author'],
                                         score=row['score'],
                                         pub_date=row['pub_date'])


def handle_comments():
    with open(('static/data/comments.csv'), mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Comment.objects.get_or_create(id=row['id'],
                                          review_id=row['review_id'],
                                          text=row['text'],
                                          author_id=row['author'],
                                          pub_date=row['pub_date'])
