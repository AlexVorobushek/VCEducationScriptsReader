from bs4 import BeautifulSoup
import warnings
warnings.simplefilter('ignore')

class Reader:
    @staticmethod
    def read_html(html_file: str) -> str:
        with open(html_file, "r", encoding='utf8') as file:
            html_code = file.read()
        soup = BeautifulSoup(html_code)
        return soup.get_text()


if __name__ == "__main__":
    with open("output.c", "w", encoding="utf8") as file:
        file.write(
            Reader.read_html("questionHtmlCode.html").replace(" ", " ")
            )
