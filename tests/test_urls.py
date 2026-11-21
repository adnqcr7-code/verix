from verix.detection.urls import extract_urls, domain_of
def test_extracts_http_url():
    assert extract_urls("check https://example.com/free-nitro now") == ["https://example.com/free-nitro"]
def test_no_urls():
    assert extract_urls("just a normal hello") == []
def test_domain():
    assert domain_of("https://discord-nitro-free.xyz/claim") == "discord-nitro-free.xyz"
