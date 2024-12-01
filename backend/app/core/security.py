import logging

from fastapi_keycloak_middleware import AuthorizationMethod, KeycloakConfiguration

from app.core.config import settings

keycloak_config = KeycloakConfiguration(
    url=settings.KEYCLOAC_URL,
    realm=settings.KEYCLOAC_REALM,
    client_id=settings.KEYCLOAC_CLIENT_ID,
    client_secret=settings.KEYCLOAC_CLIENT_SECRET,
    authorization_method=AuthorizationMethod.CLAIM,
    authorization_claim="realm_access",
)


async def scope_mapper(claim_auth: dict) -> list[str]:
    permissions = []
    try:
        permissions = claim_auth["roles"]
    except KeyError:
        logging.warning("Unknown roles")

    return permissions
