import os
import json
from datetime import datetime

# 创建示例文章数据
sample_articles = [
    {
        "id": 1,
        "title": "My first article",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "date": "August 7, 2024",
        "created_at": datetime.now().isoformat()
    },
    {
        "id": 2,
        "title": "Second article",
        "content": "这是第二篇文章的内容...",
        "date": "August 4, 2024",
        "created_at": datetime.now().isoformat()
    },
    {
        "id": 3,
        "title": "Third article",
        "content": "这是第三篇文章的内容...",
        "date": "August 1, 2024",
        "created_at": datetime.now().isoformat()
    },
    {
        "id": 4,
        "title": "Fourth article",
        "content": "中华人民共和国省级行政区是中华人民共和国的一级行政区划单位,包括23个省、5个自治区、4个直辖市和2个特别行政区,总计34个省级行政区。 [1] [7] [71]其行省制度从金末滥觞,元朝正式开始推行而延续至今。省级行政区既是国家行政管理的基本单元,也与经济社会发展及人民生活密切相关,深刻影响着社会活动的各个方面。1949年新中国成立初期,所设置的省级行政区的名称大多数沿用旧中国已存在的名称等,1951年省级政区数量达历史最高的53个,后经多次撤并(包括1958年调整为29个省级政区、1988年设立海南省、1997年增设重庆直辖市和香港特别行政区),至1999年澳门特别行政区设立后形成现行格局。 [8] [69-70]根据《中华人民共和国宪法》，省级行政区分为省、自治区、直辖市，特别行政区的设立由全国人民代表大会以法律规定。 [2] [4]省级陆地行政区域界线经1996年至2002年全面勘定,首次实现全部法定化,总长约62417公里。",
        "date": "August 1, 2024",
        "created_at": datetime.now().isoformat()
    }
]

# 创建文章目录
os.makedirs('articles', exist_ok=True)

# 保存示例文章
for article in sample_articles:
    filename = f"articles/article_{article['id']}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(article, f, ensure_ascii=False, indent=2)

print("示例文章已创建！")