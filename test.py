"""
Testing for **kwargs bug fix
Testing for multiple page searches
"""
from ddgs import DDGS
from fastcore.all import L

def search_images(term, max_images=30):
    "Search via ddgs; return image classes as a fastcore L."
    print(f"Searching for '{term}'")
    return L(DDGS().images(query=term, max_results=max_images))


results = search_images('grizzly bear', max_images=150)
if len(results) >= 100:
    print("HOOOORRRRAAAAYYYY")
    print(f"You found {len(results)} images")
print(results)
