import pdb
import pandas as pd
import numpy as np
from unimol_tools import MolPredict

clf = MolPredict(load_model='./exp')
test_pred = clf.predict('./data/mol_test.csv')

test_res = np.where(test_pred > 0.5, 1, 0)
test_result = pd.DataFrame({
        'SMILES':clf.datahub.data['smiles'],
        'TARGET':test_res.flatten().tolist(),
    })

test_result.to_csv('./data/submission.csv', index=False)