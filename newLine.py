def newline(time_dict):
    text = ''
    for key in time_dict.keys():
        text += key + '-' + time_dict[key] + '\n'

    return text