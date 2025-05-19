```dataview
TABLE WITHOUT ID 
    file.link AS "link", 
    tags AS tags,
    status AS "status",
    category AS category
    
    
FROM ""
 WHERE (
	contains(file.folder, "02-Notes")
) 

SORT category ASC,  tags ASC ,file.name ASC
``` 