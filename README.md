# scrapy-frist

## 步骤

### 创建项目
``` bash
scrapy startproject scrapy_first

cd scrapy_first
scrapy genspider gitee-project 

```

### 编写代码内容
- spiders/gitee_project.py
- pipelines.py
- settings.py

### 运行
```
scrapy crawl gitee-project
```