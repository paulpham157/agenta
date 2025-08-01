# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.api_error import ApiError
from ..types.http_validation_error import HttpValidationError


class UnprocessableEntityError(ApiError):
    def __init__(
        self,
        body: HttpValidationError,
        headers: typing.Optional[typing.Dict[str, str]] = None,
    ):
        super().__init__(status_code=422, headers=headers, body=body)
