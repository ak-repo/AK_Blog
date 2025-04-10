from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post

# Create your tests here.


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@gmail.com", password="password"
        )

        cls.post = Post.objects.create(
            title="first title",
            text="first text",
            author=cls.user,
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "first title")
        self.assertEqual(self.post.text, "first text")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "first title")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")

    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_post_listview(self):
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "first text")
        self.assertTemplateUsed(response, "blog/post_list.html")

    # Post Detail view tests
    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("/post/1/")
        self.assertEqual(response.status_code, 200)

    def test_post_detailview(self):
        response = self.client.get(reverse("post_detail", kwargs={"pk": self.post.pk}))
        no_response = self.client.get("/post/1000000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "first title")
        self.assertTemplateUsed(response, "blog/post_detail.html")

    # Post Create view tests
    def test_post_createview(self):
        response = self.client.post(
            reverse("post_new"),
            {
                "title": "New title",
                "text": "New text",
                "author": self.user.id,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "New title")
        self.assertEqual(Post.objects.last().text, "New text")

    # Post Update view tests
    def test_post_updatview(self):
        response = self.client.post(
            reverse("post_edit", args="1"),
            {
                "title": "Updated title",
                "text": "Updated text",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "Updated title")
        self.assertEqual(Post.objects.last().text, "Updated text")

    # Post Delete view tests
    def test_post_deleteview(self):
        response = self.client.post(reverse("post_delete", args="1"))
        self.assertEqual(response.status_code, 302)
