import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestPlatformFlagship(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_platform_health(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["status"], "ONLINE")
        self.assertIn("RAG_ENGINE", res.json()["available_modules"])

    def test_workflow_execution(self):
        payload = {
            "tenant_id": "TENANT-ERHA-01",
            "workflow_module": "AGENT_MESH",
            "payload": {"task": "Full enterprise automated audit"}
        }
        res = self.client.post("/execute", json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["status"], "COMPLETED")
        self.assertEqual(data["tenant_id"], "TENANT-ERHA-01")

if __name__ == "__main__":
    unittest.main()
