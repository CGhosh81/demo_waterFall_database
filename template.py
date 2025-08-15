import os
from pathlib import Path

project_name = "water_fall"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/main.py",
    f"{project_name}/auth.py",
    f"{project_name}/database.py",
    f"{project_name}/models.py",
    f"{project_name}/utils.py",

    # Templates
    # f"{project_name}/templates/login.html",
    f"{project_name}/templates/tallest/Overall_height.html",
    f"{project_name}/templates/tallest/Tallest_single_drop.html",
    f"{project_name}/templates/tallest/free_falling_drops.html",
    f"{project_name}/templates/largest/By_average_width.html",
    f"{project_name}/templates/largest/By_average_volume.html",
    f"{project_name}/templates/largest/By_volume(No_rapids).html",
    f"{project_name}/templates/largest/By_volume(still_exist).html",
    f"{project_name}/templates/database/browse_by_country.html",
    f"{project_name}/templates/database/browse_the_map.html",
    f"{project_name}/templates/database/recent_update.html",
    f"{project_name}/templates/Top_rated.html",
    f"{project_name}/templates/Books.html",
    f"{project_name}/templates/Blog.html",
    f"{project_name}/templates/water_fall_details.html",
    f"{project_name}/templates/Help.html",
    f"{project_name}/templates/Contact.html",
    # f"{project_name}/templates/logout.html",

    # Static files
    f"{project_name}/static/css/style.css",
    f"{project_name}/static/js/app.js",

    # Config and setup (optional)
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
   
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass
    else:
        print(f"✅ File already exists at: {file_path}")
