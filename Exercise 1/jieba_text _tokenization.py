import jieba
import xlrd
import xlwt
data = xlrd.open_workbook('web_crawler_res.xls')
table = data.sheet_by_name('data')
url = table.cell_value(1,0)
title = table.cell_value(1,1)
content = table.cell_value(1,2)
title = jieba.cut(title, cut_all = False)
content = jieba.cut(content, cut_all = False)
title= "/".join(title)
content = "/".join(content)
workbook = xlwt.Workbook(encoding='utf-8')
table = workbook.add_sheet('data')
table.write(0, 0, 'URL')
table.write(0, 1, 'Title')
table.write(0, 2, 'Content')
table.write(1, 0, url)
table.write(1, 1, title)
table.write(1, 2, content)
workbook.save('jieba_res.xls')
