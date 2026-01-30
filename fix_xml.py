# Fix XML parsing error by removing problematic comment block
with open('index.xml', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Keep lines 0-7268 (up to line 7269), add new comment, then skip to line 7277
new_lines = lines[:7268] + ['<!-- Blogger Scripts -->\r\n'] + lines[7276:]

with open('index.xml', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Fixed XML file - removed problematic comment block with double hyphens")
