from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class MonitoringHealthEndpointTests(APITestCase):
    def test_monitoring_health_endpoint_success(self):
        response = self.client.get("/api/monitoring/health/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("success", response.data)
        self.assertTrue(response.data["success"])
        self.assertIn("message", response.data)
        self.assertEqual(response.data["message"], "DB is online")
        
    def test_monitoring_health_endpoint_unavailable(self):
        response = self.client.get("/api/monitoring/health/")

        self.assertEqual(response.status_code, status.HTTP_503_SERVICE_UNAVAILABLE)
        self.assertIn("success", response.data)
        self.assertTrue(response.data["success"])
        self.assertIn("message", response.data)
        self.assertEqual(response.data["message"], "BD is offline")