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
            #Request parameters
            'returnFaceId':'true',
            'returnFaceAttributes':'age,gender',
            #'recognitionModel':'recognition_04',
            'returnRecognitionModel':'false',
            'setectionModel':'detection_01',
            'faceIdTimeToLive':'86400',
        })
        #'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure'
        print('imageurl=',imageurl)
        requestbody='{"url":"'+imageurl+'"}'
        try:
            conn=http.client.HTTPSConnection(self.readConfig()['host'])
            conn.request("POST","/face/v1.0/detect?%s"%params,requestbody,headers)
            response=conn.getresponse()
            data=response.read()
            json_face_detect=json.loads(str(data,'UTF-8'))
            print("detectImageUrl.faces=",json_face_detect)
            conn.close()

            print("detectLocalImage:",
                f"{imageurl}偵測到{len(json_face_detect)}個人")
            return json_face_detect

            except Exception as e:
                print("[Errno {0}]連線失敗!請檢察網路設定。{1}".format(e.errno,e.strerror))
                #return []
   
if __name__=='__main__':
    fire.Fire(FacePI)
