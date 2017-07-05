# encoding=utf-8
'''


'''


TABLE_STYLPE = '''<style>
            table {
                border-collapse: collapse;
	            margin:0 auto;
	            width: 90%;
                }

            table, td, th {
                border: 1px solid black;

            }
	    th{
	        color:#e5efef;
	        background-color:#0a7ac1;
	        height:30% 
	    }
	    td{
	        height:20% 
	    }
        </style>'''


def Gen_html_table(table=None, TransKey=None):
    '''
    将字典生成html表格
    :param table: 表格数据，列表字典　［{},］
    :param TransKey: 字典key对应的翻译{}
    :return: html表格数据
    '''

    keys = table[0].keys()
    if isinstance(TransKey, dict) == False:
        TransKey = dict(zip(keys, keys))

    # 生成模板和表头
    tdmold = ""
    th = ''
    for key in keys:
        thcell = "<th>%s</th>" % TransKey.get(key,key)
        th += thcell
        tdcell = "<td style='height: 10px;'>{%s}</td>" % key
        tdmold += tdcell

    td_data = ""
    tdmold = "<tr>%s</tr>" % tdmold
    th_data = "<tr>%s</tr>" % th
    for item in table:
        td_data += tdmold.format(**item)
    html = TABLE_STYLPE + "<table>" + th_data + td_data + "</table>"
    return html

def dict_to_xlsx(file_path=None,**kwargs):
    '''
    e.g
    data = [{"name":"yuyuan","age":12},
            {"name": "yuy", "age": 12},
            {"name": "yuy2", "age": 12},
            {"name": "yuyuan2", "age": 12},
            {"name": "yuyuan1", "age": 12},
            {"name": "yuyua3", "age": 12},
            {"name": "yuyuan6", "age": 12},
            ]
    # html = Gen_html_table(data)
    dict_to_xlsx(入职=data)

    他可以传入多个data数据，生成多个工作薄。
    当传入文件路径的时候，返回执行情况，若是没有传入文件路径，文件内容。
    :param kwargs:
    :return:
    '''
    from xlwt import Workbook,Font,XFStyle,Alignment,Borders,Pattern
    import copy

    # 写工作簿
    def sheet_write(sdata):
        #字体
        fnt = Font()
        fnt.colour_index=40
        fnt.height = 13 * 20
        tab_hd_style = XFStyle()
        tab_hd_style.font = fnt

        # 显示位置
        alignment = Alignment()
        alignment.horz = 0x07 #横居中
        alignment.vert = 0x04 #自动回车显示
        tab_hd_style.alignment=alignment

        # 边框
        borders = Borders()  # Create Borders
        borders.left = 0x01  # May be: NO_LINE, THIN, MEDIUM, DASHED, DOTTED, THICK, DOUBLE, HAIR, MEDIUM_DASHED, THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED, THIN_DASH_DOT_DOTTED, MEDIUM_DASH_DOT_DOTTED, SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through 0x0D.
        borders.right = 0x01
        borders.top = 0x01
        borders.diag=0x01
        tab_hd_style.borders = borders


        #　背景
        pat = Pattern()
        pat.pattern= pat.SOLID_PATTERN
        pat.pattern_fore_colour=30
        tab_hd_style.pattern=pat

        key = sdata[0].keys()
        keyLen = len(key)
        tab_hd = zip(keyLen*[0,],range(keyLen),key,keyLen*[tab_hd_style,])
        [ws.write(*it) for it in tab_hd]
        for index in range(keyLen):
            ws.col(index).width = 0x0d00+4

        fnt1 = copy.deepcopy(fnt)
        fnt1.colour_index=0
        fnt1.height=10*20
        fnt1.outline=1

        alignment1 =Alignment()
        alignment1.horz=0x01

        pat1 = Pattern()
        pat1.pattern = pat.SOLID_PATTERN
        pat1.pattern_fore_colour = 70

        con_table_style =  copy.deepcopy(tab_hd_style)
        con_table_style.font=fnt1
        con_table_style.alignment=alignment1
        con_table_style.pattern=pat1

        # 写表格内容
        for index, item in zip(range(1,len(sdata)+1),sdata):
            length = len(item)
            tab_con = zip(length * [index, ], range(length), item.values(),length*[con_table_style,])
            [ws.write(*it) for it in tab_con]


        #冻表头
        ws.panes_frozen = True
        ws.horz_split_pos = 1



    w = Workbook(encoding='utf-8')
    for sheet in kwargs:
        ws = w.add_sheet(sheet)
        sheet_write(kwargs[sheet])

    if file_path is None:
        import tempfile,os

        tmpfd, tempfilename = tempfile.mkstemp()
        os.close(tmpfd)
        w.save(tempfilename)
        ft = open(tempfilename,"rb")
        res = ft.read()
        os.close(tmpfd)
        os.unlink(tempfilename)
        return res

    w.save(file_path)
    return True
