import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

text = [
    "Sài Gòn, thành phố không ngủ với những con phố sầm uất và ánh đèn lấp lánh.",
    "Thành phố Hồ Chí Minh, nơi giao thoa giữa hiện đại và truyền thống.",
    "Sài Gòn là nơi tập trung của những món ăn đường phố ngon miệng và đa dạng.",
    "Từ quán cà phê ven đường đến nhà hàng sang trọng, Sài Gòn luôn đầy sức sống và sự năng động.",
    "Sài Gòn mang trong mình vẻ đẹp pha trộn giữa kiến trúc cổ điển Pháp và những tòa nhà chọc trời hiện đại.",
    "Người Sài Gòn thân thiện và luôn sẵn lòng giúp đỡ.",
    "Đến Sài Gòn, bạn có thể trải nghiệm cuộc sống về đêm sôi động và không khí náo nhiệt.",
    "Sài Gòn có những khu chợ truyền thống đầy màu sắc, nơi bạn có thể tìm thấy mọi thứ từ quần áo, đồ ăn đến đồ lưu niệm."
]

count = CountVectorizer()
word_count=count.fit_transform(text)
print("word_count",word_count)
print(word_count.toarray())


# IDF transformation
# count = TfidfVectorizer()
# word_count=count.fit_transform(text)

tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
tfidf_transformer.fit(word_count)

# In recently version of scikit-learn, method get_feature_names() was deprecated. We can use get_feature_names_out() instead.
df_idf = pd.DataFrame(tfidf_transformer.idf_, index=count.get_feature_names_out(),columns=["idf_weights"])

#inverse document frequency
df_idf.sort_values(by=['idf_weights'])
print("df_idf", df_idf)


#tfidf
tf_idf_vector=tfidf_transformer.transform(word_count)
feature_names = count.get_feature_names()

first_document_vector=tf_idf_vector[1]
df_tfifd= pd.DataFrame(first_document_vector.T.todense(), index=feature_names, columns=["tfidf"])

df_tfifd.sort_values(by=["tfidf"],ascending=False)
print("df_tfifd", df_tfifd)