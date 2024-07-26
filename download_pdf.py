import requests
import os
import pandas as pd
import re
import time

def get_paper_pdf(forum, pdf_url):
    if not os.path.exists('papers_pdf'):
        os.makedirs('papers_pdf')
        
    response = requests.get(pdf_url)
    with open(f'papers_pdf/{forum}.pdf', 'wb') as f:
        print(f"Downloading {forum}.pdf...")
        f.write(response.content)


if __name__ == '__main__':
    regex = re.compile(r"\?id=(.+)$")

    df = pd.read_csv("pdf_urls.csv")

    filenames = []
    for url in df["pdf_url"]:
        filename = re.findall(regex, url)[0]
        filenames.append(filename)
    df["b_forum"] = filenames
    
    # 假设 df_dup_forum 已经被定义且包含 'b_forum' 和 'b_pdf_url' 列
    df_dup_forum = df  # 这里仅为示例，实际中应根据实际情况定义 df_dup_forum
    df_dup_length = df_dup_forum.shape[0]

    for idx, row in df_dup_forum.iterrows():
        if idx % 10 == 0:
            print(f"{idx}/{df_dup_length}")
            # time.sleep(1.5)  # 可选：根据需要取消注释
        try:
            get_paper_pdf(row['b_forum'], row['pdf_url'])
        except Exception as e:  # 明确捕获异常类型
            print(f"Failed to download {row['b_forum']}.pdf: {e}")
            time.sleep(5)
            try:
                get_paper_pdf(row['b_forum'], row['pdf_url'])
            except Exception as e:
                print(f"Failed again to download {row['b_forum']}.pdf: {e}")
    