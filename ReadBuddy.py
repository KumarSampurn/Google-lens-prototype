import os
import cv2


class ReadBuddy:
    def __init__(self, parent_directory):
        self.parent_directory = parent_directory
        

    def create_folder_dictionary(self, new_path=None):
        
        folder_dict = {}
        
        new_folder_dict = {}
        
        for folder in os.listdir(self.parent_directory):
            
            folder_path = os.path.join(self.parent_directory, folder)
            
            if new_path:
                new_folder_path = os.path.join(new_path, folder)
                new_file_array=[]
            
            file_array = []
            
            for file in os.listdir(folder_path):
                
                if new_path:
                    new_file_path = os.path.join(new_folder_path, file)
                    new_file_array.append(new_file_path)
                
                file_path = os.path.join(folder_path, file)
                file_array.append(file_path)
                
            folder_dict[folder] = file_array
            
            if new_path:
                new_folder_dict[folder] = new_file_array
                
            

        return new_folder_dict,folder_dict

    def create_folder_image_dictionary(self, show=None):
        
        folder_dict = {}
        
        
        
        for folder in os.listdir(self.parent_directory):
            
            folder_path = os.path.join(self.parent_directory, folder)
            
            
            
            image_array = []
            
            for file in os.listdir(folder_path):
                
                file_path = os.path.join(folder_path, file)

                image=cv2.imread(file_path)
                image_array.append(image)  
                if show:
                    self.show_image(image)


                
            folder_dict[folder] = image_array

        return folder_dict

 