from app.security import create_access_token, decode_access_token, hash_password, verify_password


def test_hash_password_generates_different_value_and_verifies():
    raw = "minha-senha-segura"
    hashed = hash_password(raw)

    assert hashed != raw
    assert verify_password(raw, hashed) is True


def test_decode_access_token_returns_payload_with_subject():
    token = create_access_token(subject="7")
    payload = decode_access_token(token)

    assert payload is not None
    assert payload["sub"] == "7"
