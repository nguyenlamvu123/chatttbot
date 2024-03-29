from textblob.classifiers import NaiveBayesClassifier
from bs4 import BeautifulSoup
import requests, os 

class Da_ta:
    def __init__(self):
        self.train = []
        self.test = [
            ('Hôm qua là thứ mấy ?', 'thời gian'),
            ('Hôm nay là thứ mấy ?', 'thời gian'),
            ('Mai là thứ mấy ?', 'thời gian'),
            ('Ngày kia là thứ mấy ?', 'thời gian'),
            ('Tháng này là tháng mấy ?', 'thời gian'),
            ('Năm trước là năm bao nhiêu ?', 'thời gian'),
            ('Tháng trước là tháng mấy ?', 'thời gian'),
            ('Thứ hai tuần sau là ngày bao nhiêu ?', 'thời gian'),
            ('Thứ ba tuần sau là ngày bao nhiêu ?', 'thời gian'),
            ('Thứ tư tuần sau là ngày bao nhiêu ?', 'thời gian'),
            ('Thứ năm tuần sau là ngày bao nhiêu ?', 'thời gian'),
            ('Thứ sáu tuần sau là ngày bao nhiêu ?', 'thời gian'),
            ('Thứ bảy tuần sau là ngày bao nhiêu ?', 'thời gian'),
            ('Chủ nhật tuần sau là ngày bao nhiêu ?', 'thời gian'),
            ('Qua có mát không ?', 'thời tiết'),
            ('Thời tiết hôm qua có oi không ?', 'thời tiết'),
            ('Hôm qua có dễ chịu không ?', 'thời tiết'),
            ('Mai có nắng không ?', 'thời tiết'),
            ('Ngày mai có mưa không ?', 'thời tiết'),
            ('Thời tiết ngày mai mát không ?', 'thời tiết'),
            ('Ngày mai có oi không ?', 'thời tiết'),
            ('Thời tiết mai có dễ chịu không ?', 'thời tiết'),
            ("Độ ẩm hôm nay bao nhiêu ?", 'thời tiết'),
            ("Độ ẩm hôm qua bao nhiêu ?", 'thời tiết'),
            ("Độ ẩm ngày mai bao nhiêu ?", 'thời tiết'),
            ("Nhiệt độ hôm nay bao nhiêu ?", 'thời tiết'),
            ("Nhiệt độ hôm qua bao nhiêu ?", 'thời tiết'),
            ("Nhiệt độ mai bao nhiêu ?", 'thời tiết'),
            ('Giá vàng hôm nay thế nào ?', 'tài chính'),
            ('Giá vàng hôm qua thế nào ?', 'tài chính'),
            ('Tỷ giá hôm nay thế nào ?', 'tài chính'),
            ('Tỷ giá hôm qua thế nào ?', 'tài chính'),
            ('Hôm qua là ngày bao nhiêu ?', 'thời gian'),
            ('Hôm nay là ngày bao nhiêu ?', 'thời gian'),
            ('Mai là ngày bao nhiêu ?', 'thời gian'),
            ('Ngày kia là ngày bao nhiêu ?', 'thời gian'),
            ('Năm sau là năm bao nhiêu ?', 'thời gian'),
            ('Tháng sau là tháng mấy ?', 'thời gian'),
            ('Năm nay là năm bao nhiêu ?', 'thời gian'),
            ('Thứ ba trước là ngày bao nhiêu ?', 'thời gian'),
            ('Thời tiết hôm nay thế nào ?', 'thời tiết'),
            ('Nay có nắng không ?', 'thời tiết'),
            ('Thời tiết hôm nay có mưa không ?', 'thời tiết'),
            ('Nay có mát không ?', 'thời tiết'),
            ('Hôm nay có oi không ?', 'thời tiết'),
            ('Thời tiết nay có dễ chịu không ?', 'thời tiết'),
            ('Hôm qua có nắng không ?', 'thời tiết'),
            ('Thời tiết hôm qua có mưa không ?', 'thời tiết'),
            ("Độ ẩm hôm nay bao nhiêu ?", 'thời tiết'),
            ('giá vàng ?', 'tài chính'),
            ]
##        self.test = []
        self.cl = NaiveBayesClassifier(self.train)

    @staticmethod 
    def saveload_model(cl=False, newdata=None):
        import _pickle as cPickle
