import re

from google.cloud import vision


class GoogleVision():
    client = vision.ImageAnnotatorClient()

    @classmethod
    def get_isbn_from_image(cls, url):
        res = cls.client.annotate_image({
            'image': {
                'source': {
                    'image_uri': url
                }
            }
        })
        
        text = res.full_text_annotation.text
        return re.search( r'978(?:-?\d){10}', text).group(0)

