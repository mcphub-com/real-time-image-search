import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/letscrape-6bRBa3QguO5/api/real-time-image-search'

mcp = FastMCP('real-time-image-search')

@mcp.tool()
def search_images(query: Annotated[str, Field(description='Search query / keyword')],
                  limit: Annotated[Union[int, float, None], Field(description='Maximum number of results to return. Default: 10 Allowed values: 1-100 Default: 10')] = None,
                  size: Annotated[Literal['any', 'large', 'medium', 'icon', '400x300_and_more', '640x480_and_more', '800x600_and_more', '1024x768_and_more', '2mp_and_more', '4mp_and_more', '6mp_and_more', '8mp_and_more', '10mp_and_more', '12mp_and_more', '15mp_and_more', '20mp_and_more', '40mp_and_more', '70mp_and_more', None], Field(description='Find images of a specific size. Default: any Allowed values: any, large, medium, icon, 400x300_and_more, 640x480_and_more, 800x600_and_more, 1024x768_and_more, 2mp_and_more, 4mp_and_more, 6mp_and_more, 8mp_and_more, 10mp_and_more, 12mp_and_more, 15mp_and_more, 20mp_and_more, 40mp_and_more, 70mp_and_more')] = None,
                  color: Annotated[Literal['any', 'red', 'orange', 'yellow', 'green', 'teal', 'blue', 'purple', 'pink', 'white', 'gray', 'black', 'brown', 'full', 'transparent', 'grayscale', None], Field(description='Find images with a specific dominant color. Default: any Allowed values: any, red, orange, yellow, green, teal, blue, purple, pink, white, gray, black, brown, full, transparent, grayscale')] = None,
                  type: Annotated[Literal['any', 'face', 'photo', 'clipart', 'lineart', 'animated', None], Field(description='Find images of a specific type. Default: any Allowed values: any, face, photo, clipart, lineart, animated')] = None,
                  time: Annotated[Literal['any', 'day', 'week', 'month', 'year', None], Field(description='Find images last updated in a specific time range. Default: any Allowed values: any, day, week, month, year')] = None,
                  usage_rights: Annotated[Literal['any', 'creative_commons', 'commercial', None], Field(description='Find images with specific usage rights / license / copyright. Default: any Allowed values: any, creative_commons, commercial')] = None,
                  file_type: Annotated[Literal['any', 'jpg', 'jpeg', 'png', 'gif', 'svg', 'webp', 'ico', 'raw', None], Field(description='Find images of a specific format / file type. Default: any Allowed values: any, jpg, jpeg, png, gif, svg, webp, ico, raw')] = None,
                  aspect_ratio: Annotated[Literal['any', 'tall', 'square', 'wide', 'panoramic', None], Field(description='Find images with a specific aspect ratio. Default: any Allowed values: any, tall, square, wide, panoramic')] = None,
                  country: Annotated[Union[str, None], Field(description='Find images published in a specific country / region. Allowed values: 2-letter country code, see ISO 3166-1 alpha-2')] = None,
                  safe_search: Annotated[Literal['off', 'blur', 'on', None], Field(description='How to show explicit content in your search results, like sexual activity and graphic violence. Default: blur Allowed values: off, blur, on')] = None,
                  region: Annotated[Union[str, None], Field(description='The country / region from which to make the query. Default: us Allowed values: 2-letter country code, see ISO 3166-1 alpha-2')] = None,
                  fields: Annotated[Union[str, None], Field(description='A comma separated list of image fields to include in the response (field projection). By default all fields are returned. Example: title,size,thumbnail_url,position')] = None) -> dict:
    '''Get real-time image search results from across the web. Supports all Google Images search filters.'''
    url = 'https://real-time-image-search.p.rapidapi.com/search'
    headers = {'x-rapidapi-host': 'real-time-image-search.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'limit': limit,
        'size': size,
        'color': color,
        'type': type,
        'time': time,
        'usage_rights': usage_rights,
        'file_type': file_type,
        'aspect_ratio': aspect_ratio,
        'country': country,
        'safe_search': safe_search,
        'region': region,
        'fields': fields,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

if __name__ == '__main__':
   mcp.run(transport="stdio")