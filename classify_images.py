# Imports classifier function for using CNN to classify images 
from classifier import classifier 

# TODO 3: Define classify_images function below, specifically replace the None
#       below by the function definition of the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def classify_images(images_dir, results_dic, model):
    for key in results_dic:
        model_label = ""
        classified = classifier(images_dir+'/'+key,model)
 
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
        
        #results_dic[key].append(model_label)
        truth = results_dic[key][0]
        
        # Classifier Label
        if truth in model_label:
           results_dic[key].extend((model_label,1))
        else:
           results_dic[key].extend((model_label,0))
        
    print(results_dic)
