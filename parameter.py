#basic architecture
CHAR_EMBEDDING_SIZE=100                 #字嵌入维度
WORD_EMBEDDING_SIZE=100                 #词嵌入维度
INPUT_SIZE=WORD_EMBEDDING_SIZE=100      #词嵌入维度

MAX_EPOCH=20                            #最大迭代次数
LAYER_NUM=2                             #lstm层数2
HIDDEN_UNITS_NUM=256                    #隐藏层结点数量
HIDDEN_UNITS_NUM2=256                   #隐藏层2结点数量
BATCH_SIZE=512                          #batch大小

#learning rate
LEARNING_RATE=0.001                      #学习率
DECAY=0.85                              #衰减系数

#Weaken Overfitting
DROPOUT_RATE=0.5                        #dropout 比率
LAMBDA_PW=0.5                           #PW层级正则化系数
LAMBDA_PPH=0.5                          #PW层级正则化系数
LAMBDA_IPH=0.5                          #PW层级正则化系数


#can't modify
CLASS_NUM=3                             #类别数量
MAX_SENTENCE_SIZE=30                    #固定句子长度为59 (从整个数据集得来)
TIMESTEP_SIZE=MAX_SENTENCE_SIZE         #LSTM的time_step应该和句子长度一致
WORD_VOCAB_SIZE=48028                   # 样本中不同字的个数+1(padding 0)，根据处理数据的时候得到