## 待处理
```dataview
TABLE WITHOUT ID 
    file.link AS "link", 
    category AS "category",
    tags AS tags,
    status AS "Status"
   

FROM ""
WHERE (
    length(category) = 0
	OR length(status) = 0
	AND contains(file.folder, "02-Notes")
)
SORT category ASC ,tags ASC ,file.name ASC
```