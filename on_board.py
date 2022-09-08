import os
from getpass import getpass

print("---------------------------------------------------------------------------------------------------------")
cloud = int(input("Kindly Select Your Cloud:\n1.MICROSOFT AZURE        2.AWS        3.GOOGLE CLOUD \n\nYour input: "))
print("---------------------------------------------------------------------------------------------------------")
centralizedpat = getpass("Enter Insight Central repo PAT tocken: ")
if cloud == 1:
    # os.system(f"git clone --sparse --filter=blob:none --depth=1 https://{centralizedpat}@dev.azure.com/nsitmspdevops/Insight%20CMP%20Centralized%20Repository/_git/onboard_script")
    os.system(f"git clone --sparse --filter=blob:none --depth=1 https://{centralizedpat}@dev.azure.com/nsitmspdevops/Development-Insight%20CMP%20Centralized%20Repository/_git/onboard_script")
    cwd = os.getcwd()
    os.chdir(f"{cwd}/onboard_script")
    if os.path.exists("azure-pipelines.yml"): os.system("rm azure-pipelines.yml")
    if os.path.exists("aws.py"): os.system("rm aws.py")
    if os.path.exists("gcp.py"): os.system("rm gcp.py")
    exec(open("azure.py").read())
    os.chdir(cwd)
    if os.path.exists("onboard_script"): os.system("rm -rf onboard_script")
elif cloud == 2:
    # os.system(f"git clone --sparse --filter=blob:none --depth=1 https://{centralizedpat}@dev.azure.com/nsitmspdevops/Insight%20CMP%20Centralized%20Repository/_git/onboard_script")
    os.system(f"git clone --sparse --filter=blob:none --depth=1 https://{centralizedpat}@dev.azure.com/nsitmspdevops/Development-Insight%20CMP%20Centralized%20Repository/_git/onboard_script")
    cwd = os.getcwd()
    os.chdir(f"{cwd}/onboard_script")
    if os.path.exists("azure-pipelines.yml"): os.system("rm azure-pipelines.yml")
    if os.path.exists("azure.py"): os.system("rm azure.py")
    if os.path.exists("gcp.py"): os.system("rm gcp.py")
    exec(open("aws.py").read())
    os.chdir(cwd)
    if os.path.exists("onboard_script"): os.system("rm -rf onboard_script")
elif cloud == 3:
    # os.system(f"git clone --sparse --filter=blob:none --depth=1 https://{centralizedpat}@dev.azure.com/nsitmspdevops/Insight%20CMP%20Centralized%20Repository/_git/onboard_script")
    os.system(f"git clone --sparse --filter=blob:none --depth=1 https://{centralizedpat}@dev.azure.com/nsitmspdevops/Development-Insight%20CMP%20Centralized%20Repository/_git/onboard_script")
    cwd = os.getcwd()
    os.chdir(f"{cwd}/onboard_script")
    if os.path.exists("azure-pipelines.yml"): os.system("rm azure-pipelines.yml")
    if os.path.exists("azure.py"): os.system("rm azure.py")
    if os.path.exists("aws.py"): os.system("rm aws.py")
    exec(open("gcp.py").read())
    os.chdir(cwd)
    if os.path.exists("onboard_script"): os.system("rm -rf onboard_script")
else:
    print("Wrong input received...")

    