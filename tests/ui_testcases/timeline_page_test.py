import allure
from page_objects.timeline_page import TimeLinePage
from tests.base_test import BaseTest
from application_settings.application_settings import ApplicationSettings


class TimeLinePageTest(BaseTest):

    application_settings = ApplicationSettings()
    data = application_settings.get_test_data_from_excel("login", "login_data")

    @allure.title("Timeline Page - Sanity Test")
    @allure.description("Checking if a user can post normal text on timeline")
    def test_01_post_text_successfully(self):
        timeline_page = TimeLinePage(self.driver)
        print("Starting to test text posting functionality")
        assert timeline_page.post_text_successfully() is True, "text posting failed"

    @allure.title("Timeline Page - Sanity Test")
    @allure.description("Checking if a user can post image on timeline")
    def test_02_post_image_successfully(self):
        timeline_page = TimeLinePage(self.driver)
        print("Starting to test image posting functionality")
        assert timeline_page.post_image_successfully() is True, "image posting failed"

    @allure.title("Timeline Page - Sanity Test")
    @allure.description("Checking if a user can post video on timeline")
    def test_03_post_video_successfully(self):
        timeline_page = TimeLinePage(self.driver)
        print("Starting to test video sharing functionality")
        assert timeline_page.post_video_successfully() is True, "Video posting failed"

    @allure.title("Timeline Page - Sanity Test")
    @allure.description("Checking if a user can post audio on timeline")
    def test_04_post_audio_successfully(self):
        timeline_page = TimeLinePage(self.driver)
        print("Starting to test audio sharing functionality")
        assert timeline_page.post_audio_successfully() is True, "Audio posting failed"
