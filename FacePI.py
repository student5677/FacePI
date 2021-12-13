import fire,json

class FacePI:
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
    def detectImageUrl(self,imageurl):
        headers={
            #Request headers
            'Content-Type':'application/json',#用網路圖檔辨識

            'Ocp-Apim-Subscription-Key':self.readConfig()['api_key'],
        }

        params=urllib.parse.urlencode({

        
        })
   
if __name__=='__main__':
    fire.Fire(FacePI)
