# 1. From the following table, write a SQL query to find the name and year of the movies. Return movie title, movie release year.

Movie.objects.values('mov_title','mov_year')


# 2. From the following table, write a SQL query to find when the movie 'American Beauty' released. Return movie release year. 

Movie.objects.get(mov_title='American Beauty').mov_year



# 3. From the following table, write a SQL query to find the movie that was released in 1999. Return movie title.

Movie.objects.filter(mov_year='1999').values('mov_title')
# <QuerySet [{'mov_title': 'Eyes Wide Shut                                    '}, {'mov_title': 'American Beauty                                   '}]>



# 4. From the following table, write a SQL query to find those movies, which were released before 1998. Return movie title.

Movie.objects.filter(mov_year__lt=1998).values('mov_title')

# <QuerySet [{'mov_title': 'Vertigo                                           '}, {'mov_title': 'The Innocents                                     '}, {'mov_title': 'Lawrence of Arabia                                '}, {'mov_title': 'The Deer Hunter                                   '}, {'mov_title': 'Amadeus                                           '}, {'mov_title': 'Blade Runner                                      '}, {'mov_title': 'The Usual Suspects                                '}, {'mov_title': 'Chinatown                                         '}, {'mov_title': 'Boogie Nights                                     '}, {'mov_title': 'Annie Hall                                        '}, {'mov_title': 'Princess Mononoke                                 '}, {'mov_title': 'The Shawshank Redemption                          '}, {'mov_title': 'Titanic                                           '}, {'mov_title': 'Good Will Hunting                                 '}, {'mov_title': 'Deliverance                                       '}, {'mov_title': 'Trainspotting                                     '}, {'mov_title': 'Aliens                                            '}, {'mov_title': 'Seven Samurai                                     '}, {'mov_title': 'Back to the Future                                '}, {'mov_title': 'Braveheart                                        '}]>
# >>> 



# 5. From the following tables, write a SQL query to find the name of all reviewers and movies together in a single list. 

from django.db.models import Q
Reviewer.objects.values_list('rev_name', flat=True).union(Movie.objects.values_list('mov_title', flat=True))

# <QuerySet [None, 'The Usual Suspects                                ', 'Amadeus                                           ', 'American Beauty                                   ', 'Alec Shaw                     ', 'Boogie Nights                                     ', 'Hannah Steele                 ', 'Neal Wruck                    ', 'The Shawshank Redemption                          ', 'Richard Adams                 ', 'Titanic                                           ', 'Krug Stillo                   ', 'Paul Monks                    ', 'Righty Sock                   ', 'Seven Samurai                                     ', 'Sasha Goldshtein              ', 'The Deer Hunter                                   ', 'Jack Malvern                  ', 'Princess Mononoke                                 ', 'Lawrence of Arabia                                ', '...(remaining elements truncated)...']>
# >>> result
# <QuerySet [None, 'The Usual Suspects                                ', 'Amadeus                                           ', 'American Beauty                                   ', 'Alec Shaw                     ', 'Boogie Nights                                     ', 'Hannah Steele                 ', 'Neal Wruck                    ', 'The Shawshank Redemption                          ', 'Richard Adams                 ', 'Titanic                                           ', 'Krug Stillo                   ', 'Paul Monks                    ', 'Righty Sock                   ', 'Seven Samurai                                     ', 'Sasha Goldshtein              ', 'The Deer Hunter                                   ', 'Jack Malvern                  ', 'Princess Mononoke                                 ', 'Lawrence of Arabia                                ', '...(remaining elements truncated)...']>


# 6. From the following table, write a SQL query to find all reviewers who have rated seven or more stars to their rating. Return reviewer name.

Reviewer.objects.filter(rating__rev_stars__gte=7, rev_name__isnull=False).values_list('rev_name', flat=True)


#7. From the following tables, write a SQL query to find the movies without any rating. Return movie title. 

Movie.objects.exclude(mov_id__in=Rating.objects.values('mov_id')).values_list('mov_title', flat=True)


#8. From the following table, write a SQL query to find the movies with ID 905 or 907 or 917. Return movie title.

Movie.objects.filter(mov_id__in=['905', '907', '917']).values_list('mov_title', flat=True)




#9. Question