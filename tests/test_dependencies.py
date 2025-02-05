import pytest

from fastapi_app.dependencies import common_parameters, get_azure_credentials


@pytest.mark.asyncio
async def test_get_common_parameters(mock_session_env):
    result = await common_parameters()
    assert result.openai_chat_model == "gpt-35-turbo"
    assert result.openai_embed_model == "text-embedding-ada-002"
    assert result.openai_embed_dimensions == 1536
    assert result.openai_chat_deployment == "gpt-35-turbo"
    assert result.openai_embed_deployment == "text-embedding-ada-002"


@pytest.mark.asyncio
async def test_get_azure_credentials(mock_session_env, mock_default_azure_credential):
    result = await get_azure_credentials()
    token = result.get_token("https://vault.azure.net")
    assert token.expires_on == 9999999999
    assert token.token == ""
