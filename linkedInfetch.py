from pydantic import BaseModel, Field
from typing import Type
from superagi.tools.base_tool import BaseTool
import requests

class LinkedInProfileInput(BaseModel):
    linkedin_url: str = Field(..., description="LinkedIn profile URL to fetch data from")

class LinkedInProfileTool(BaseTool):
    """
    LinkedIn Profile Tool
    """
    name: str = "LinkedIn Profile Tool"
    args_schema: Type[BaseModel] = LinkedInProfileInput
    description: str = "Fetches data from a LinkedIn profile"

    def _execute(self, linkedin_url: str = None):
        rapid_api_key = self.get_tool_config('X-RapidAPI-Key')

        url = "https://fresh-linkedin-profile-data.p.rapidapi.com/get-linkedin-profile"
        headers = {
            "X-RapidAPI-Key": rapid_api_key,
            "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com"
        }
        querystring = {"linkedin_url": linkedin_url}

        response = requests.get(url, headers=headers, params=querystring)
        response = response.json()
        headline = response['data']['headline']
        about = response['data']['about']
        experiences = response['data']['experiences']

        result_data = {
            'headline': headline,
            'about': about,
            'experiences': experiences
        }
        return result_data