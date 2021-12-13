class Config:
    def __init__(self) -> None:
        basepath=os.path.dirname(os.path.realpath(__fire__))
        self.configpath=os.path.join(basepath,'../Config.json')
    def readConfig(self):
        with open('Config.json','r',encoding='utf-8') as f:
            config=json.load(f)
        return config

    def writeConfig(self,config):
        with open('Config.json','w',encoding='utf-8') as f:
            json.dump(config,f)

    def setConfig(self):
        config=self.readConfig()
        print("[]為預設值，按enter表示不更動")
        api_key=input(f'輸入API_KEY[{config["api_key"]}]:')
        if api_key:config["api_key"]=api_key
        title=input(f'輸入title[{config["title"]}]:')
        if title:config["title"]=title

        self.writeConfig(config)
