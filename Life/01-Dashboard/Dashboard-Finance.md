
```dataview
TABLE WITHOUT ID 
    file.link AS "link", 
    tags AS tags,
    status AS "status"
    
FROM ""
WHERE (
    status = "Done"
    OR status = "InProgress"
    OR status = "ToDo"
    AND contains(category, "Finance")
    AND contains(file.folder, "02-Notes")
    AND (assistance != "true")
)

SORT category ASC,  tags ASC , file.name ASC
```