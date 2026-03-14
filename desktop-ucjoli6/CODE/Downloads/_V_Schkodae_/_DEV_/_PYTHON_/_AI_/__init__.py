try:
    import os   # sys,
    if os.name == 'nt_':
        dirPath = os.getcwd()
        print(f" -> pwd : {dirPath} \n ")
except ImportError as IE:
    pass