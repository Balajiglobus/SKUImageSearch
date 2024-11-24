from django.shortcuts import render
import json

# Load the JSON data
with open('data.json', 'r') as f:
    data = json.load(f)

def search_sku(request):
    image_url = None
    error = None

    if request.method == 'POST':
        sku = request.POST.get('sku', '').strip()
        # Search for the SKU in the JSON data
        result = next((item for item in data if item['SKU'] == sku), None)

        if result:
            image_url = result['imageURL']
        else:
            error = "SKU not found!"

    return render(request, 'searchapp/search.html', {'image_url': image_url, 'error': error})
