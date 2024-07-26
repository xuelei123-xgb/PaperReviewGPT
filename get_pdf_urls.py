import jsonlines
import csv

# 输入文件名
input_file = 'total_notes.jsonl'
output_file = 'pdf_urls_1.csv'

# 用于存储pdf_url的集合，自动去重
pdf_urls = set()

# 读取JSONL文件
with jsonlines.open(input_file) as reader:
    for obj in reader:
        basic_dict = obj.get("basic_dict", {})
        reviews_msg = obj.get('reviews_msg', [])
        
        pdf_url = basic_dict.get("pdf_url", "")

        if pdf_url and reviews_msg:  # 检查pdf_url和reviews_msg是否都为空
            pdf_urls.add(pdf_url)

# 写入CSV文件
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['pdf_url'])  # 写入表头
    for url in pdf_urls:
        writer.writerow([url])

print(f'{len(pdf_urls)} unique PDF URLs have been written to {output_file}')
