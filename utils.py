import convertapi

def convert(imp, exp, conv):
    convertapi.api_secret = '9bgjl6kGBTSNh8Hk'
    convertapi.convert(exp, { 'File': conv }).save_files('convertedFile.' + exp)
    fileToSend = open("convertedFile." + exp, "rb")
    return fileToSend