```dataview
TABLE WITHOUT ID 
    file.link AS "link", 
    tags AS tags,
    status AS status

FROM ""
WHERE (
    contains(tags, "CLI")
    OR contains(tags, "Python")
    OR contains(tags, "VSCode")
    AND contains(file.folder, "02-Notes")
    AND (assistance != "true")
)
SORT category ASC, tags ASC , file.name ASC
```
