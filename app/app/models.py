class PatientRecord:
    def __init__(self, feature_2, feature_3, feature_4, feature_5, feature_37, feature_43, feature_44):

        self.feature_2 = float(round(feature_2,2))
        self.feature_3 = float(round(feature_3,2))
        self.feature_4 = float(round(feature_4,2))
        self.feature_5 = float(round(feature_5,2))
        self.feature_37 = float(round(feature_37,2))
        self.feature_43 = float(round(feature_43,2))
        self.feature_44 = float(round(feature_44,2))
         
                                                                                                        
    def __str__(self):
        return '{\nfeature_2:'+str(self.feature_2)+',\nfeature_3:'+str(self.feature_3)+',\nfeature_4:'+str(self.feature_4)+',\nfeature_5:'+str(self.feature_5)+',\nfeature_37:'+str(self.feature_37)+',\nfeature_43:'+str(self.feature_43)+',\nfeature_44:'+str(self.feature_44)+'\n}'