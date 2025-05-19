
```dataview
Table without id 
	file.link as "link", 
	choice(length(category) > 0, category, "") as "category",
    choice(length(tags) > 0, tags, "") as "tags",
	dateformat(file.mtime, "yyyy-MM-dd HH:mm") as "last time" 
    
where file.mtime >= date(today) - dur(1 day)
sort file.mtime DESC
```
