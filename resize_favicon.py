from PIL import Image
import os

# Open the original image
img = Image.open('fav icon image.png')

# Create favicon directory if it doesn't exist
if not os.path.exists('favicon'):
    os.makedirs('favicon')

# Define sizes for different purposes
sizes = {
    16: 'favicon-16x16.png',
    32: 'favicon-32x32.png',
    180: 'apple-touch-icon.png',
    192: 'android-chrome-192x192.png',
    512: 'android-chrome-512x512.png'
}

# Generate each size
for size, filename in sizes.items():
    resized_img = img.copy()
    resized_img.thumbnail((size, size), Image.Resampling.LANCZOS)
    resized_img.save(os.path.join('favicon', filename), 'PNG')

print("Favicon images generated successfully!") 