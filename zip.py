from zipfile import ZipFile
name2=""

def zname(name):
  with ZipFile(name,'r') as zf:
    fname=zf.namelist()
    for name in fname:
      passw=bytes(name.replace('.zip',''), 'utf-8')
      print(passw)
      zf.extract(name,pwd=passw)
      name2=zname(name)  
    return name2             


with ZipFile('49805.zip','r') as zf:
  
  while True:
    print("name2:"+name2)
    if name2!="":
      passw=bytes(name2.replace('.zip',''), 'utf-8')
      print(name2)
      name2=zname(name2)
    else:
      fname=zf.namelist()
      for name in fname:
        passw=bytes(name.replace('.zip',''), 'utf-8')
        print(passw)
        zf.extract(name,pwd=passw)
        name2=zname(name)