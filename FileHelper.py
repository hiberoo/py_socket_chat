import time
import os


class FileHelper:
    log_name = time.strftime("%Y_%m_%d", time.localtime(time.time()))
    log_path = os.path.dirname(__file__) + "/" + log_name

    @staticmethod
    def write(content):
        print(FileHelper.log_path)
        with open(FileHelper.log_path, "a+", encoding="utf-8") as file:
            file.write(content)
            file.write("\r")
            print(content)
            file.close()


#test
if __name__ == "__main__":
    FileHelper.write("test1")
