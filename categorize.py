import pandas as pd

df = pd.read_excel("DatanCleaning.xlsx", sheet_name=0)

# Function for taking project titles and returning as a category using keyowrds

##Categories:Oncology, Neuro/Brain Disroders, Drug Delivery, Pain Management
#Imaging/Monitering, Cardiovascular, Musculoskeletal, Device Development



def categorize(title):
    title = str(title).lower()
    
    if any(word in title for word in ["cancer", "tumor", "oncology", "sarcoma", "carcinoma", "glioma", "glioblastoma", "ablation"]):
        return "Oncology"
    elif any(word in title for word in ["brain", "neuro", "alzheimer", "parkinson", "tremor", "seizure", "ptsd", "ocd", "addiction", "memory", "cognitive"]):
        return "Neuro/Brain Disorders"
    elif any(word in title for word in ["drug delivery", "blood-brain barrier", "nanoparticle", "gene therapy", "bbb"]):
        return "Drug Delivery"
    elif any(word in title for word in ["pain", "analges", "nocicepti"]):
        return "Pain Management"
    elif any(word in title for word in ["imaging", "mri", "diagnostic", "monitoring", "photoacoustic", "ultrasound scan"]):
        return "Imaging/Monitoring"
    elif any(word in title for word in ["heart", "cardiac", "cardiovascular", "artery", "vascular"]):
        return "Cardiovascular"
    elif any(word in title for word in ["bone", "muscle", "tendon", "fracture", "musculoskeletal"]):
        return "Musculoskeletal"
    elif any(word in title for word in ["transducer", "device", "hardware", "acoustic", "histotripsy", "array system"]):
        return "Device Development"
    else:
        #In case no catch
        return "Other"
    
#Applying function to each row's Project Title
df["Research Category"] = df["Project Title"].apply(categorize)

#Grants in each category
print(df["Research Category"].value_counts())

#New Excel file
df.to_excel("DataCategorized.xlsx", index=False)
print("\nSaved to DataCategorized.xlsx")