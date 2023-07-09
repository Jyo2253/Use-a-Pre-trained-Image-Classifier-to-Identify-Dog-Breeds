# Imports classifier function for using CNN to classify images 
from classifier import classifier 

# TODO 3: Define classify_images function below, specifically replace the None
#       below by the function definition of the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       res_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def classify_images(img_dir, res_dic, model):
    for key in res_dic:
        model_label = ""
        classified = classifier(img_dir+'/'+key,model)
 
        lowPetImage = classified.lower()
        

        wordListPetImage = lowPetImage
        """
        pet_name = ""
        
        for word in wordListPetImage:
            if word.isalpha():
                pet_name += word + " " """
        lowPetImage = lowPetImage.strip()
        #print("Classifier: " + lowPetImage)
        model_label = lowPetImage
        
        #res_dic[key].append(model_label)
        truth = res_dic[key][0]
        
        # Classifier Label
        if truth in model_label:
           res_dic[key].extend((model_label,1))
        else:
           res_dic[key].extend((model_label,0))
        
    print(res_dic)
