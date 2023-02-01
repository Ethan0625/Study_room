import re
def solution(new_id):
    '''
    3<= id.lenght <=15
    step1 id.lower()
    stemp2 re.sub('[^a-z0-9]', ' ', new_id)
    '''
    new_id = re.sub('[^a-z0-9-_.]', '', new_id.lower())
    new_id = re.sub('[.]+','.', new_id)
    if len(new_id)==0:
        new_id == 'a'
    else:
        if new_id[0]=='.':
            if len(new_id)==1:
                new_id = 'a'
            else:
                new_id = new_id[1:]
        if new_id[-1]=='.':
            if len(new_id)==1:
                new_id = 'a'
            else:
                new_id = new_id[:-1]
    new_id = new_id[:15]
    if new_id[-1]=='.':
        new_id = new_id[:-1]
    if len(new_id)<=2:
        new_id = new_id.ljust(3,new_id[-1])
    return new_id