# 网络爬虫脚本

#### 描述
常见的网络爬虫: 图片爬虫、链接爬虫、糗事百科爬虫、微信爬虫、多线程爬虫


#### TODO

1. 图片爬虫:
   1. 使用`urlopen`打开网页并读取网页源码;
   2. 使用`findall`对网页源码进行第一次过滤, 把无关图片链接去除, 留下中间的商品列表部分;
   3. 使用`findall`对网页源码进行第二次过滤, 匹配商品列表的所有图片链接;
   4. 根据匹配到的图片链接，使用`urlretrieve`爬取对应的图片并保存到本地;

2. 链接爬虫

3. 糗事百科爬虫

### Note

1. 关于`findall`函数返回结果列表中每个元素包含的信息:
   - 当给出的正则表达式中不带括号时，列表的元素为字符串，此字符串为整个正则表达式匹配的内容;
   - 当给出的正则表达式中带有一个括号时，列表的元素为字符串，此字符串的内容与括号中的正则表达式相对应（而不是整个正则表达式的匹配内容）;
   - 当给出的正则表达式中带有多个括号时，列表的元素为多个字符串组成的tuple，tuple中字符串个数与括号对数相同，字符串内容与每个括号内的正则表达式相对应;

2. 使用`re.compile`函数将正则表达式预编译为正则表达式对象, 能够提高匹配的速度;

3. 关于限定符: `* + ? {n} {n,} {n, m}`

4. 关于正则表达式的模式

5. 关于 exec 函数的使用: 
   - exec 执行储存在字符串中的 Python 语句
   - `exec('print("Hello World")')` -> Hello World

### Issues

1. 使用 wiki 爬虫爬取 糗事百科 内容时出现以下异常
   - `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xed in position 81654: invalid continuation byte`
   - 触发该异常的原因是：出现了无法进行转换的 二进制数据 ;
   - 解决方法: `decode('utf-8', 'ignore')`
   - `UnicodeEncodeError: 'gbk' codec can't encode character '\U0001f602' in position 39: illegal multibyte sequence`
   - 触发该异常的原因是：在windows下面, 新文件的默认编码是 gbk , 而写入数据的编码则是 utf-8 , 因此导致无法解析;
   - 解决方法: `open('wiki.txt', 'w', encoding='utf-8')`
