import unittest

from app import create_app


class AppRouteTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_routes_return_200(self):
        routes = [
            "/",
            "/programme",
            "/curriculum",
            "/admissions",
            "/faculty",
            "/research",
            "/students-alumni",
            "/contact",
        ]
        for route in routes:
            with self.subTest(route=route):
                response = self.client.get(route)
                self.assertEqual(response.status_code, 200)

    def test_home_contains_programme_heading(self):
        response = self.client.get("/")
        self.assertIn(b"MSc in New Media", response.data)


if __name__ == "__main__":
    unittest.main()

