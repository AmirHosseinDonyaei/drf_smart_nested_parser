from typing import Any, Optional

from rest_framework.parsers import (
    BaseParser,
    JSONParser,
    FormParser,
    MultiPartParser,
    DataAndFiles,
)

from .utils import parse_nested_keys


class SmartNestedParser(BaseParser):
    media_type = "*/*"

    def parse(
        self,
        stream,
        media_type: Optional[str] = None,
        parser_context: Optional[dict] = None,
    ) -> Any:
        parser_context = parser_context or {}
        request = parser_context.get("request")

        if request is None:
            raise RuntimeError("SmartNestedParser requires request in parser_context.")

        media_type = media_type or request.content_type or ""

        if "application/json" in media_type:
            return JSONParser().parse(stream, media_type, parser_context)

        if "multipart/form-data" in media_type:
            parsed = MultiPartParser().parse(stream, media_type, parser_context)
            nested_data = parse_nested_keys(parsed.data)
            return DataAndFiles(data=nested_data, files=parsed.files)

        if "application/x-www-form-urlencoded" in media_type:
            parsed = FormParser().parse(stream, media_type, parser_context)
            nested_data = parse_nested_keys(parsed.data)
            return DataAndFiles(data=nested_data, files=parsed.files)

        parsed = FormParser().parse(stream, media_type, parser_context)
        nested_data = parse_nested_keys(parsed.data)
        return DataAndFiles(data=nested_data, files=parsed.files)
