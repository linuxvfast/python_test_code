#coding: utf-8
import smtplib
from email.mime.text import MIMEText

HOST = "smtp服务器地址"
SUBJECT = "官网流量数据报表"
TO = "接收人地址，如果报554将自己的邮箱也添加进去"
FROM = "发件人地址"

msg = MIMEText("""
    <table width="800" border="0" cellspacing="0" cellpadding="4">
      <tr>
        <td bgcolor="#CECFAD" height="20" style="font-size:14px">*官网数据  <a href="monitor.domain.com">更多>></a></td>
      </tr>
      <tr>
        <td bgcolor="#EFEBDE" height="100" style="font-size:13px">
        1）日访问量:<font color=red>152433</font>  访问次数:23651 页面浏览量:45123 点击数:545122  数据流量:504Mb<br>
        2）状态码信息<br>
        &nbsp;&nbsp;500:105  404:3264  503:214<br>
        3）访客浏览器信息<br>
        &nbsp;&nbsp;IE:50%  firefox:10% chrome:30% other:10%<br>
        4）页面信息<br>
        &nbsp;&nbsp;/index.php 42153<br>
        &nbsp;&nbsp;/view.php 21451<br>
        &nbsp;&nbsp;/login.php 5112<br>
	</td>
      </tr>
    </table>""","html","utf-8")
msg['Subject'] = SUBJECT
msg['From']=FROM
msg['To']=TO

try:
    server = smtplib.SMTP()
    server.connect(HOST,"25")
    server.starttls()
    server.login("发件人地址","授权密码(163邮箱需要使用授权密码)")
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()
    print("邮件发送成功！")
except Exception as e:
    print("失败："+str(e))