##        import cPickle
        if not cl:
            with open(
                'save_training.pickle',
                'rb',
                ) as load_training:
                return cPickle.load(load_training) # LOAD TRAINED CLASSIFIER
        with open(
            'save_training.pickle',
            'wb',
            ) as save_training:
            cPickle.dump(cl, save_training)  # SAVE TRAINED CLASSIFIER

    def updatedata(
        self,
        typ_e,
        new_data = [
            ('She is my best friend.', 'pos'),
            ("I'm happy to have a new friend.", 'pos'),
            ("Stay thirsty, my friend.", 'pos'),
            ("He ain't from around here.", 'neg')
            ]
        ):
        import json
        with open (
            os.path.join(os.getcwd(), 'data', typ_e+ '.txt'),
            'w',
            encoding="utf-8"
            ) as f:
            f.write(json.dumps(new_data))
        self.cl.update(new_data)
        print(self.cl.accuracy(self.test))

    def soup_(self, url, typ_e=None):
        if not url == '':
##            headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
##            req = requests.get(url, headers=headers)
            req = requests.get(url, verify=False)
            soup = BeautifulSoup(req.content, 'html.parser')
        if not typ_e:
            return soup 
        elif typ_e == 'taichinh_':
            for new_data in self.taichinh_(soup):
                self.updatedata(new_data=new_data, typ_e=typ_e)
            return 
        elif typ_e == 'thoitiet':
##31072022            for new_data in self.thoitiet(soup):
##31072022                self.updatedata(new_data=new_data)
            new_data = self.thoitiet(soup)
        elif typ_e == 'taichinh':
##31072022            for new_data in self.taichinh(soup):
##31072022                self.updatedata(new_data=new_data)
            new_data = self.taichinh(soup)
        elif typ_e == 'thoigian':
            new_data = self.thoigian()
        else:
            input('error')
##        self.saveload_model(
##            filename=typ_e,
##            newdata=new_data
##            )
        self.updatedata(new_data=new_data, typ_e=typ_e)

    @staticmethod
    def thoitiet(soup):
        div = soup.find('div', id='list-news')
        new_data = []
        for art in div.find_all('article'):
##31072022            new_data = []
            h2 = art.find('h2', class_="title-news")
            if not h2:
                continue  # input(art.prettify())
            a = h2.find('a', {
                "data-medium": lambda x: "Item-" in x
                })
            soup0 = Da_ta().soup_(url=a['href'])
            section = soup0.find(
                'section',
                class_=lambda x: "page-detail" in x
                and "top-detail" in x
                )
            artle = section.find(
                'article',
                class_=lambda x: "fck_detail" in x
                )
            for p in artle.find_all('p', class_="Normal"):
                new_data.append((p.text, 'thời tiết'))
                # print(new_data)
##31072022            yield new_data
        return new_data

    @staticmethod
    def taichinh(soup):
        div_ = soup.find('div', class_='newsTop')
        div = div_.find('div', class_='col4')
        new_data = []
        for art in div.find_all('div', class_='itemBox'):
##31072022            new_data = []
            h2 = art.find('h3', class_="itemTitle")
            a = h2.find('a', {
                "href": True 
                })  # print(a['href'])
            soup0 = Da_ta().soup_(url=a['href'])
            section = soup0.find(
                'div',
                class_='contentMain'
                )
            artle = section.find(
                'div',
                class_='description'
                )
            for p in artle.find_all(
                'p',
                {
                    'style': "text-align: justify;"
                    }
                ):
                new_data.append((p.text, 'tài chính'))
                # print(new_data)
