from pydantic import BaseModel, ConfigDict, Field


class CreateUserRequestAttr(BaseModel, hide_input_in_errors=True):
    name: str = Field(
        title="First name",
        alias="firstName",
        min_length=2,
        max_length=20,
    )


class CreateUserRequestModelConfig(BaseModel):
    model_config = ConfigDict(hide_input_in_errors=True)
    name: str = Field(
        title="First name",
        alias="firstName",
        min_length=2,
        max_length=20,
    )
