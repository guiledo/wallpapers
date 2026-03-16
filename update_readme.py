import os

def update_readme():
    pics_dir = 'pics'
    readme_file = 'README.md'
    
    # Supported image extensions
    extensions = ('.png', '.jpg', '.jpeg', '.webp', '.gif')
    
    # Get all image files in pics directory
    images = [f for f in os.listdir(pics_dir) if f.lower().endswith(extensions)]
    # Sort them to keep the README order consistent
    images.sort()
    
    with open(readme_file, 'w') as f:
        f.write('# my wallpapers\n\n')
        for image in images:
            alt_text = os.path.splitext(image)[0]
            f.write(f'<a href="pics/{image}"><img alt="{alt_text}" src="pics/{image}"></a>\n\n')

if __name__ == "__main__":
    update_readme()
