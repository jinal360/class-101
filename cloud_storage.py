import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from, file_to):
         dbx = dropbox.Dropbox(self.access_token)

        f =  open(file_from, 'rb') 
        dbx.files_upload(f.read(),file_to)

def main():
    acees_token = 'sl.AyQdKaFruW0U3RQSr7wztxyPdHbTVcG1GmDH0aIIZl73S3SeAne_RaCsGw-ujly0MI2E67V0sGo9qbTohdUlNObFvM_G0b9Mf48v87M5vPP7d05LFZfdPfhrdbIiwQMFUa8AD0Y'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer:")
    file_to = input("Enter the file path to upload to dropbox:")

    transferData.upload_file(file_from,file_to)
    print("file has been moved !!")

main()    