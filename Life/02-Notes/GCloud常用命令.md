---
category:
  - Tech
tags:
  - GCP
status: Done
---
1. 复制文件
- **gcloud storage cp**
    ```bash
    gcloud storage cp --recursive my-data gs://my-bucket/backup
    ```
    
    这会把 `my-data` 目录下的所有内容复制到 `gs://my-bucket/backup`。如果您再次运行此命令，它会重新复制所有文件，并覆盖目标位置已有的文件。
    
2. 同步文件
- **gcloud storage rsync**
    ```bash
    gcloud storage rsync my-data gs://my-bucket/backup
    ```
     首次运行： 效果与 `cp` 类似，会将 `my-data` 的所有内容复制到 `gs://my-bucket/backup`。
     再次运行： 如果您在 `my-data` 中修改了一个文件或添加了一个新文件，`rsync` 只会上传那个被修改或新增的文件。如果 `my-data` 中的文件与 `gs://my-bucket/backup` 中的文件完全相同，则几乎不传输数据。
- **gcloud storage rsync -d**
    ```bash
    gcloud storage rsync -d my-data gs://my-bucket/backup
    ```
     镜像同步，gcs中的内容将会和my-data完全一致。如果在 `my-data` 中删除了一个文件，并且运行此命令，那么 `gs://my-bucket/backup` 中对应的文件也会被删除。
     
  