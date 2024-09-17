from pyflarum import FlarumUser
import requests
import json
from bs4 import BeautifulSoup

# Here, we initialize our `FlarumUser` object. You can't do anything without this first:

USER = FlarumUser(forum_url="YOUR FLARUM URL HERE")
token = 'YOUR PUSHPLUS TOKEN'


def judgeIdInFile(id):
  file = open("id.txt", "r")
  if id in file.read():
    file.close()
    return True
  else:
    file.close()
    return False


def writeData(id):
  file = open("id.txt", "a")
  file.write(id + "\n")
  file.close()


def getData():
  dic = {}
  data2=getPost()
  singlePost=[]
  for discussion in USER.get_discussions():
    singlePost=[]
    singlePost += data2[discussion.id]
    singlePost.append(discussion.url)
    singlePost.append(discussion.title)
    dic[discussion.id] = singlePost
  return dic

#[title,date,authorname,content,url]
def sendMessage(titles,time,user,content,bbsurl):
  url = 'http://www.pushplus.plus/send'
  title = 'Have new post in forum'  #The title of the message
  content = 'time：' + time + "\n" + "time:" + titles + "\n" + "user：" + user + "\n" + "Post link：" +"<a href=\"" +bbsurl +"\" rel=\" nofollow ugc\">"+bbsurl+"</a>"+ "\n" + "content:" +"\n"+content  #the Oush plus content 
  data = {
    "token":token,
    "title":title,
    "content":content,
    "topic":"sst",
    "template":"json"#Data type is json
}
  body=json.dumps(data).encode(encoding='utf-8')
  headers = {'Content-Type':'application/json'}
  request_result=requests.post(url,data=body,headers=headers)
  return request_result


def getPost():
  resultDict = {}
  for i in USER.get_discussions():
    if i.id == 10:
      continue
    postInfo = USER.get_discussion_by_id(i.id)
    temp = postInfo.get_author('first_number')["data"]["attributes"]["username"]
    resultDict[str(i.id)] = [postInfo.title, postInfo["data"]["attributes"]["createdAt"],temp
                        , postInfo["included"][0]["attributes"]["contentHtml"], "https://bbs.sstown.world/d/"+str(i.id)]
  return(resultDict)
