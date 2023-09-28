from pydantic import BaseModel, Field 
from typing import Type
from superagi.tools.base_tool import BaseTool
import requests

class LinkedInProfileInput(BaseModel):
    linkedin_url: str = Field(..., description="LinkedIn profile URL to fetch data from DO NOT make up any url")   
class LinkedInProfileTool(BaseTool):
    """
    Execute LinkedIn Profile data extraction tool
    
    Args:
        linkedin_url : LinkedIn profile URL to fetch data from
    Returns:
       Profile data from the api request.

    """
    name: str = "LinkedIn Profile Tool"
    args_schema: Type[BaseModel] = LinkedInProfileInput
    description: str = "Fetches data from a LinkedIn profile"

    def _execute(self, args: LinkedInProfileInput): 
        linkedin_url = args.linkedin_url
        rapid_api_key = self.get_tool_config('X-RapidAPI-Key')
        rapid_host = self.get_tool_config('X-RapidAPI-Host')
        end_point = self.get_tool_config('End-Point')
        request_type = self.get_tool_config('Request-Type')
        first_param = self.get_tool_config('First-Param')
        request_type = request_type.lower()
        url = "https://hook.eu2.make.com/fs3b86gb8pap98gl347t3e7pzrbtq9jm"
        headers = {
            "X-RapidAPI-Key": rapid_api_key,
            "X-RapidAPI-Host": rapid_host
        }

        querystring = {first_param: linkedin_url}

        response = requests.get(url, headers=headers, params=querystring)
        return response.json()