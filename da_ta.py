from textblob.classifiers import NaiveBayesClassifier
class Da_ta:
    def __init__(self):
        self.train = [
            ('Hôm nay là thứ mấy ?', 'thời gian'),
            ('Mai là thứ mấy ?', 'thời gian'),
            ('Ngày kia là thứ mấy ?', 'thời gian'),
            ('Hôm nay là ngày bao nhiêu ?', 'thời gian'),
            ('Mai là ngày bao nhiêu ?', 'thời gian'),
            ('Ngày kia là ngày bao nhiêu ?', 'thời gian'),
            ('Năm nay là năm bao nhiêu ?', 'thời gian'),
            ('Tháng này là tháng mấy ?', 'thời gian'),
            ('Năm nay là năm bao nhiêu ?', 'thời gian'),
            ('Tháng này là tháng mấy ?', 'thời gian'),
            ('Thứ hai tuần sau là ngày bao nhiêu ?', 'thời gian'),
            ('Thứ ba tuần sau là ngày bao nhiêu ?', 'thời gian'),
            ('Thứ tư tuần sau là ngày bao nhiêu ?', 'thời gian'),
            ('Thứ năm tuần sau là ngày bao nhiêu ?', 'thời gian'),
            ('Thứ sáu tuần sau là ngày bao nhiêu ?', 'thời gian'),
            ('Thứ bảy tuần sau là ngày bao nhiêu ?', 'thời gian'),
            ('Chủ nhật tuần sau là ngày bao nhiêu ?', 'thời gian'),
            ]
        self.test = [
            ('Bia nặng quá.', 'ăn'),
            ('Tao là một người khó tính', 'giới thiệu'),
            ]
        self.cl = NaiveBayesClassifier(self.train)

    def updatedata(
        self,
        new_data = [
            ('She is my best friend.', 'pos'),
            ("I'm happy to have a new friend.", 'pos'),
            ("Stay thirsty, my friend.", 'pos'),
            ("He ain't from around here.", 'neg')
            ],
        ):
        self.cl.update(new_data)
        self.cl.accuracy(self.test)
        
da_ta = Da_ta()
