from src.helper.msg import Erris

class SaveJsonError(Exception):
    """ Exception for save json error """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    async def send_message(self):
        note = '🚨 *Error* 🚨\n\n'
        file = 'Note: visionofhumanity - server: 29.154 - yearly \n\n'
        try:
            await Erris().send_message(note + file + self.message)
        except Exception as e:
            print(f"Failed to send message: {e}")


class UploadS3Error(Exception):
    """ Exception for upload to s3 error """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    async def send_message(self):
        note = '🚨 *Error* 🚨\n\n'
        file = 'Note: visionofhumanity - server: 29.154 - yearly \n\n'
        try:
            await Erris().send_message(note + file + self.message)
        except Exception as e:
            print(f"Failed to send message: {e}")


class PageRequestError(Exception):
    """ Exception for page request error """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        
    async def send_message(self):
        note = '🚨 *Error* 🚨\n\n'
        file = 'Note: visionofhumanity - server: 29.154 - yearly \n\n'
        try:
            await Erris().send_message(note + file + self.message)
        except Exception as e:
            print(f"Failed to send message: {e}")


        
