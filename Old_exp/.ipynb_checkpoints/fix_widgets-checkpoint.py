import json
from pathlib import Path

# عدلي الاسم هنا للنسخة اللي تبين تصلحينها
path = Path("New_Exp_NLP_RAG_Project_edit.ipynb")

text = path.read_text(encoding="utf-8")

# نتأكد أول إنه JSON سليم
nb = json.loads(text)

meta = nb.get("metadata", {})
if "widgets" in meta:
    print("Found 'widgets' in metadata — removing it...")
    meta.pop("widgets")
else:
    print("No 'widgets' key found in metadata.")

# نحفظ نسخة جديدة عشان حتى نسخة edit تبقى موجودة كنسخة احتياط
fixed_path = path.with_name(path.stem + "_fixed.ipynb")
fixed_path.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding="utf-8")

print("Saved fixed notebook as:", fixed_path)
