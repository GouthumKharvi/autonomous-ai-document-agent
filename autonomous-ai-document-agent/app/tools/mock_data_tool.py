"""
Production-ready mock data provider for the Autonomous AI Document Agent.
"""

from typing import Dict


class MockDataProvider:
    """
    Provides realistic mock business data based on the document type.
    """

    _MOCK_DATA = {

        "Business Proposal": {
            "company_name": "ABC Technologies Pvt. Ltd.",
            "industry": "Artificial Intelligence",
            "location": "Bengaluru, India",
            "budget": "₹25 Lakhs",
            "timeline": "6 Months",
            "team_size": "6 Members",
            "project_manager": "John Smith",
            "deliverables": [
                "Requirement Analysis",
                "Solution Design",
                "Development",
                "Testing",
                "Deployment",
                "Documentation"
            ],
            "risks": [
                "Requirement Changes",
                "Integration Delays",
                "Resource Constraints"
            ]
        },

        "Meeting Minutes": {
            "meeting_date": "07 July 2026",
            "meeting_time": "10:00 AM",
            "location": "Conference Room A",
            "chairperson": "Project Manager",
            "attendees": [
                "Project Manager",
                "Business Analyst",
                "AI Engineer",
                "QA Engineer"
            ],
            "action_items": [
                "Finalize requirements",
                "Prepare architecture",
                "Schedule next review"
            ]
        },

        "Project Plan": {
            "budget": "₹18 Lakhs",
            "timeline": "5 Months",
            "team_size": "5 Members",
            "phases": [
                "Planning",
                "Design",
                "Implementation",
                "Testing",
                "Deployment"
            ]
        },

        "Business Report": {
            "report_period": "Q2 2026",
            "revenue": "₹1.8 Crores",
            "growth": "18%",
            "recommendations": [
                "Increase AI adoption",
                "Optimize operational costs",
                "Expand market reach"
            ]
        },

        "Technical Design": {
            "architecture": "Microservices",
            "backend": "FastAPI",
            "workflow": "LangGraph",
            "database": "PostgreSQL",
            "deployment": "Docker",
            "cloud": "AWS"
        },

        "Standard Operating Procedure": {
            "department": "AI Engineering",
            "owner": "Engineering Manager",
            "review_cycle": "Every 6 Months"
        },

        "Software Requirements Specification (SRS)": {
            "project_name": "AI-Powered E-commerce Platform",
            "version": "1.0",
            "client": "ABC Technologies Pvt. Ltd.",
            "industry": "Artificial Intelligence",
            "location": "Bengaluru, India",
            "budget": "₹25 Lakhs",
            "timeline": "6 Months",
            "team_size": "6 Members",
            "project_manager": "John Smith",
            "development_methodology": "Agile Scrum",
            "document_standard": "IEEE 830",
            "technology_stack": "FastAPI, LangGraph, Gemini, PostgreSQL"
        },

        "Product Specification": {
            "product_name": "AI Resume Screening System",
            "version": "1.0",
            "target_users": "Recruitment Teams",
            "functional_requirements": [
                "Resume Parsing",
                "Semantic Matching",
                "Candidate Ranking"
            ],
            "non_functional_requirements": [
                "Scalability",
                "Security",
                "High Availability"
            ]
        }
    }

    @classmethod
    def get_mock_data(cls, document_type: str) -> Dict:
        """
        Return mock data for the requested document type.
        """

        return cls._MOCK_DATA.get(document_type, {})