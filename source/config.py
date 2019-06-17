input_dir = 'data/datasets/uic/'
output_dir = 'data/outputs/uic/'
input_file = 'uic_dataset_trimmed_segmented_04212019.csv' #'uic_dataset_trimmed_04112019.csv'
input_file = 'uic_dataset_trimmed_segmented_04212019.csv' #'uic_dataset_trimmed_04112019.csv'

deepspeech_dir = '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/deepspeech/'

perform_cross_validation = True

credential_file = './data/credentials/My_First_Project-761280e25a00.json'

# TODO: change this to simple variable or use .ini

'''
'toy'=False makes the model run only linear and Cs=[1,10]. 
'''
config = {
    'regression':False,
    'perform_cross_validation': False,
    'toy':True,
    'cluster': False,
    'test': True,
    'run_text':False,
    'run_audio':True,
    'create_features':False,
    'group_by': 'response',
    'gpt2': '/Users/danielmlow/Dropbox/gpt-2/models/117M/',
    'liwc':'/Users/danielmlow/Dropbox/data/liwc_english_dictionary/',
    'input':'./data/datasets/daic/',
    'util':'./data/util/',
    'output_dir':'./data/outputs/',
    'trainingFile':'depression_all_data.txt',
    'inputPath':'/Users/danielmlow/Dropbox/depression/data/input/',
    'audio_file':'text_audio_df.csv',
    'features':'NGRAM,HEDGE,LIWC,VADER,SENTI,MODAL,EMBED,PERSON,DISCOURSE',
    'feature_numbers':1000,
    'train_test_split': 0.2


}
