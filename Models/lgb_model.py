from Models.basemodel import *
import lightgbm as lgb
import pandas as pd

class lightgbm(BaseModel):
    def __init__(self):
        self.boosting_type = 'gbdt'
        self.n_estimators=100
        self.num_leaves=35
        self.max_depth=-1
        self.objective="binary"
        self.learning_rate=.01
        self.subsample=.8
        self.subsample_freq = 1
        self.max_bin=255
        self.subsample_for_bin=200000
        self.colsample_bytree=.8
        self.min_child_samples= 500
        self.min_split_gain=0.0
        self.min_child_weight=0.001
        self.min_child_samples=20     
        self.is_unbalance = False
        self.reg_alpha=0
    #    self.random_state=15
        self.reg_lambda=0 
        self.config_outname = "tuning_parameters"
    
    def lgb_params(self):
        return lgb.LGBMModel(boosting_type=self.boosting_type, 
                             num_leaves=self.num_leaves,
                             max_depth=self.max_depth,
                             learning_rate=self.learning_rate,
                             n_estimators=self.n_estimators,
                             max_bin=self.max_bin,
                             subsample_for_bin=self.subsample_for_bin,
                             objective=self.objective, 
                             min_split_gain=self.min_split_gain,
                             min_child_weight=self.min_child_weight,
                             min_child_samples=self.min_child_samples,
                             subsample=self.subsample,
                             subsample_freq=self.subsample_freq,
                             colsample_bytree=self.colsample_bytree,
                             reg_alpha=self.reg_alpha,
                             reg_lambda=self.reg_lambda,
        #                     random_state=self.random_state,
                            # n_jobs=n_jobs,
                             #silent=silent
                            )
        
        
class lgb_train(lightgbm):
    def __init__(self):
        self.sample_weight=None
        self.init_score=None
        self.group=None
        self.eval_set=None
        self.eval_names=None
        self.eval_sample_weight=None 
        self.eval_init_score=None
        self.eval_group=None
        self.eval_metric="gini_lgb"
        self.early_stopping_rounds=None
        self.verbose=True
        self.feature_name='auto'
        self.categorical_feature='auto'
        self.callbacks=None  
        self.preprocess = True
        self.config_outname = "train_parameters" 
    
    def set_eval_set(self,x,y,z= 0,w =None):
        if type(z) == "int":
            self.eval_set = [(preprocess_data(x),(y))]
            
        else:
            self.eval_set = [(preprocess_data(x),(y)),(preprocess_data(z),(w))]
    
    def Cat_features(self,f_cats):
        self.categorical_feature = f_cats
    
    def fit(self,clf,train,y):
        if self.preprocess:
            return clf.fit(preprocess_data(train),(y),self.sample_weight,self.init_score,self.group,self.eval_set, 
                           self.eval_names,self.eval_sample_weight,self.eval_init_score, self.eval_group,
                           self.eval_metric,self.early_stopping_rounds,self.verbose,self.feature_name, 
                           self.categorical_feature, self.callbacks)
    
def preprocess_data(train):
    train = pd.DataFrame(train)
    for c in list(set(train.select_dtypes(include=['object']).columns)):
        lbl = LabelEncoder()
        lbl.fit(list(train[c].values) )
        train[c] = lbl.transform(list(train[c].values))
    return train
        
                          
       
    
        