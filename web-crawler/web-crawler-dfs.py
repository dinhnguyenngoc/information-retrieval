import os
import requests
from bs4 import BeautifulSoup

# Khai báo danh sách tập seeds chứa các URLs ban đầu
seeds = [
    #"https://vnexpress.net"
    "https://dantri.com.vn"
    #"https://vietnamnet.vn"
]

# Danh sách các URL đã truy cập
visited = []

# Chiều sâu duyệt tối đa của mỗi URL
MAX_DEPTH = 3

# vnexpress.net site:    
    # h1 class title-detail
    # p class desctiption
    # article class= fck_detail
# dantri.com.vn
    # h1 class title-page detail
    # h2 class singular-sapo
    # div class singular-content
# html_content: a beautifulsoup object
def get_article_content(html_content):        
    # vnexpress
    title = html_content.find("h1", {"class": "title-detail"})
    desc = html_content.find("p", {"class": "description"})
    content = html_content.find("article", {"class": "fck_detail"})
    if title is None:
        # dantri
        title = html_content.find("h1", {"class": "title-page detail"})
        desc = html_content.find("h2", {"class": "singular-sapo"})
        content = html_content.find("div", {"class": "singular-content"})
    if title is not None:
        title = title.text
        desc = desc.text
        content = content.text
        #print(f"title: " + title)
        return title + "\n" +  desc + "\n" + content
    return ""

# Viết hàm đệ quy để tiến hành quét qua các URLs trong tập seeds theo
def fetch_by_dfs(base, path, visited, max_depth=MAX_DEPTH, depth=0):
    # Kiểm tra xem chiều sâu hiện tại đã vượt quá [MAX_DEPTH] hay chưa
    if depth < max_depth:
        try:
            # Tải nội dung ở định dạng <html> của webpage hiện tại đang đứng
            # Ở bước này chúng ta có thể lưu nội dung của website vào CSDL để phục vụ cho việc chỉ mục sau này            
            html_content = BeautifulSoup(requests.get(base + path).text, "html.parser")
            
            file_name = (base + path).split('/')[-1].replace('.html', '').replace('.htm', '') + '.txt'
            print((base + path))
            # Lấy thư mục hiện tại của tập tin .py
            current_directory = os.path.dirname(os.path.abspath(__file__))                        
            article_content = get_article_content(html_content)
            if(file_name != '.txt' and len(article_content) > 0):
                file_path = os.path.join(current_directory, 'output', file_name)                
                with open(file_path, "w") as file:
                    file.write(article_content)
            
            # Lấy toàn bộ các thẻ <a> là các thẻ chứa hyper-links (href) của webpage đang đứng
            a_tags = html_content.find_all("a")
            
            # Duyệt qua từng hyper-links của webpage đang có
            for link in a_tags:

                # Lấy ra đường dẫn liên kết trong attribute [href]
                href = link.get("href")

                # Kiểm tra xem đường dẫn này chúng ta đã duyệt qua hay chưa? thông qua đối chiếu trong danh sách [visited]
                if href not in visited:
                    # Nếu chưa duyệt qua tiến hành bỏ hyper-link này vào [visited]
                    visited.append(href)
                    #print('Chiều sâu (depth) hiện tại: [{}/{}] - duyệt URL: [{}], '. format(depth, max_depth, href))                                        

                    # Kiểm tra xem đường dẫn này có phải là một đường dẫn hợp lệ - bắt đầu bằng http, ví dụ: https://vnexpress.net
                    if href.startswith("http"):
                        # Nếu hợp lệ - tiến hành gọi đệ quy hàm [fetch_by_dfs] duyệt hyper-link đang xét và tăng chiều sâu [depth] lên 1
                        fetch_by_dfs(href, "", visited, max_depth, depth + 1)
                    else:
                        # Nếu không hợp lệ thì tiếp tục quay lại hyper-link cha [base] và duyệt các hyper-links kế cạnh theo chiều ngang - tăng chiều sâu [depth] lên 1
                        fetch_by_dfs(base, href, visited, max_depth, depth + 1)
        except Exception as ex:
          print(ex)
          pass
      
# Duyệt qua từng URL có trong tập seeds
for url in seeds:
  #Bỏ url này vào danh sách [visited]
  visited.append(url)
  fetch_by_dfs(url, "", visited)
  
#get_content_by_url('https://vnexpress.net/nga-tuyen-bo-khong-co-gi-de-dam-phan-voi-ukraine-4783068.html')