from django.test import TestCase
from django.urls import reverse

from dashboard.models import Robot


class ModelTestCase(TestCase):
    def test_robot_model_created_successfully(self):
        robot = Robot(name="Robot 1", motor_type="DC")

        self.assertEqual(robot.name, "Robot 1")
        self.assertEqual(robot.motor_type, "DC")

    def test_robot_model_created_with_null_name_should_fail(self):
        pass

    def test_robot_run_model_created_successfully(self):
        #robot_run = RobotRun()
        pass

    def test_robot_run_distance_max_value_limit(self):
        pass


class ViewsTestCase(TestCase):
    def test_show_robot_run(self):
        # split into moe tests after views.py refactor
        pass

    def test_register_robot_get_method(self):
        url = reverse('register-robot')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register_robot.html')

    def test_register_robot_post_method(self):
        url = reverse('register-robot')
        data = {'name': 'Robot 3', 'motor_type': 'servo'}

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Robot.objects.count(), 1)

        created_robot = Robot.objects.first()

        self.assertEqual(created_robot.name, 'Robot 3')
        self.assertEqual(created_robot.motor_type, 'servo')
        self.assertTemplateUsed(response, 'register_robot.html')

    def test_show_robot_detail_post_method(self):
        url = reverse('robot-detail')
        data = {"robot_id": 5}

        response = self.client.post(url, data)

        pass
