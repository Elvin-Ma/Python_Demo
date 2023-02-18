import re

def demo_1():
    p = re.compile(r"test123")
    print(p.search("atest123b").span())

def demo_2():
    import re
    
    # re.match(pattern, string, flags=0)
    # print(re.match(r".","abc"))
    
    p = re.compile(r".")
    # print(p.match("abc"))
    # print(p.match("9bc"))
    # print(p.match("@bc"))
    # print(p.match(".bc"))
    # print(p.match("\tbc"))
    # print(p.match("\nbc"))

    p = re.compile(r".", flags=re.DOTALL)
    print(p.match("\nbc"))
    
def demo_3():
    import re

    p = re.compile(r"^ab")
    print(p.findall("abcd\nabfg"))

    p = re.compile(r"^ab", flags=re.MULTILINE)
    print(p.findall("abcd\nabfg"))

def demo_4():
    import re
    p = re.compile(r"cd$")
    # print(p.findall("abcd"))


    p = re.compile(r"cd$", flags=re.MULTILINE)
    print(p.findall("abcdefcd"))

def demo_5():
    import re
    p = re.compile(r"ab+?")
    print(p.search("a")) # 0次
    print(p.search("ab")) # 1次
    print(p.search("abb")) # 2次
    print(p.search("abbbc")) # 3次
    
def demo_6():
    import re
    p = re.compile(r"ab{2}")
    print(p.search("abc"))
    print(p.search("abbc"))
    print(p.search("abbbc"))

def demo_7():
    import re
    p = re.compile(r"ab{2,4}") # 贪婪模式
    # print(p.search("abc"))
    # print(p.search("abbc"))
    # print(p.search("abbbc"))
    # print(p.search("abbbbc"))
    # print(p.search("abbbbbc"))

    p = re.compile(r"ab{,4}")
    print(p.search("ac").group()) # 0个也算
    # print(p.search("abc"))

    # p = re.compile(r"ab{2,}")
    # print(p.search("abbbbc")) #贪婪模式
    # print(p.search("abbbbbc"))
    
def demo_8():
    import re
    p = re.compile(r"[deb]")
    print(p.search("abc"))
    print(p.search("aebcd"))
    
def demo_9():
    import re
    # 只匹配*号
    p = re.compile(r"\*")
    print(p.fullmatch("*"))

    # 只匹配+号
    p = re.compile(r"\+")
    print(p.fullmatch("+"))

    # 只匹配?号
    p = re.compile(r"\?")
    print(p.fullmatch("?"))
    
def demo_10():
    import re
  
    """ \1匹配的内容和第1组一定一样 """
    p = re.compile(r"(.+) \1")
    # print(p.search("abc abc"))
    # print(p.search("5 5"))
    
    # """ 两个组匹配的内容不一定一样 """
    p = re.compile(r"(.+) (.+)")
    print(type(p.search("ab abcd").groups()))
    # print(p.search("5 5"))
    
def demo_11():
    import re
    p = re.compile(r"[0-9]")
    print(p.search("a1234b"))
    
    p = re.compile(r"[0-9]+")
    print(p.search("a1234b"))
    
def demo_12():
    import re
    p = re.compile("\n")
    print(p.findall("\n"))
    
    # p = re.compile(r"\t")
    # print(p.findall("\t"))
    
    # p = re.compile(r"\\")
    # print(p.findall("\\"))
    
    # p = re.compile(r"\'")
    # print(p.findall("'"))
    
    # p = re.compile(r"\"")
    # print(p.findall('"'))
    
def demo_13():
    import re
    p = re.compile(r"b(.+)a(.+)e")
    m = p.match("babacdefg")
    # print(m)
    # print(m.group(1), m.group(2))
    # print(m.groups())
    # print(m.span(1), m.span(2))
    # print(m.start(1), m.end(1))
    # print(m.start(2), m.end(2))

    # 多个分组，返回元组列表
    # print(p.findall("babacdefg"))

    # 引用第1组匹配的内容
    p = re.compile(r"b(.+)a(\1)e")
    print(p.findall("babaabefg"))
    
def demo_14():
    import re
    p = re.compile(r"b(?:.+)a(?:.+)e")
    m = p.match("babacdefg")
    print(m)
    
def demo_15():
    import re

    """
    第一步：  .+[.] 匹配成功
    第二步：  前向肯定界定符匹配成功才继续第三步，否则匹配失败
    第三步：  .+ 接着第一步继续匹配
    最后结果为第一步和第三步匹配的结果 """
    p = re.compile(r".+[.](?=exe$).+")
    m = p.match("ab.exe")  # 文件名必须以exe为后缀
    print(m)
    
def demo_16():
    import re
    p = re.compile(r'blue|white|red')
    """ 把每一个从左开始非重叠匹配的字符串用其他字符串替换 """
    print(p.sub('colour', 'blue socks and red shoes'))
    print(p.sub('colour', 'blue socks and red shoes', count=1))
    
    def func(matchobj):
        if matchobj.group(0) == '-':
            return ' '
        else:
            return '-'

    """ 把每一个从左开始非重叠匹配的对象作为参数传入函数调用
    这个函数只能有一个 匹配对象 参数, 并返回一个替换字符串 """
    p = re.compile(r'-{1,2}')
    print(p.sub(func, 'pro----gram-files'))
    
def demo_17():
    import re
    p = re.compile(r'blue|white|red')
    print(p.subn('colour', 'blue socks and red shoes'))
    print(p.subn('colour', 'blue socks and red shoes', count=1))


    def func(matchobj):
        if matchobj.group(0) == '-':
            return ' '
        else:
            return '-'

    p = re.compile(r'-{1,2}')
    print(p.subn(func, 'pro----gram-files'))

def demo_18():
    import re
    p = re.compile(r"b(.+)a(.+)e")
    m = p.match("babacdefg")
    print(m)
    print(m.group())
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))
    print(m.group(2, 1, 0)) #注意一下
    
def demo_19():
    import re

    # 等价于 p = re.compile(r"\d+\.\d*")
    p = re.compile(r"""
                    \d +  # 匹配整数部分, re.X使得该空格不影响
                    \.    # 匹配小数点, re.X使得可以分段写
                    \d *  # 匹配小数部分, re.X使得该空格不影响
                    """, re.X)

    print(p.findall("1.2345.78"))
    
if __name__ == "__main__":
    # demo_1()
    # demo_2()
    # demo_3()
    # demo_4()
    # demo_5()
    # demo_6()
    # demo_7()
    # demo_8()
    # demo_9()
    # demo_10()
    # demo_11()
    # demo_12()
    # demo_13()
    # demo_14()
    # demo_15()
    # demo_16()
    # demo_17()
    # demo_18()
    demo_19()
    print("run reg_demo.py successfully !!!")