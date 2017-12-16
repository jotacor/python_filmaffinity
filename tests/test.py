from unittest import TestCase

import sys
import os
import random

import python_filmaffinity
from python_filmaffinity.config import FIELDS_PAGE_MOVIES, FIELDS_PAGE_DETAIL

path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path + '/../')


class TestApi(TestCase):
    service = python_filmaffinity.FilmAffinity()

    def check_list(self, movies):
        self.assertNotEqual(0, len(movies))
        movie = random.choice(movies)
        for field in FIELDS_PAGE_MOVIES:
            self.assertNotEqual(movie[field], None)
        self.assertNotEqual(len(movie['directors']), 0)

    def check_element(self, movie):
        for field in FIELDS_PAGE_DETAIL:
            self.assertNotEqual(movie[field], None)

    def test_search(self):
        movies = self.service.search(title='Batman')
        self.check_list(movies)

    def test_get_movie(self):
        movie = self.service.get_movie(id='197671')
        self.check_element(movie)

    def test_top_filmaffinity(self):
        movies = self.service.top_filmaffinity()
        self.check_list(movies)

    def test_top_series(self):
        movies = self.service.top_tv_series()
        self.check_list(movies)
        movies = self.service.top_tv_series(top=5)
        self.assertEqual(len(movies), 5)
        movies = self.service.top_tv_series(top=80)
        self.assertEqual(len(movies), 30)
        movies = self.service.top_tv_series(from_year='2010', to_year='2011')
        self.check_list(movies)

    def test_top_premieres(self):
        movies = self.service.top_premieres()
        self.check_list(movies)

    def test_top_filmaffinity_years(self):
        movies = self.service.top_filmaffinity(from_year='2010', to_year='2011')
        self.check_list(movies)

    def test_search_years(self):
        movies = self.service.search(
            title='Batman', from_year='2000', to_year='2011')
        self.check_list(movies)

    def test_top_netflix(self):
        movies = self.service.top_netflix(top=10)
        self.check_list(movies)

    def test_top_movistar(self):
        movies = self.service.top_movistar(top=10)
        self.check_list(movies)

    def test_top_rakuten(self):
        movies = self.service.top_rakuten(top=10)
        self.check_list(movies)

    def test_top_hbo(self):
        movies = self.service.top_hbo(top=10)
        self.check_list(movies)

    def test_top_filmin(self):
        movies = self.service.top_filmin(top=10)
        self.check_list(movies)

    def test_recommend_netflix(self):
        movie = self.service.recommend_netflix()
        self.check_element(movie)

    def test_recommend_hbo(self):
        movie = self.service.recommend_hbo()
        self.check_element(movie)

    def test_recommend_filmin(self):
        movie = self.service.recommend_filmin()
        self.check_element(movie)

    def test_recommend_movistar(self):
        movie = self.service.recommend_movistar()
        self.check_element(movie)

    def test_recommend_rakuten(self):
        movie = self.service.recommend_rakuten()
        self.check_element(movie)

    def test_trailer(self):
        trailer = self.service._get_trailer('Batman')
        self.assertNotEqual(trailer, None)

    def test_images(self):
        movie = self.service.get_movie(id='668878', images=True)
        self.assertNotEqual(movie['images'], [])

    def test_top_dvd(self):
        movies = self.service.top_dvd(top=10)
        self.check_list(movies)
        movies = self.service.top_dvd(top=20)
        self.assertEqual(len(movies), 20)
        movies = self.service.top_dvd(top=80)
        self.assertEqual(len(movies), 40)
        self.check_list(movies)
