import requests
res = requests.post('http://192.168.3.101:5002/upload-image', json=[
    {
        'id':'123',
        'image':'https://images.freeimages.com/images/large-previews/371/swiss-mountains-1362975.jpg'
    },
    {
        'id':'345',
        'image':'https://image.freepik.com/free-vector/red-rooster-cock-side-view-abstract_1284-16627.jpg'
    }
])