##31072022            yield new_data
        return new_data

    @staticmethod
    def taichinh_(soup):
        part = 1
        while part < 21:
            div_ = soup.find('div', class_="exam-content")
            if div_ is None:
                input("part: "+ str(part))
            div = div_.find('ul')
            new_data = []
            for art in div.find_all('li'):
    ##31072022            new_data = []
                a = art.find('a', href=True)
                cauhoi = a.find('p').text;print(cauhoi)
                new_data.append((cauhoi, 'tài chính'))
                for p in art.find_all('p'): 
                    pp = p.text;print(pp)
                    new_data.append((pp, 'tài chính'))
                    # print(new_data)
            part += 1
            soup = Da_ta().soup_(url=s['url'][:-1]+ str(part))
            yield new_data

    @staticmethod
    def thoigian(
        stri_="""Thời gian được tính bằng năm, tháng, tuần, ngày, giờ, phút, giây, Đêm. Trong đó, đơn vị cơ sở là "ngày", một ngày được chia làm 24 giờ (12 canh giờ - cách tính thường sử dụng thời xưa), 1 giờ chia thành 60 phút, 1 tuần gồm 7 ngày, 1 tháng bao gồm 28 đến 31 ngày tuỳ thuộc vào tháng trong năm,...

Theo quy ước hiện đại trong vật lý 1 giây được định nghĩa như sau:[2][3]

Giây là khoảng thời gian bằng 9,192,631,770 lần chu kỳ của bức xạ điện từ phát ra bởi nguyên tử Cs133 khi thay đổi trạng thái giữa hai mức năng lượng đáy siêu tinh vi.
Các đơn vị thời gian thông dụng khác được định nghĩa dựa trên khái niệm giây như sau:

Một phút có 60 giây
Một giờ có 60 phút
Một ngày có 24 giờ
Một tuần có 7 ngày
Một tháng có 4 tuần + 0, 1, 2, 3 ngày, (trung bình 30,4 ngày)
Một năm là khoảng thời gian trung bình của một chu kỳ Trái Đất quay quanh Mặt Trời, gồm có 12 tháng, hoặc 52 tuần 1 ngày, hoặc 365 ngày và 6 giờ.
Trong lý thuyết tương đối của Albert Einstein, đại lượng ct, với c là vận tốc ánh sáng và t là thời gian, được coi như là một chiều đặc biệt thêm vào cho không gian ba chiều để tạo thành không-thời gian[4][cần dẫn nguồn]. Việc cho thêm chiều thời gian giúp việc định vị các sự kiện được dễ dàng khi hệ quy chiếu thay đổi, tương tự như định vị các điểm trong không gian ba chiều cổ điển.

Vật lý cũng như nhiều ngành khoa học khác xem thời gian là một trong số những đại lượng cơ bản ít ỏi.[5]

Nó được dùng định nghĩa nhiều đại lượng khác như vận tốc nhưng nếu dùng những đại lượng như vậy mà định nghĩa trở lại thời gian sẽ tạo ra lối định nghĩa lòng vòng (tiếng Anh: circular definition).[6]

Một dạng định nghĩa operational về thời gian được diễn tả như sau: quan sát số lần lập cụ thể của một sự kiện có tính chu kì (như chuyển động của con lắc tự do) nảy sinh một loại đơn vị tiêu chuẩn như giây.

Thời Cổ đại người Trung Quốc thường tính thời gian theo Can Chi tức là chia thời gian theo các Canh theo thứ tự 12 con Giáp để tính thời gian trong ngày."""
        ):
        stri_ = [
            s for s in stri_.replace('.', '\n').split('\n')
            if not any([
                s.strip() == '',
                all([
                    s.strip().startswith('['),
                    s.strip().endswith(']'),
                    ])
                ])
            ]
        new_data = []
        for p in stri_:            
            new_data.append((p, 'thời gian'))
##        input(new_data)
        return new_data

    @staticmethod
    def onelink(url="https://thitruongtaichinhtiente.vn/vietnam-airlines-va-tinh-quang-binh-ky-ket-thoa-thuan-hop-tac-toan-dien-giai-doan-2022-2026-41674.html"):
        soup0 = Da_ta().soup_(url=url)
        try:
            section = soup0.find(
                'div',
                class_='contentMain'
                )
        except:                
            print(soup0)
            import traceback
            print(traceback.format_exc())
            input()
        artle = section.find(
            'div',
            class_='description'
            )
        for p in artle.find_all(
            'p',
            {
                'style': "text-align: justify;"
                }
            ):
            print(p.text)

    

da_ta = Da_ta()
##da_ta.onelink()
if os.path.exists(
    os.path.join(
        os.getcwd(),
        'save_training.pickle',
        )
    ):
    da_ta.cl = da_ta.saveload_model(cl=False)
else:
    for s in [
        {'url': '',
        'type': 'thoigian'},
        {'url': 'https://thitruongtaichinhtiente.vn/',
        'type': 'taichinh'},
        {'url': 'https://tracnghiem.net/dai-hoc/500-cau-trac-nghiem-tai-chinh-ngan-hang-44.html?mode=part&part=1',
        'type': 'taichinh_'},
        {'url': 'https://vnexpress.net/tag/du-bao-thoi-tiet-38424',
        'type': 'thoitiet'},
        ]:
        da_ta.soup_(
            url=s['url'],
            typ_e=s['type'],
            )
        da_ta.saveload_model(cl=da_ta.cl)
