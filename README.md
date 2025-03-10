## 0x01 简介

该项目是为了解决[RWCTF 4th Desperate Cat](https://github.com/voidfyoo/rwctf-4th-desperate-cat)，基于[ascii-zip](https://github.com/Arusekk/ascii-zip)进行修改，生成字节均在ASCII范围的特殊jar。

#### 1.1 生成包含class的ascii jar

```bash
➜ ascii-jar python3 ascii-jar-1.py
[-] CRC:False RDL:False CDL:True CDAFL:False Padding data: 1*A
[-] CRC:False RDL:False CDL:True CDAFL:False Padding data: 2*A
[-] CRC:False RDL:False CDL:True CDAFL:False Padding data: 3*A
......
[-] CRC:False RDL:True CDL:True CDAFL:True Padding data: 247*A
[+] CRC:True RDL:True CDL:True CDAFL:True Padding data: 248*A
[+] Generate ascii01.jar success
```

#### 1.2 生成包含`META-INF/resources/`的ascii jar


```bash
➜  ascii-jar python3 ascii-jar-2.py
[-] CRC:False RDL:True CDL:True CDAFL:True Padding data: 1*A
[-] CRC:False RDL:True CDL:True CDAFL:True Padding data: 2*A
[-] CRC:False RDL:True CDL:True CDAFL:True Padding data: 3*A
[-] CRC:False RDL:True CDL:True CDAFL:True Padding data: 4*A
[-] CRC:False RDL:True CDL:True CDAFL:True Padding data: 5*A
[-] CRC:False RDL:True CDL:True CDAFL:True Padding data: 6*A
[-] CRC:False RDL:True CDL:True CDAFL:True Padding data: 7*A
[-] CRC:False RDL:True CDL:True CDAFL:True Padding data: 8*A
[-] CRC:False RDL:True CDL:True CDAFL:True Padding data: 9*A
[-] CRC:False RDL:True CDL:False CDAFL:True Padding data: 10*A
[-] CRC:False RDL:True CDL:True CDAFL:True Padding data: 11*A
[-] CRC:False RDL:True CDL:True CDAFL:True Padding data: 12*A
[+] CRC:True RDL:True CDL:True CDAFL:True Padding data: 13*A
[+] Generate ascii02.jar success
```



## 0x02 改进

尽管得到了第一次padding之后满足条件的ascii jar，但是经过第二次padding前后脏字符，可能会出现最终的jar包不是ascii jar，所以要多加一层判断，对于第二次padding前后脏字符生成的jar也需要判断是否为ascii jar。

由于不同的java代码和jsp代码可能会有不同的padding效果，有些甚至需要padding `1w*A`才能最终生成ascii jar，所以笔者经过收集测试，在项目中准备了一些开箱即用的ascii jar，都只需padding < `1k*A`

- eviljsp：
  - shell.jsp：执行命令
  - behinder1.jsp：冰蝎jsp
  - behinder2.jsp：冰蝎jsp
  - Todo：整合内存马jsp
- evilclass
  - Exploit.java：简单执行命令
  - Todo：整合注入内存马
- eviljsp-jar/evilclass-jar：对应上面两个目录，有开箱即用的ascii jar，文件名为`[填充A的个数]-[filename].jar`



## 0x03 更多

* [RWCTF 4th Desperate Cat Writeup](https://mp.weixin.qq.com/s/QQ2xR32Fxj_nnMsFCucbCg)
* [RWCTF 4th Desperate Cat ASCII Jar Writeup](https://gv7.me/articles/2022/rwctf-4th-desperate-cat-ascii-jar-writeup/)
