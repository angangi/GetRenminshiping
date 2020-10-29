from get_rmsp_article import get_article
from convert_to_docx import convert_to_docx
from get_urls import get_urls

urls = get_urls()
articles = []
for url in urls:
    try:
        article_dict = get_article(url=url)
        articles.append(article_dict)
    except IndexError:
        continue
convert_to_docx(articles=articles)
