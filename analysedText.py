class analysedText(object):
    
    def __init__ (self, text):
        self.fmtText=text.lower()
        self.fmtText=self.fmtText.replace(".","")
        self.fmtText=self.fmtText.replace(",","")
        self.fmtText=self.fmtText.replace("?","")
        self.fmtText=self.fmtText.replace("!","")
        
    
    def freqAll(self):        
        keys=self.fmtText.split(" ")
        values=[]
        
        for i in keys:
            values.append(keys.count(i))
        
        dic = dict(zip(keys,values))
        
        return dic
    
    def freqOf(self,word):
        keys=self.fmtText.split(" ")
        values=[]
        
        for i in keys:
            values.append(keys.count(i))
        
        dic = dict(zip(keys,values))
        
        try:
            return dic[word.lower()]
        
        except:
            print("No existe en la lista")
