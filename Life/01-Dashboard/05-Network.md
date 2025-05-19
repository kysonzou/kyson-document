```dataview
TABLE WITHOUT ID 
    file.link AS "link", 
    tags AS tags,
    status AS status

    

FROM ""
WHERE (
    contains(tags, "Network")
    AND contains(file.folder, "02-Notes")
)
SORT category ASC, tags ASC , file.name ASC
```
