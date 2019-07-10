import coreapi
import coreschema
from rest_framework.schemas import AutoSchema, ManualSchema

GroupDeleteSchema = AutoSchema([
    coreapi.Field(
                "group_id",
                required=True,
                location="form",
                schema=coreschema.Integer(),
                description="角色ID",
            ),
])
OrderSchema = AutoSchema([
    coreapi.Field(
        "page",
        required=False,
        location="query",
        schema=coreschema.Integer(),
        description="A page number within the paginated result set."
    ),
    coreapi.Field(
        "page_size",
        required=False,
        location="query",
        schema=coreschema.Integer(),
        description="Number of results to return per page."
    ),
])