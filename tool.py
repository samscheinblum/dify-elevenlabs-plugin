
import requests
from dify_plugin.tool import BaseTool, ToolRequest, ToolResponse
from io import BytesIO

class tool(BaseTool):
    def run(self, request: ToolRequest) -> ToolResponse:
        api_key = request.credentials['api_key']
        voice_id = request.credentials['voice_id']
        text = request.params['text']

        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
        headers = {
            "xi-api-key": api_key,
            "Content-Type": "application/json"
        }
        payload = {
            "text": text,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75
            }
        }

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code != 200:
            return ToolResponse(error=f"Error from ElevenLabs API: {response.text}")

        audio_file = BytesIO(response.content)
        return ToolResponse(files={ "audio": ("output.mp3", audio_file, "audio/mpeg") })


tool = tool()
