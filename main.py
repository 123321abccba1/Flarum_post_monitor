import functions

def main():
  dic=functions.getPost()
  #[title,date,authorname,content,url]
  for fid in list(dic.keys()):
    print(fid)
    if not(functions.judgeIdInFile(fid)):
      print(functions.sendMessage(dic[fid][0],dic[fid][1],dic[fid][2],dic[fid][3],dic[fid][4]))
      functions.writeData(fid)


main()
