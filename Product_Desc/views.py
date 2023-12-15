import os
import requests
from openai import OpenAI
from dotenv import load_dotenv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser


load_dotenv()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
ImaggaAPIAuth = (os.environ.get("IMAGGA_API_KEY"), os.environ.get("IMAGGA_API_SECRET"))


@api_view()
def ProductDesc(request, title: str):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {
                "role": "user",
                "content": 'You are an assistant that takes a product title as the input and returns a product description of the product in less than 50 words then a list consisting of less than 10 SEO keywords present in the product description with each one separated by a ",". The description and the keywords should be separated by "--keys--" string.\n\nTitle:'
                + title,
            },
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    msg: str = response.choices[0].message.content
    title, keywords = msg.split("--keys--")
    title = title.strip("\n")
    keywords = [x.strip() for x in keywords.split(",")]
    return Response({"title": title, "keywords": keywords})


class ImageAnalyze(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        response = requests.post(
            "https://api.imagga.com/v2/tags",
            auth=ImaggaAPIAuth,
            files={"image": request.data["picture"].open("rb")},
        )
        li: list = response.json()["result"]["tags"]
        tags = [x["tag"]["en"] for x in li]
        return Response({"working": tags})
