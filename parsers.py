from rest_framework.parsers import JSONParser, FormParser, MultiPartParser, DataAndFiles
from .utils import parse_nested_keys

class SmartNestedParser:
    media_type = '*/*'

    def parse(self, stream, media_type=None, parser_context=None):
        parser_context = parser_context or {}
        request = parser_context.get('request')

        if not request:
            raise Exception("SmartNestedParser requires a request object")

        if media_type and 'application/json' in media_type:
            return JSONParser().parse(stream, media_type, parser_context)
        elif media_type and 'multipart/form-data' in media_type:
            form_parser = MultiPartParser()
            data_and_files = form_parser.parse(stream, media_type, parser_context)

            data = parse_nested_keys(data_and_files.data)
            return DataAndFiles(data=data, files=data_and_files.files)
        else:
            form_parser = FormParser()
            data_and_files = form_parser.parse(stream, media_type, parser_context)
            data = parse_nested_keys(data_and_files.data)
            return DataAndFiles(data=data, files=data_and_files.files)