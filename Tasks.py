import json
import time
class Task:
    
    def __init__(self,title):
        data=None
        with open("data.json","r") as f:
            data=json.load(f)
        ID=Task.get_last(data)
        self.title=title
        self.id=(ID+1)
        self.status="t"
        self.creation=time.time()
        self.updated=time.time()
        data[self.id]=[self.title,self.status,self.creation,self.updated]
        with open("data.json","w") as f:
            json.dump(data,f)
        print(f"Task created successfully, ID={self.id}")
    @staticmethod
    def update(id,new_task):
        with open("data.json","r") as f:
            data=json.load(f)
        if not data:
            print("No tasks created yet.")
            return None
        if id in data.keys():
            [title,status,creation,updated]=data[id]
            data[id]=[new_task,status,creation,time.time()]
            with open("data.json","w") as f:
                json.dump(data,f)
        else:
            print("Task ID does not exist in list")
    @staticmethod
    def delete(id):
        with open("data.json","r") as f:
            data=json.load(f)
        if not data:
            print("No data to delete")
            return None
        elif id in data.keys():
            del data[id]
            print(f"Task deleted with ID={id}")
            with open("data.json","w") as f:
                json.dump(data,f)
        else:
            print("Data doesn't exist")
    @staticmethod
    def listing(progess):
        with open("data.json","r") as f:
                data=json.load(f)
        if progess=="all":
            Task.display(data)
        elif progess=="done":
            ext_data=dict()
            for key in data.keys():
                if data[key][1]=="d":
                    ext_data[key]=data[key]
            Task.display(ext_data)
        elif progess=="in-progress":
            ext_data=dict()
            for key in data.keys():
                if data[key][1]=="ip":
                    ext_data[key]=data[key]
            Task.display(ext_data)
        elif progess=="todo":
            ext_data=dict()
            for key in data.keys():
                if data[key][1]=="t":
                    ext_data[key]=data[key]
            Task.display(ext_data)
    @staticmethod
    def display(data):
        for key in data.keys():
            print("========================Task=========================")
            Progress={"d":"Done","t":"To-Do","ip":"in-progress"}
            [title,progress,creation,updatedat]=data[key]
            print(f"Title:{title}\nProgress:{Progress[progress]}\nCreated At:{time.ctime(creation)}\nUpdated At:{time.ctime(updatedat)}\n=======================End Of Task=========================\n")
    @staticmethod
    def mark(id,new_type):
        Types={"in-progress":"ip","done":"d","todo":"t"}
        with open("data.json","r") as f:
            data=json.load(f)
        if not data:
            print("No tasks created yet.")
            return None
        if id in data.keys():
            [title,status,creation,updated]=data[id]
            data[id]=[title,Types[new_type],creation,time.time()]
            with open("data.json","w") as f:
                json.dump(data,f)
            print(f"Task with id {id} updated successfully")
        else:
            print("Task ID does not exist in list")
  
    @staticmethod
    def get_last(data):
        if not data:
            return 0
        return max(map(int,data.keys()))
          

    
