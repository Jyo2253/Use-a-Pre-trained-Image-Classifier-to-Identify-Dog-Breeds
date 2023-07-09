# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (res_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as res_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          res_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the res_stats_dic dictionary that you create 
#       with this function
# 
def calculates_results_stats(res_dic):       
    res_stats_dic = dict()
    
    res_stats_dic['n_dogs_img'] = 0
    res_stats_dic['n_match'] = 0
    res_stats_dic['n_correct_dogs'] = 0
    res_stats_dic['n_correct_notdogs'] = 0
    res_stats_dic['n_correct_breed'] = 0       
    
    for key in res_dic:
         
        # Labels Match Exactly
        if res_dic[key][2] == 1:
            res_stats_dic['n_match'] += 1
            
        # Pet Image Label is a Dog AND Labels match- counts Correct Breed
        if res_dic[key][3] == 1 and res_dic[key][2] == 1:
            res_stats_dic['n_correct_breed'] += 1
        
        # Pet Image Label is a Dog - counts number of dog images
        if res_dic[key][3] == 1:
            res_stats_dic['n_dogs_img'] += 1
    
            # Classifier classifies image as Dog (& pet image is a dog)
            # counts number of correct dog classifications
            if res_dic[key][4] == 1:
                res_stats_dic['n_correct_dogs'] += 1
        
        # Pet Image Label is NOT a Dog
        else:
            # Classifier classifies image as NOT a Dog(& pet image isn't a dog)
            # counts number of correct NOT dog clasifications.
            if res_dic[key][4] == 0:
                res_stats_dic['n_correct_notdogs'] += 1
        
        
    # calculates number of total images
    res_stats_dic['n_images'] = len(res_dic)

    # calculates number of not-a-dog images using - images & dog images counts
    res_stats_dic['n_notdogs_img'] = (res_stats_dic['n_images'] - 
                                      res_stats_dic['n_dogs_img']) 
    
    res_stats_dic['pct_match'] = (res_stats_dic['n_match']/res_stats_dic['n_images'])*100
    
    # Calculates % correct dogs
    res_stats_dic['pct_correct_dogs'] = (res_stats_dic['n_correct_dogs']/res_stats_dic['n_dogs_img'])*100
    
    # Calculates % correct breed of dog
    res_stats_dic['pct_correct_breed'] = (res_stats_dic['n_correct_breed']/res_stats_dic['n_dogs_img'])*100
    
    
    # Calculates % correct not-a-dog images
    # Uses conditional statement for when no 'not a dog' images were submitted   
    if res_stats_dic['n_notdogs_img'] > 0:
        res_stats_dic['pct_correct_notdogs'] = (res_stats_dic['n_correct_notdogs'] /
                                                res_stats_dic['n_notdogs_img'])*100.0
    else:
        res_stats_dic['pct_correct_notdogs'] = 0.0

    return res_stats_dic
