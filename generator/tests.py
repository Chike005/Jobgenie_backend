from django.test import TestCase
from django.urls import reverse
import json

class ResumeEndpointsTests(TestCase):
    def setUp(self):
        self.payload = {
            "full_name": "Chike Emmanuel Ifedi",
            "email": "emmanuelifedi0@gmail.com",
            "phone": "07918942902",
            "education": [
                {"degree": "BSc Computer Science", "institution": "University of Bolton", "location": "Bolton, UK", "date": "07/2025"}
            ],
            "projects": [
                {"name":"ShareBite","date":"02/2025–07/2025","problem":"Food donation/reservation app","tools":["Django","React","SQLite","Google Maps API"],"highlights":["Donation & reservation flows","Geo drop-off selection"]}
            ],
            "work_history": [
                {"role":"IT Support Intern","org":"AppTech Lagos","date":"06/2022–08/2023","bullets":["Maintained internal apps","Debugged production issues"]}
            ],
            "skills": ["Python","Django","React","AWS"]
        }

    def test_generate_resume_json(self):
        res = self.client.post("/api/generate_resume/", data=json.dumps(self.payload), content_type="application/json")
        self.assertEqual(res.status_code, 200)
        self.assertIn("resume", res.json())

    def test_generate_resume_docx(self):
        res = self.client.post("/api/generate_resume_docx/", data=json.dumps(self.payload), content_type="application/json")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res["Content-Type"], "application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        self.assertTrue(res.content.startswith(b"PK"))  # .docx is a zip -> starts with PK
