
from unimol_tools import MolTrain, MolPredict

clf = MolTrain(task='classification',
               data_type='molecule',
               epoch = 30,
               learning_rate=1e-4,
               batch_size=16,
               early_stopping=5,
               metrics='auc',
               split='random',
               save_path='./exp',
               remove_hs=True)

clf.fit('./data/mol_train.csv')