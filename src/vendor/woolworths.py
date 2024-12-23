import requests

from src.obj import ItemSearchResult


def product_search(user_query: str, max_n_items: int) -> list[ItemSearchResult]:
    """
    TODO
    """
    response = requests.get(
        url="https://www.woolworths.co.za/server/searchCategory",
        params={
            "pageURL": "/cat",
            "Ntt": user_query,
            "Dy": 1,
        },
        headers={
            "User-Agent": "Please let me in",
            "referer": "https://www.woolworths.co.za/cat",
        },
    )
    items_info_raw: list[dict] = response.json()["contents"][0]["mainContent"][0][
        "contents"
    ][0]["records"]
    if len(items_info_raw) > max_n_items:
        items_info_raw = items_info_raw[:max_n_items]

    items_info: list[dict] = [
        {
            "item_title": item["attributes"]["p_displayName"],
            "item_image_url": item["attributes"]["p_externalImageReference"],
            "item_prices": item["startingPrice"],
        }
        for item in items_info_raw
    ]
    return items_info
