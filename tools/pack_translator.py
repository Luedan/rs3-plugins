import os, zipfile

src_dir = 'plugins/rs-translator'
out_zip = 'dist/rs-translator-v1.0.0.zip'

with zipfile.ZipFile(out_zip, 'w', compression=zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, src_dir).replace('\\', '/')
            z.write(full_path, rel_path)

print(f"Re-packaged {out_zip} successfully!")
with zipfile.ZipFile(out_zip, 'r') as z:
    names = z.namelist()
    print(f"Total files: {len(names)}")
    assert 'src/quest_helper_hook.lua' in names
    print("Found src/quest_helper_hook.lua!")
