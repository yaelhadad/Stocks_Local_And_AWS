import json

# קרא את הקובץ הישן עם קידוד שמניחים שהוא Windows-1252
with open("sqlite_data.json", "r", encoding="cp1252", errors="ignore") as f:
    data = json.load(f)

# שמור קובץ חדש בקידוד UTF-8
with open("sqlite_data_fixed.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Done! קובץ חדש בשם sqlite_data_fixed.json מוכן לטעינה")
