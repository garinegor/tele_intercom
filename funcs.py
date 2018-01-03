import cognitive_face as CF
import os

KEY = '3c064f7a007c4ce2834f49aa740bcc42'
CF.Key.set(KEY)
CF.BaseUrl.set('https://westcentralus.api.cognitive.microsoft.com/face/v1.0/')

def who_is(path,group_id):
	to_r=None
	faces_result = CF.face.detect(path)
	if len(faces_result)==1:
		result=CF.face.identify([faces_result[0]['faceId']],group_id)
		print(result)
		if len(result[0]['candidates'])!=0:
			result=result[0]['candidates'][0]
			print(result)
			if result['confidence']>0.5:
				to_r=CF.person.get(group_id,result['personId'])['name']
	return to_r
def add_person(name,group=1):
	personId=CF.person.create(group,name)['personId']
	for filename in os.listdir('./persons/'+name):
		if filename[-4:]==".jpg":
			print('./persons/'+name+'/'+filename)
			CF.person.add_face('./persons/'+name+'/'+filename,group,personId)
		else:
			print(filename)
	CF.person_group.train(group)