def menu_items(request):
    """Adds links to the context for rendering in the global header navigation"""
    return {
        "navigation": [
            {"label": "One", "url": "/one"},
            {"label": "Two", "url": "/two"},
            {"label": "Three", "url": "/three"},
            {"label": "Four", "url": "/four"},
        ]
    }
