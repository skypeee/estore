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