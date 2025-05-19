## 未开始
```dataview
TABLE WITHOUT ID 
    file.link AS "link", 
    category AS "category",
    tags AS tags,
    status AS "Status"
    
FROM ""
WHERE (
    status = "ToDo"
    AND contains(file.folder, "02-Notes")
)
SORT category ASC, tags ASC ,file.name ASC
```

## 进行中

```dataview
TABLE WITHOUT ID 
    file.link AS "link", 
    category AS "category",
    tags AS tags,
    status AS "Status"
    

FROM ""
WHERE (
    status = "InProgress" 
    AND contains(file.folder, "02-Notes")
)
SORT tags ASC ,category ASC,file.name ASC
```

