from pyecharts import Geo

data = [("海门", 9), ("鄂尔多斯", 12), ("招远", 12), ("舟山", 12),
        ("齐齐哈尔", 14), ("盐城", 15), ("赤峰", 16), ("青岛", 18),
        ("乳山", 18), ("金昌", 19), ("泉州", 21), ("莱西", 21), ("日照", 21),
        ("胶南", 22), ("南通", 23), ("拉萨", 24), ("云浮", 24), ("梅州", 25),
        ("茂名", 22), ("湛江", 66), ("清远", 22), ("东莞", 35), ("深圳", 25),
        ("成都", 11), ("重庆", 55), ("泸州", 11), ("宜宾", 44)
        ]
geo = Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff", title_pos="center", width=1200, height=600,
          background_color='#404a59')
attr, value = geo.cast(data)
geo.add("", attr, value, visual_range=[0, 1000], visual_text_color="#fff", symbol_size=15, is_visualmap=True)
geo.show_config()
geo.render(path="pm25.html")
