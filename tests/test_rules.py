from verix.detection.classifier import classify
def test_normal_message_is_zero():
    r = classify("Hey everyone, game night at 8pm tomorrow?")
    assert r["risk_level"] == 0
def test_free_nitro_is_suspicious():
    r = classify("FREE NITRO!! claim at https://discord-nitro-free.xyz/claim now")
    assert r["risk_level"] >= 2
    assert "nitro" in r["explanation"].lower() or "discord" in r["explanation"].lower()
def test_crypto_doubling_is_high():
    r = classify("Send 0.1 BTC and get 0.2 BTC back, double your crypto!")
    assert r["risk_level"] >= 1
def test_sender_not_accused():
    r = classify("Someone sent me this link https://discord-nitro-free.xyz — is it real?")
    assert r["risk_level"] >= 1
    assert "criminal" not in r["explanation"].lower()
